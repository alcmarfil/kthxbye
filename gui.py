import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import sys
import io
import builtins
import threading
from queue import Queue

# Add src directory to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# interpreter components
from lexer.tokenizer import tokenize
from parser.parser import Parser
from semantics.interpreter import Interpreter
from semantics.environment import Environment
from parser.errors import ParseError, RuntimeError


class ConsoleIO:
    # class to redirect stdout/stderr to console widget (sa GUI instead na terminal)
    def __init__(self, console_widget, tag="output"):
        self.console = console_widget
        self.tag = tag
        self.buffer = ""
        
    def write(self, text):
        if text:  # Only write if there's actual text
            self.console.insert("end", text, self.tag)
            self.console.see("end")
            # Force update
            try:
                self.console.update_idletasks()
            except:
                pass
        
    def flush(self):
        pass
    
    def isatty(self):
        return False


class LOLCodeGUI:
    # initialiaze the app
    def __init__(self, root):
        self.root = root
        self.root.title("ANG POGI NI SIR AARON LOLTERPRETER")
        self.root.geometry("1920x1080")
        self.root.minsize(1000, 600)
        
        # Variables
        self.current_file = None
        self.input_queue = Queue() # handles user input
        self.input_waiting = False 
        self.input_var_name = None
        self.input_start_pos = None
        
        # Setup GUI
        self.setup_gui()
        
        # Redirect stdout/stderr
        self.setup_io_redirect()
        
    def setup_gui(self): # Visual compotnents
        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Top frame: File explorer and Run button
        top_frame = tk.Frame(main_frame, bg="#f0f0f0")
        top_frame.pack(fill=tk.X, pady=(0, 5))
        
        # File selection
        file_frame = tk.Frame(top_frame, bg="#f0f0f0")
        file_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(file_frame, text="File:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        self.file_path_var = tk.StringVar(value="No file selected")
        file_label = tk.Label(file_frame, textvariable=self.file_path_var, 
                             bg="#ffffff", relief=tk.SUNKEN, anchor="w", 
                             padx=5, pady=2, font=("Arial", 9))
        file_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        browse_btn = tk.Button(file_frame, text="Browse...", command=self.browse_file,
                               bg="#2196F3", fg="white", font=("Arial", 9, "bold"),
                               padx=10, pady=2)
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        # Run button
        run_btn = tk.Button(top_frame, text="▶ Run", command=self.run_code,
                           bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                           padx=20, pady=5)
        run_btn.pack(side=tk.RIGHT, padx=5)
        
        # Middle frame: Text editor and side panels
        middle_frame = tk.Frame(main_frame, bg="#f0f0f0")
        middle_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel: Text editor
        editor_frame = tk.LabelFrame(middle_frame, text="Text Editor", 
                                    font=("Arial", 10, "bold"), bg="#f0f0f0")
        editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Create frame for editor with line numbers
        editor_container = tk.Frame(editor_frame, bg="#f0f0f0")
        editor_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Line numbers widgetss
        self.line_numbers = tk.Text(editor_container, width=4, padx=3, pady=5,
                                   takefocus=0, border=0, background="#f5f5f5",
                                   state=tk.DISABLED, wrap=tk.NONE,
                                   font=("Consolas", 11))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Main editor
        editor_text_frame = tk.Frame(editor_container)
        editor_text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.editor = tk.Text(editor_text_frame, wrap=tk.WORD,
                             font=("Consolas", 11),
                             bg="#ffffff", fg="#000000",
                             insertbackground="#000000",
                             padx=5, pady=5)
        
        # Scrollbars
        # scrolls both editor and line numbers together
        editor_v_scroll = ttk.Scrollbar(editor_text_frame, orient=tk.VERTICAL, command=self.on_editor_scroll) 
        editor_h_scroll = ttk.Scrollbar(editor_text_frame, orient=tk.HORIZONTAL, command=self.editor.xview)
        
        self.editor.config(yscrollcommand=self.on_text_scroll, xscrollcommand=editor_h_scroll.set)
        
        # Pack widgets
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        editor_v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        editor_h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind events for line number updates
        self.editor.bind("<KeyRelease>", self.on_editor_change)
        self.editor.bind("<Button-1>", self.on_editor_change)
        self.editor.bind("<MouseWheel>", self.on_editor_change)
        self.editor.bind("<<Modified>>", self.on_editor_change)
        
        # Bind paste event
        self.editor.bind("<Control-v>", lambda e: self.root.after(10, self.on_editor_change))
        self.editor.bind("<Button-3>", lambda e: self.root.after(10, self.on_editor_change))  # Right-click paste
        
        # Initial line numbers update
        self.update_line_numbers()
        
        # Right panel: Tokens and Symbol Table
        right_panel = tk.Frame(middle_frame, bg="#f0f0f0")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(5, 0))
        
        # lexeme list
        tokens_frame = tk.LabelFrame(right_panel, text="Lexemes", 
                                    font=("Arial", 10, "bold"), bg="#f0f0f0")
        tokens_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Lexemess
        tokens_tree = ttk.Treeview(tokens_frame, columns=("Value", "Type", "Line", "Column"),
                                   show="headings", height=12)
        tokens_tree.heading("Value", text="Value")
        tokens_tree.heading("Type", text="Type")
        tokens_tree.heading("Line", text="Line")
        tokens_tree.heading("Column", text="Column")
        
        tokens_tree.column("Value", width=150, anchor="w")
        tokens_tree.column("Type", width=150, anchor="w")
        tokens_tree.column("Line", width=60, anchor="center")
        tokens_tree.column("Column", width=60, anchor="center")
        
        tokens_scroll = ttk.Scrollbar(tokens_frame, orient=tk.VERTICAL, command=tokens_tree.yview)
        tokens_tree.configure(yscrollcommand=tokens_scroll.set)
        
        tokens_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tokens_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tokens_tree = tokens_tree
        
        # Symbol Table
        symbol_frame = tk.LabelFrame(right_panel, text="Symbol Table", 
                                     font=("Arial", 10, "bold"), bg="#f0f0f0")
        symbol_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview for symbol table
        symbol_tree = ttk.Treeview(symbol_frame, columns=("Variable", "Value"),
                                   show="headings", height=12)
        symbol_tree.heading("Variable", text="Variable")
        symbol_tree.heading("Value", text="Value")
        
        symbol_tree.column("Variable", width=120, anchor="w")
        symbol_tree.column("Value", width=150, anchor="w")
        
        symbol_scroll = ttk.Scrollbar(symbol_frame, orient=tk.VERTICAL, command=symbol_tree.yview)
        symbol_tree.configure(yscrollcommand=symbol_scroll.set)
        
        symbol_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        symbol_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.symbol_tree = symbol_tree
        
        # Bottom frame: Console
        console_frame = tk.LabelFrame(main_frame, text="CONSOLE", 
                                     font=("Arial", 10, "bold"), bg="#f0f0f0")
        console_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        self.console = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD,
                                                font=("Consolas", 10),
                                                bg="#1e1e1e", fg="#d4d4d4",
                                                insertbackground="#ffffff",
                                                height=10)
        self.console.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # make console editablee
        self.console.config(state=tk.NORMAL)
        
        # Add welcome message
        self.console.insert("end", "Let's code! LOL!\n", "output")
        

        # Color coding sa console
        self.console.tag_config("output", foreground="#d4d4d4")
        self.console.tag_config("error", foreground="#f48771")
        self.console.tag_config("input", foreground="#4ec9b0")
        self.console.tag_config("prompt", foreground="#4ec9b0", font=("Consolas", 10, "bold"))
        
        # Bind Enter key for input
        self.console.bind("<Return>", self.handle_console_input)

        # Bind keypress events to monitor cursor position
        self.console.bind("<KeyPress>", self.on_console_key)
        self.console.bind("<Button-1>", self.on_console_click)
        
        # Clear button for console
        clear_btn = tk.Button(console_frame, text="Clear Console", command=self.clear_console,
                             bg="#ff9800", fg="white", font=("Arial", 9),
                             padx=10, pady=2)
        clear_btn.pack(side=tk.BOTTOM, anchor=tk.E, padx=5, pady=2)
        
    def setup_io_redirect(self):
        # save original io so we can restore later
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.original_input = builtins.input
        
    def restore_io(self):
        # put everything back 
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
        builtins.input = self.original_input
        
    def on_console_click(self, event):
        # handles mouse click 
        if not self.input_waiting or not self.input_start_pos:
            return None
        
        try:
            # Get click position
            click_pos = self.console.index(f"@{event.x},{event.y}")
            # if clicked before input start, move to input start
           #  prevents user from clicking before the input prompt.
            if self.console.compare(click_pos, "<", self.input_start_pos):
                self.console.mark_set(tk.INSERT, self.input_start_pos)
                return "break"
        except:
            pass
        return None
    
    def on_console_key(self, event):
        # prevent editing outside input area"""
        if not self.input_waiting:
            # If not waiting for input, allow normal editing
            return None
        
        # If waiting for input, ensure console is editable
        if self.console.cget("state") != tk.NORMAL:
            self.console.config(state=tk.NORMAL)
        
        # use after() to check position after the key is processed
        # This allows normal typing to work
        self.root.after(10, self.check_cursor_position)
        
        return None  # Always allow the key press
    
    def check_cursor_position(self):
        # Check and correct cursor position after key press
        if not self.input_waiting or not self.input_start_pos:
            return
        
        try:
            current_pos = self.console.index(tk.INSERT)
            # if cursor moved before input start move it back
            if self.console.compare(current_pos, "<", self.input_start_pos):
                self.console.mark_set(tk.INSERT, self.input_start_pos)
        except:
            pass
    
    def handle_console_input(self, event):
        # Handle Enter key press when waiting for input
        if not self.input_waiting:
            # Normal Enter behavior (new line lang)
            return None
        
        # Get input value from console
        if self.input_start_pos:
            try:
                # Get text from input start to end of line
                end_pos = self.console.index(f"{self.input_start_pos} lineend")
                input_text = self.console.get(self.input_start_pos, end_pos).strip()
                
                # Add newline after input (or not ano ba mas maganda)
                self.console.insert("end", "\n")
                self.console.see("end")
                
                # Put result in queue
                self.input_queue.put(input_text)
                self.input_waiting = False
                self.input_start_pos = None
                self.input_var_name = None
                
                return "break"  # Prevent default newline
            except Exception as e:
                # Error getting input, use empty string
                self.input_queue.put("")
                self.input_waiting = False
                self.input_start_pos = None
                self.input_var_name = None
        else:
            self.input_queue.put("")
            self.input_waiting = False
        
        return "break"
    
    def custom_input(self, prompt=""):
        # Custom input function that uses console for input
        # ensure console is editable
        self.console.config(state=tk.NORMAL)
        
        # Mark the start position for input 
        # Get position at the end
        self.input_start_pos = self.console.index(tk.END + "-1c")
        self.input_waiting = True
        
        # Focus on console and set cursor position
        self.console.focus_set()
        self.console.mark_set(tk.INSERT, self.input_start_pos)
        self.console.see(tk.INSERT)
        self.root.update_idletasks()
        
        # Wait for input
        result = self.wait_for_input()
        
        # Reset variable name for next input / iwas overlap
        self.input_var_name = None
        
        return result
    
    def wait_for_input(self):
        # wait for input using queue with event processing
        import time # make sure lang
        start_time = time.time()
        timeout = 300  # 5 minute timeout 
        
        while self.input_waiting and (time.time() - start_time) < timeout:
            # Process GUI events
            self.root.update_idletasks()
            self.root.update()
            
            # Check if input is ready
            try:
                result = self.input_queue.get_nowait()
                return result
            except:
                # No input yet, continue waiting
                time.sleep(0.01)  # Small delay to 
                continue
        
        # Timeout or cancelled
        if self.input_waiting:
            # Still waiting but timed out, cancel it
            self.input_waiting = False
            self.input_start_pos = None
            self.input_var_name = None
        return ""
        
        """
        lolcode code calls GIMMEH 
        Interpreter calls custom_input()
        custom_input sets input_waiting = True
        wait_for_input loops-> processing GUI events
        user types and presses Enter -> handle_console_input triggered
        input text put in input_queue
        wait_for_input gets text from queue and returns it
        interpreter receives the input value"""


    def on_editor_scroll(self, *args):
        # when scrollbar moves scroll both editor and line numbers
        self.editor.yview(*args)
        self.line_numbers.yview(*args)
    
    def on_text_scroll(self, first, last):
        # sync scrollbar and line numbers
        # Update the scrollbar
        self.editor.yview_moveto(first)
        # Sync line numbers
        self.line_numbers.yview_moveto(first)
        # Return the values for the scrollbar
        return first, last
    
    def on_editor_change(self, event=None):
        self.update_line_numbers()
    
    def update_line_numbers(self):
        # update line numbers display
        # Get current line count
        content = self.editor.get(1.0, tk.END)
        line_count = content.count('\n')
        
        # Update line numbers
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)
        
        # Add line numbers
        for i in range(1, line_count + 1):
            self.line_numbers.insert(tk.END, f"{i}\n")
        
        self.line_numbers.config(state=tk.DISABLED)
        
        # Sync scrolling
        try:
            self.line_numbers.yview_moveto(self.editor.yview()[0])
        except:
            pass
    
    def browse_file(self):
        # open file browser to select lol file
        file_path = filedialog.askopenfilename(
            title="Select LOLCODE File",
            filetypes=[("LOLCODE files", "*.lol")]
        )
        
        if file_path:
            self.current_file = Path(file_path)
            self.file_path_var.set(str(self.current_file))
            
            # load file content into editor
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.editor.delete(1.0, tk.END)
                self.editor.insert(1.0, content)
                self.update_line_numbers()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file:\n{e}")
                
    def clear_console(self):
       # clear console
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.NORMAL)
        
    def update_tokens_display(self, tokens):
        # Clear existing items
        for item in self.tokens_tree.get_children():
            self.tokens_tree.delete(item)
     # populate sthe Lexemes table with tokens
        # add lexemes
        for token in tokens:
            self.tokens_tree.insert("", tk.END, values=(
                repr(token.get("value", "")), 
                token.get("type", ""),  
                token.get("line", ""),
                token.get("column", "")
            ))
            
    def update_symbol_table(self, env):
        #Update symbol table 
        for item in self.symbol_tree.get_children():
            self.symbol_tree.delete(item)
            
        # from env table 
        if env.var_table:
            for var_name, var_value in sorted(env.var_table.items()):
                value_str = str(var_value)
                    
                self.symbol_tree.insert("", tk.END, values=(var_name, value_str))
        else:
            # Show message when symbol table is empty (or not TODO: tanong)
            self.symbol_tree.insert("", tk.END, values=("(No variables)", ""))

            
    def run_code(self):
            #Execute the code from the editor
            # Clear console
            self.clear_console()
            
            # Get code from editor
            code = self.editor.get(1.0, tk.END)
            
            if not code.strip():
                messagebox.showwarning("Warning", "No code to execute!")
                return
                
            # Redirect I/O
            sys.stdout = ConsoleIO(self.console, "output")
            sys.stderr = ConsoleIO(self.console, "error")
            builtins.input = self.custom_input
            
            try:
                # Tokenize
                #eror show in console and stop
                # display tokens in Lexemes table
                try:
                    tokens = tokenize(code)
                except ValueError as e:
                    error_msg = f"Lexical Error: {str(e)}\n"
                    self.console.insert("end", error_msg, "error")
                    self.console.see("end")
                    self.restore_io()
                    return
                except Exception as e:
                    error_msg = f"Tokenization Error: {str(e)}\n"
                    self.console.insert("end", error_msg, "error")
                    self.console.see("end")
                    self.restore_io()
                    return
                
                tokens_dict = [
                    {
                        "type": token.type,
                        "value": token.value,
                        "line": token.line,
                        "column": token.column
                    }
                    for token in tokens
                ]
                
                # update lexemes
                self.update_tokens_display(tokens_dict)
                self.root.update()
                
                # Parse
                try:
                    parser = Parser(tokens_dict) # analyzes token structure
                    ast = parser.parse() #builds ast
                except Exception as e:
                    error_msg = f"Parse Error: {str(e)}\n"
                    self.console.insert("end", error_msg, "error")
                    self.console.see("end")
                    self.restore_io()
                    return
                
                if isinstance(ast, dict) and ast.get("error", False):
                    error_msg = f"Parse Error: {ast['message']}\n"
                    error_msg += f"Line {ast.get('line', '?')}, Column {ast.get('column', '?')}\n"
                    self.console.insert("end", error_msg, "error")
                    self.console.see("end")
                    self.restore_io()
                    return
                
                # Interpret
                env = Environment() # Create variable storage
                interpreter = Interpreter() # Create interpreter
                
                prelude_section = ast.get("prelude", [])
                if prelude_section:
                    for func in prelude_section:
                        try: 
                            interpreter.evaluate(func, env)
                            # update symbol table after prelude functions
                            self.update_symbol_table(env)
                            self.root.update()
                        except RuntimeError as e:
                            error_msg = f"Runtime Error in prelude: {e.message}\n"
                            self.console.insert("end", error_msg, "error")
                            self.console.see("end")
                postlude_section = ast.get("postlude", [])
                if postlude_section:
                    for func in postlude_section:
                        try:
                            interpreter.evaluate(func, env)
                            # update symbol table after postlude functions
                            self.update_symbol_table(env)
                            self.root.update()
                        except RuntimeError as e:
                            error_msg = f"Runtime Error in postlude: {e.message}\n"
                            self.console.insert("end", error_msg, "error")
                            self.console.see("end")
                # Evaluate declarations (from WAZZUP section)
                wazzup_section = ast.get("wazzup")
                if wazzup_section:
                    if isinstance(wazzup_section, dict):
                        declarations = wazzup_section.get("declarations", [])
                    else:
                        # Handle case where wazzup might be None or different structure
                        declarations = []
                        
                    for dec in declarations:
                        try:
                            interpreter.evaluate(dec, env)
                            self.update_symbol_table(env)
                            self.root.update()
                        except RuntimeError as e:
                            error_msg = f"Runtime Error in declaration: {e.message}\n"
                            self.console.insert("end", error_msg, "error")
                            self.console.see("end")
                
                # Update symbol table after declarations (even if empty)
                self.update_symbol_table(env)
                self.root.update()
                
                # Evaluate statements
                statements = ast.get("statements", [])
                if statements:
                    for stmt in statements:
                        try:
                            # Capture variable name if this is an InputStatement
                            if isinstance(stmt, dict) and stmt.get("node_type") == "InputStatement":
                                self.input_var_name = stmt.get("target")
                            
                            interpreter.evaluate(stmt, env)
                            # Update symbol table after each statement (in case variables are created)
                            self.update_symbol_table(env)
                            self.root.update()
                        except RuntimeError as e:
                            error_msg = f"Runtime Error: {e.message}\n"
                            self.console.insert("end", error_msg, "error")
                            self.console.see("end")
                            break
                        except Exception as e:
                            error_msg = f"Error: {str(e)}\n"
                            self.console.insert("end", error_msg, "error")
                            self.console.see("end")
                            break
                
                # final symbol table update
                self.update_symbol_table(env)
                self.root.update()
                
            except Exception as e:
                error_msg = f"Unexpected Error: {str(e)}\n"
                self.console.insert("end", error_msg, "error")
                import traceback
                tb_str = traceback.format_exc()
                self.console.insert("end", tb_str, "error")
                self.console.see("end")
            finally:
                # Restore I/O
                self.restore_io()
                # Force console update
                self.console.see("end")
                self.root.update_idletasks()
            
def main():
    root = tk.Tk()
    app = LOLCodeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()