from parser.errors import RuntimeError

class Environment:
    def __init__(self, parent=None):
        self.var_table = {}  # variable name to value mapping
        self.func_table = {} # function name to function definition mapping
        self.parent = parent

    def set_var(self, name, value):
        self.var_table[name] = value
    
    def get_var(self, name):
        if name in self.var_table:
            return self.var_table[name]
        else:
            raise RuntimeError(f"Variable '{name}' not declared.")

    def set_func(self, name, func_def):
        self.func_table[name] = func_def
    
    def get_func(self, name):
        if name in self.func_table:
            return self.func_table[name]
        elif self.parent:
            return self.parent.get_func(name)
        else:
            raise  RuntimeError(f"Function '{name}' not declared.")