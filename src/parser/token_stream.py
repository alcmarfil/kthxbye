# helper for iterating tokens

from parser.errors import ParseError

# TokenStream class to iterate through tokens
class TokenStream:
    def __init__(self, tokens):
        self.tokens = tokens # list of tokens
        self.symbols = set() # set of declared variables
        self.position = 0 # current position in the token list

    def current(self):
        # return the current token (or a dummy EOF token if past end)
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return {"type": "EOF", "value": None, "line": -1, "column": -1}
    
    def peek(self, offset=1):
        # look ahead without consuming
        index = self.position + offset # index of the token to look ahead 
        if index < len(self.tokens): # if index is within the list
            return self.tokens[index]
        return None

    def advance(self):
        # move to the next token
        if self.position < len(self.tokens):
            self.position += 1 # increment position

    def expect(self, expected_type):
        # consume and return a token of expected type, or raise error
        token = self.current() 
        if token["type"] != expected_type:
            raise ParseError(f"Expected {expected_type}, got {token['type']}", token)
        self.advance()
        return token

    def match(self, expected_type):
        # if current token matches, consume it and return True
        if self.current()["type"] == expected_type: # if current token matches expected type
            self.advance()
            return True
        return False

    def at_end(self):
        # true if at or past end of token list
        return self.position >= len(self.tokens)

    def skip_comments(self):
        # skip over any comment tokens (BTW, MULTI_LINE_COMMENT)
        while not self.at_end() and self.current()["type"] in ["BTW"]:
            self.advance()
    def skip_multiple_line_comments(self):
        # skip over any multi-line comment tokens (MULTI_LINE_COMMENT)
        while not self.at_end() and self.current()["type"] in ["MULTI_LINE_COMMENT"]:
            self.advance()

    def is_declared(self, name):
        # true if variable is declared
        return name in self.symbols

    

