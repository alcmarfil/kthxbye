
# ParseError class to handle parsing errors
class ParseError(Exception):
    def __init__(self, message, token):
        self.message = message
        self.token = token
        # include the token position in the message 
        super().__init__(f"{message} at line {token['line']}, column {token['column']}")

# RuntimeError class to handle runtime/interpreter errors
class RuntimeError(Exception):
    def __init__(self, message, node=None):
        self.message = message
        self.node = node
        if node and 'line' in node and 'column' in node:
            super().__init__(f"{message} at line {node['line']}, column {node['column']}")
        else: 
            super().__init__(message)