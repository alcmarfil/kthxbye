from parser.errors import RuntimeError

class Environment:
    def __init__(self):
        self.var_table = {}  # variable name to value mapping
        self.func_table = {} # function name to function definition mapping

    def set_var(self, name, value):
        self.var_table[name] = value
    
    def get_var(self, name):
        if name in self.var_table:
            return self.var_table[name]
        else:
            raise RuntimeError(f"Variable '{name}' not declared.")
