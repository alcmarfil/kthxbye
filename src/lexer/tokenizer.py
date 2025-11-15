#main lexical analyzer

from lexer.patterns import PATTERNS
import re

#Token class to represent different token types
class Token:
    def __init__(self, type_, value, line=None, column =None):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}, {self.column})"
#tokenizer function
def tokenize(code):
    tokens = []  #list to hold tokens
    position = 0 #position in code (character index)
    line = 1     
    column = 1

    #loop till end of code
    while position < len(code):
        matched = False #flag to check if any pattern matched
        for token_type, pattern in PATTERNS.items(): #check each pattern
            match = pattern.match(code, position) # match based sa current position
            if match: #if pattern matches
                value = match.group(0) #capture matched value
                
                # Strip quotes from YARN_LITERAL
                if token_type == "YARN_LITERAL":
                    value = value[1:-1]  # Remove quotes
                if token_type != "WHITESPACE":  #ignore lang whitespace and comments pero need parin update line/column
                    tokens.append(Token(token_type, value, line, column))
                # print(f"Matched {token_type} with value '{value}' at line {line}, column {column}") #debug print
                lines = value.count('\n') #count new lines kapag may multiple lines
                if lines > 0: #if multiple lines matched
                    line += lines #add yung lines sa line count
                    column = len(value) - value.rfind('\n') #need ma reset column after last new line. rfind("\n") gets index of last newline
                else:
                    column += len(value) #update column based on length of matched value

                position = match.end(0) #move position to end of matched token
                matched = True
                break
        if not matched: # if di matched diretso read next char
            position += 1 
            column += 1
    return tokens

