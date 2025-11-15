class Environment:
    def __init__(self):
        self.var_table = {}  # variable name to value mapping

    def set_var(self, name, value):
        self.var_table[name] = value
    
    def get_var(self, name):
        if name in self.var_table:
            return self.var_table[name]
        else:
            Exception(f"Variable '{name}' not declared.")