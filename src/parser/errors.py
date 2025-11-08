# ParseError and utils

class ParseError(Exception):
    def __init__(self, message, token):
        self.message = message
        self.token = token
        super().__init__(f"{message} at line {token['line']}, column {token['column']}")