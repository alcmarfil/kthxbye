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

def _get_line_number(code, position):
    return code[:position].count('\n') + 1

def _get_line_start(code, position):
    line_start = code.rfind('\n', 0, position)
    return line_start + 1 if line_start != -1 else 0

def _get_line_end(code, position):
    line_end = code.find('\n', position)
    return line_end if line_end != -1 else len(code)

def _validate_multiline_comment(code, match, comment_value):
    match_start = match.start() # get the start position of the match 
    
    keywords = [
        ("OBTW", True),  # OBTW must have nothing before it
        ("TLDR", False)   # TLDR must have nothing after it
    ]
    
    for keyword, check_before in keywords: # check kada keyword
        keyword_pos = comment_value.find(keyword) # find the position of the keyword in the comment value
        if keyword_pos == -1: # if the keyword is not found, continue
            continue
            
        keyword_abs_pos = match_start + keyword_pos #get the absolute position of the keyword
        # para to validate if the keyword is on its own line
        
        if check_before:
            # check if nothing appears before OBTW on the same line
            line_start = _get_line_start(code, keyword_abs_pos) 
            line_content = code[line_start:keyword_abs_pos] 
            if line_content.strip(): # if meron laman, mag raise ng error
                line_num = _get_line_number(code, keyword_abs_pos)
                raise ValueError(
                    f"Multiline comment '{keyword}' must be on its own line (line {line_num}). "
                    f"It cannot appear inline with other code."
                )
        else:
            # check if nothing appears after TLDR on the same line
            keyword_end_pos = keyword_abs_pos + len(keyword)
            line_end = _get_line_end(code, keyword_end_pos)
            line_content = code[keyword_end_pos:line_end]
            if line_content.strip(): #check if there is anything after tldr
                line_num = _get_line_number(code, keyword_end_pos) #get the lin number 
                raise ValueError(
                    f"Multiline comment '{keyword}' must be on its own line (line {line_num}). "
                    f"It cannot appear inline with other code."
                )

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
                
                # validate multiline comments: OBTW and TLDR must be on their own lines
                if token_type == "MULTI_LINE_COMMENT":
                    _validate_multiline_comment(code, match, value)
                
                # strip quotes from YARN_LITERAL
                if token_type == "YARN_LITERAL":
                    value = value[1:-1]  # Remove quotes
                if token_type != "WHITESPACE":  #ignore lang whitespace and comments pero need parin update line/column
                    tokens.append(Token(token_type, value, line, column))
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
            # Check for positive sign followed by digits (not allowed in LOLCODE)
            if position < len(code) and code[position] == '+':
                if position + 1 < len(code) and code[position + 1].isdigit():
                    raise ValueError(f"Positive sign (+) not allowed before numbers at line {line}, column {column}. Use number without sign or negative sign (-) for negative numbers.")
            position += 1 
            column += 1
    return tokens

