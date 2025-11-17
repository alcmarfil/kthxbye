from parser.token_stream import TokenStream
from parser.ast_nodes import create_node
from parser.errors import ParseError

# reserved keywords that cannot be used as variable names
RESERVED_KEYWORDS = {
            "HAI", "KTHXBYE", "I_HAS_A", "ITZ", "VISIBLE", "GIMMEH",
            "R", "IS_NOW_A", "MAEK", "A", "O_RLY", "YA_RLY", "MEBBE",
            "NO_WAI", "OIC", "WTF", "OMG", "OMGWTF", "IM_IN_YR",
            "IM_OUTTA_YR", "UPPIN", "NERFIN", "TIL", "WILE",
            "HOW_IZ_I", "IF_U_SAY_SO", "FOUND_YR", "GTFO", "SMOOSH",
            "BOTH_OF", "EITHER_OF", "WON_OF", "NOT", "ANY_OF", "ALL_OF",
            "BOTH_SAEM", "DIFFRINT", "SUM_OF", "DIFF_OF", "PRODUKT_OF",
            "QUOSHUNT_OF", "MOD_OF", "BIGGR_OF", "SMALLR_OF", "IT"
        }

# Parser class to parse the tokens into an AST
class Parser:
    def __init__(self, tokens):
        self.tokens = TokenStream(tokens)
        self.errors = []

    def parse(self):
        # try to parse the program, if an error occurs, return the error message
        try:
            return self.parse_program()
        except ParseError as e:
            return {
                "error": True,
                "message": e.message,
                "line": e.token["line"],
                "column": e.token["column"]
            }
        
    # <program> ::= [<function_list>] HAI <linebreak> <wazzup_section> <statement_list> <linebreak> KTHXBYE [<function_list>]
    def parse_program(self):
        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()
        # functions can be defined before HAI (per spec)
        pre_program_functions = self.parse_function_list()
        
        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()

        start = self.tokens.current()
        self.tokens.expect("HAI")

        # optional linebreak
        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()

        # prelude: functions after HAI but before WAZZUP
        prelude = self.parse_function_list()

        # wazzup section (optional)
        wazzup = self.parse_wazzup_section()

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()
        # main statements
        statements = self.parse_statement_list()

        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()
        
        # postlude: functions after main statements but before KTHXBYE
        postlude = self.parse_function_list()

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()

        self.tokens.expect("KTHXBYE")

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()

        post_program_functions = self.parse_function_list()

        self.tokens.skip_comments()
        self.tokens.skip_multiple_line_comments()
        # after KTHXBYE and optional functions, program must end
        if not self.tokens.at_end():
            raise ParseError(
                f"Unexpected token '{self.tokens.current()['type']}' after KTHXBYE. Only functions and comments are allowed after KTHXBYE.",
                self.tokens.current()
            )

        # return the program node
        return create_node(
            "Program",
            prelude=pre_program_functions + prelude,  # functions before and after HAI (before WAZZUP)
            wazzup=wazzup,
            statements=statements,
            postlude=postlude + post_program_functions,  # functions after statements and after KTHXBYE
            start_line=start["line"]
        )


    
    def parse_function_list(self):
        functions = []
        while self.tokens.current()["type"] == "HOW_IZ_I": # while the current token is a function definition
            func = self.parse_function_def() # parse the function definition
            functions.append(func) # add the function to the list
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
        return functions

    # <wazzup_section> ::= WAZZUP <linebreak> <declaration_list> <linebreak> BUHBYE | <empty>
    def parse_wazzup_section(self):
        self.tokens.skip_comments()
        if self.tokens.current()["type"] == "WAZZUP":
            self.tokens.advance()

            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
            self.tokens.skip_comments()
            decls = self.parse_declaration_list() # parse the declaration list

            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()

            self.tokens.expect("BUHBYE") 
            return create_node("WazzupSection", declarations=decls)

        return None # if it is empty


    # <declaration_list> ::= <declaration> | <declaration> <linebreak> <declaration_list>
    def parse_declaration_list(self):
        declarations = []
        while not self.tokens.at_end() and self.tokens.current()["type"] != "BUHBYE":
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
                continue
            if self.tokens.current()["type"] == "I_HAS_A":
                decl = self.parse_declaration() # parse the declaration
                declarations.append(decl) # add the declaration to the list
            else:
                raise ParseError(
                    f"Unexpected token '{self.tokens.current()['type']}' in WAZZUP section. Only variable declarations (I HAS A) are allowed.",
                    self.tokens.current()
                )
        return declarations


    # <declaration> ::= I HAS A varident | I HAS A varident ITZ <literal> | I HAS A varident ITZ <expr>
    def parse_declaration(self):
        start = self.tokens.current()
        self.tokens.expect("I_HAS_A")

        # expect variable name
        var_token = self.tokens.expect("IDENTIFIER")
        var_name = var_token["value"]

        # check if the variable name is a reserved keyword
        if var_name in RESERVED_KEYWORDS:
            raise ParseError(f"Cannot use reserved keyword '{var_name}' as variable name", var_token)

        # add variable to symbol table
        self.tokens.symbols.add(var_name)

        init_value = None
        if self.tokens.current()["type"] == "ITZ":
            self.tokens.advance()
            init_value = self.parse_expr()
        else:
            init_value = {
                "node_type": "Literal",
                "value": None,
                "data_type": "NOOB_LITERAL"
            }
        
        self.tokens.skip_comments()

        return create_node("Declaration", name=var_name, value=init_value, line=start["line"])



    # <statement_list> ::= <statement> | <statement> <linebreak> <statement_list>
    def parse_statement_list(self, until_keywords=None):
        statements = []
        if until_keywords is None:
            until_keywords = ["KTHXBYE", "BUHBYE"]

        # while the current token is not a keyword to stop at
        while not self.tokens.at_end():
            # Skip comments before checking until_keywords
            self.tokens.skip_comments()
            self.tokens.skip_multiple_line_comments()
            
            # Check if we've reached a stopping keyword
            if self.tokens.current()["type"] in until_keywords:
                break
                
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
                continue

            stmt = self.parse_statement() # parse the statement\
            statements.append(stmt)

            # optional linebreak after each statement
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()

        return statements



    # <statement> ::= <print> | <declaration> ...
    def parse_statement(self):
        current_type = self.tokens.current()["type"]

        if current_type == "BTW":
            self.tokens.advance()
            return self.parse_statement()
        elif current_type == "MULTI_LINE_COMMENT":
            self.tokens.advance()
            return self.parse_statement()
        elif current_type == "VISIBLE":
            return self.parse_print()
        elif current_type == "I_HAS_A":
            return self.parse_declaration()
        elif current_type == "IDENTIFIER":
            token_value = self.tokens.current()["value"]

            # check for reserved keywords typo
            if token_value in RESERVED_KEYWORDS:
                raise ParseError(f"Unexpected keyword or invalid identifier '{token_value}'", self.tokens.current())

            # check if it's an assignment
            next_token = self.tokens.peek()
            if next_token and next_token["type"] in ["R", "IS_NOW_A"]:
                # check if declared
                if not self.tokens.is_declared(token_value): 
                    raise ParseError(f"Unknown identifier '{token_value}'", self.tokens.current())
                return self.parse_assignment()
                     
            # now parse as an expression
            expr = self.parse_expr()
            line = expr.get("line", expr.get("start_line", self.tokens.current()["line"]))
            
            self.tokens.skip_comments()
            self.tokens.skip_multiple_line_comments()
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
            self.tokens.skip_comments()
            self.tokens.skip_multiple_line_comments()
            
            if self.tokens.current()["type"] == "O_RLY":
                return self.parse_conditional_with_expr(expr, line)
            elif self.tokens.current()["type"] == "WTF":
                return self.parse_switch_with_expr(expr, line)
            else:
                return create_node("ExpressionStatement", expression=expr, line=line)

        elif current_type == "GIMMEH":
            return self.parse_input()
        elif current_type == "O_RLY":
            return self.parse_conditional()
        elif current_type == "WTF":
            return self.parse_switch()
        elif current_type == "IM_IN_YR":
            return self.parse_loop()
        elif current_type == "HOW_IZ_I":
            return self.parse_function_def()
        elif current_type == "I_IZ":
            return self.parse_function_call()
        elif current_type == "FOUND_YR":
            return self.parse_return()
        elif current_type == "GTFO":
            return self.parse_break()
        else:
            # literal expression by itself 
            start = self.tokens.current()
            expr = self.parse_expr()
            
            # Check if expression is followed by O RLY? or WTF? (skip comments and linebreaks)
            self.tokens.skip_comments()
            self.tokens.skip_multiple_line_comments()
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
            self.tokens.skip_comments()
            self.tokens.skip_multiple_line_comments()
            
            # If followed by O_RLY, combine into Conditional
            if self.tokens.current()["type"] == "O_RLY":
                return self.parse_conditional_with_expr(expr, start["line"])
            # If followed by WTF, combine into Switch
            elif self.tokens.current()["type"] == "WTF":
                return self.parse_switch_with_expr(expr, start["line"])
            # Otherwise, return as ExpressionStatement
            else:
                return create_node("ExpressionStatement", expression=expr, line=start["line"])


    # <print> ::= VISIBLE <print_args> <opt_excl>
    def parse_print(self):
        start = self.tokens.expect("VISIBLE")
        args = self.parse_print_args()

        # optional exclamation
        if self.tokens.current()["type"] == "EXCLAMATION":
            self.tokens.advance()
            exclamation = True
        else:
            exclamation = False
        
        self.tokens.skip_comments()

        return create_node("PrintStatement", arguments=args, exclamation=exclamation, line=start["line"])

    # <print_args> ::= <expr> | <expr> AN <print_args>
    def parse_print_args(self):
        args = [self.parse_expr()]
        while self.tokens.current()["type"] == "PLUS" or self.tokens.current()["type"] == "AN" : # while the current token is an AN
            self.tokens.advance()
            args.append(self.parse_expr()) # add the expression to the list
        return args

    def parse_expr(self): # parses an expression
        current = self.tokens.current()
        token_value = current["value"]
        token_type = current["type"]

        literal_types = [
            "NUMBR_LITERAL", "NUMBAR_LITERAL", "YARN_LITERAL",
            "TROOF_LITERAL", "TYPE_LITERAL", "NOOB_LITERAL"
        ]

        # string concatenation
        if token_type == "SMOOSH":
            return self.parse_string_expr()
        
        # comparison expressions
        if token_value in ["BOTH OF", "EITHER OF", "WON OF"]:
            operator = token_value
            self.tokens.advance()
            left = self.parse_expr()
            self.tokens.expect("AN")
            right = self.parse_expr()
            return create_node("BooleanExpression", operator=operator, left=left, right=right)

        if token_value == "NOT":
            operator = token_value
            self.tokens.advance()
            expr = self.parse_expr()
            return create_node("BooleanNotExpression", operator=operator, expr=expr)
        
        if token_value in ["BOTH SAEM", "DIFFRINT"]:
            operator = token_value
            self.tokens.advance()
            left = self.parse_expr()
            self.tokens.expect("AN")
            right = self.parse_expr()
            return create_node("EqualityExpression", operator=operator, left=left, right=right)


        if token_value in ["ANY OF", "ALL OF"]:
            operator = token_value
            self.tokens.advance() # advance to the next token

            # check cannot be ALL OF or ANY OF
            next_token_type = self.tokens.current().get("type", "")
            if next_token_type in ["ALL_OF", "ANY_OF"]:
                raise ParseError("ALL OF and ANY OF cannot be nested into each other or themselves", self.tokens.current())
            
            exprs = [self.parse_expr()] #first expression
            while self.tokens.current()["type"] == "AN": 
                self.tokens.advance()
                next_token_type = self.tokens.current().get("type", "")
                if next_token_type in ["ALL_OF", "ANY_OF"]:
                    raise ParseError("ALL OF and ANY OF cannot be nested into each other or themselves", self.tokens.current())
                exprs.append(self.parse_expr()) 

            self.tokens.expect("MKAY")  # must end with MKAY
            return create_node("BooleanListExpression", operator=operator, expressions=exprs)
    
        # arithmetic expressions
        if token_value in ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF"]:
            operator = token_value
            self.tokens.advance()  # skip operator keyword

            left = self.parse_expr()        
            self.tokens.expect("AN")        
            right = self.parse_expr()        

            return create_node("BinaryExpression", operator=operator, left=left,right=right)

        # literals
        elif token_type in literal_types:
            literal_value = current["value"]
            if token_type == "NUMBR_LITERAL" or token_type == "NUMBAR_LITERAL":
                if literal_value.startswith("+"):
                    raise ParseError(f"Positive sign (+) not allowed in {token_type}. Use number without sign or negative sign (-) for negative numbers.", current)
            elif token_type == "TROOF_LITERAL":
                if literal_value not in ["WIN", "FAIL"]:
                    raise ParseError(f"Invalid TROOF literal: '{literal_value}'. Only WIN or FAIL are allowed.", current)
            self.tokens.advance()
            return create_node("Literal", value=literal_value, data_type=token_type)

        # variable references
        elif token_type == "IDENTIFIER":
            self.tokens.advance()
            return create_node("Variable", name=current["value"])
        
        elif token_type == "MAEK":
            self.tokens.advance()
            return self.parse_type_cast()
        
        elif token_type == "I_IZ":
            return self.parse_function_call()
        
        # if none match
        else:
            raise ParseError(
                "Expected an expression (number, string, variable, arithmetic, boolean, or type cast)",
                current
            )



    # <assignment> ::= varident R <expr> | varident R <type_cast> | varident IS NOW A <type_cast> | <string_assignment>
    def parse_assignment(self):
        start = self.tokens.current()
        var_token = self.tokens.expect("IDENTIFIER")
        var_name = var_token["value"]

        # normal assignment
        if self.tokens.match("R"):
            value = self.parse_expr()
            return create_node("Assignment", target=var_name, value=value, line=start["line"])

        # type change: varident IS NOW A <type>
        elif self.tokens.match("IS_NOW_A"):
            type_token = self.tokens.expect("TYPE_LITERAL")
            return create_node(
                "TypeChange",
                variable=var_name,
                new_type=type_token["value"],
                line=start["line"]
            )

        # other case (string or typecast with IS_NOW_A inside expr)
        else:
            raise ParseError("Invalid assignment syntax", self.tokens.current())


    # <type_cast> ::= MAEK <expr> A <type>
    def parse_type_cast(self):
        expr = self.parse_expr()
        self.tokens.expect("A")
        type_token = self.tokens.expect("TYPE_LITERAL")
        return create_node("TypeCast", expr=expr, type_name=type_token["value"])

    # <input> ::= GIMMEH varident
    def parse_input(self):
        start = self.tokens.expect("GIMMEH")
        var_token = self.tokens.expect("IDENTIFIER")
        return create_node("InputStatement", target=var_token["value"], line=start["line"])
    
    
    def parse_string_expr(self):
    # SMOOSH [ <expr> ( AN <expr> )* ] [ MKAY ]
        self.tokens.expect("SMOOSH")
        exprs = []

        # if next token cannot start an expression, allow empty SMOOSH (empty string)
        if self.tokens.current()["type"] not in [
            "NUMBR_LITERAL", "NUMBAR_LITERAL", "YARN_LITERAL",
            "TROOF_LITERAL", "TYPE_LITERAL", "NOOB_LITERAL",
            "IDENTIFIER", "SMOOSH", "MAEK", "I_IZ",
            "SUM_OF", "DIFF_OF", "PRODUKT_OF", "QUOSHUNT_OF",
            "MOD_OF", "BIGGR_OF", "SMALLR_OF",
            "BOTH_OF", "EITHER_OF", "WON_OF", "NOT",
            "ANY_OF", "ALL_OF", "BOTH_SAEM", "DIFFRINT"
        ]:
            # treat as empty string
            return create_node("StringExpression", expressions=[])

        # first expression (if present)
        exprs.append(self.parse_expr())

        # chain with AN <expr>
        while self.tokens.current()["type"] == "AN":
            self.tokens.advance()
            if self.tokens.current()["type"] in ["LINEBREAK", "KTHXBYE", "BUHBYE", None]:
                raise ParseError("Expected expression after 'AN' in SMOOSH", self.tokens.current())
            exprs.append(self.parse_expr())

        # optional MKAY to close SMOOSH (accept but not required)
        if self.tokens.current()["type"] == "MKAY":
            self.tokens.advance()

        return create_node("StringExpression", expressions=exprs)


    '''
    <conditional> ::= O RLY? <linebreak> <yes_block> <maybe_block> <linebreak> <end_conditional>
    <yes_block>   ::= YA RLY <linebreak> <statement_list>
    <maybe_block> ::= MEBBE <expr> <statement_list> <maybe_block>
                    | NO WAI <linebreak> <statement_list>
                    | <empty>
    <end_conditional> ::= OIC
    '''
    def parse_conditional(self, condition_expr=None):
        start = self.tokens.current()
        self.tokens.expect("O_RLY")
        
        self.tokens.skip_comments()
        
        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()

        self.tokens.expect("YA_RLY")
        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()
        yes_block = self.parse_statement_list(until_keywords=["MEBBE", "NO_WAI", "OIC"])

        # MEBBE / NO WAI block (0 or more MEBBE, optional NO WAI)
        maybe_blocks = []
        else_block = None

        while self.tokens.current()["type"] in ["MEBBE", "NO_WAI"]: # while the current token is a MEBBE or NO WAI
            if self.tokens.current()["type"] == "MEBBE":
                self.tokens.advance()
                condition = self.parse_expr()
                if self.tokens.current()["type"] == "LINEBREAK": #skip linebreak if present
                    self.tokens.advance()
                block = self.parse_statement_list(until_keywords=["MEBBE", "NO_WAI", "OIC"])
                maybe_blocks.append({"condition": condition, "statements": block})
            elif self.tokens.current()["type"] == "NO_WAI":
                self.tokens.advance()
                if self.tokens.current()["type"] == "LINEBREAK":
                    self.tokens.advance()
                else_block = self.parse_statement_list(until_keywords=["OIC"])
                break

        # end conditional
        self.tokens.expect("OIC")

        return create_node("Conditional", condition=condition_expr, yes_block=yes_block,maybe_blocks=maybe_blocks,else_block=else_block,start_line=start["line"])
    
    def parse_conditional_with_expr(self, condition_expr, expr_line):
        """Parse conditional when expression comes before O RLY?"""
        return self.parse_conditional(condition_expr=condition_expr)

    '''
    <switch> ::= WTF? <linebreak> <case_list> <opt_default_case> <linebreak> OIC
    <case_list> ::= <case_clause> | <case_clause> <linebreak> <case_list>
    <case_clause> ::= OMG <literal> <linebreak> <statement_list>
    <opt_default_case> ::= OMGWTF <linebreak> <statement_list> | <empty>
    '''
    def parse_switch(self, switch_value_expr=None):
        start = self.tokens.current()
        self.tokens.expect("WTF")

        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()

       # case list
        cases = []
        while self.tokens.current()["type"] == "OMG":
            self.tokens.advance()
            literal = self.parse_expr()  # usually a literal
            while self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
            statements = self.parse_statement_list(until_keywords=["OMG", "OMGWTF", "OIC"])
            cases.append({"literal": literal, "statements": statements})

            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()

        # optional default
        default_statements = None
        if self.tokens.current()["type"] == "OMGWTF":
            self.tokens.advance()
            if self.tokens.current()["type"] == "LINEBREAK":
                self.tokens.advance()
            default_statements = self.parse_statement_list(until_keywords=["OIC"])

        self.tokens.expect("OIC")

        return create_node("Switch", switch_value=switch_value_expr, cases=cases,default=default_statements,start_line=start["line"])
    
    def parse_switch_with_expr(self, switch_value_expr, expr_line):
        """Parse switch when expression comes before WTF?"""
        return self.parse_switch(switch_value_expr=switch_value_expr)
    
    def parse_increment(self): 
        start = self.tokens.current()
        self.tokens.expect("UPPIN")
        var_token = self.tokens.expect("IDENTIFIER")
        return create_node("Increment", variable=var_token["value"], start_line=start["line"])

    def parse_decrement(self):
        start = self.tokens.current()
        self.tokens.expect("NERFIN")
        var_token = self.tokens.expect("IDENTIFIER")
        return create_node("Decrement", variable=var_token["value"], start_line=start["line"])

    def parse_loop(self): #okay 
        start = self.tokens.current()
        self.tokens.expect("IM_IN_YR")

        # loop variable
        loop_var_token = self.tokens.expect("IDENTIFIER")
        loop_var = loop_var_token["value"]

        # UPPIN or NERFIN
        loop_op_token = self.tokens.current()
        if loop_op_token["type"] in ["UPPIN", "NERFIN"]:
            loop_op = loop_op_token["type"]
            self.tokens.advance()
        else:
            raise ParseError("Expected ['UPPIN', 'NERFIN']", loop_op_token)

        # YR <target_var>
        self.tokens.expect("YR")
        target_var_token = self.tokens.expect("IDENTIFIER")
        target_var = target_var_token["value"]

        # optional loop condition
        loop_condition = None
        if self.tokens.current()["type"] in ["TIL", "WILE"]:
            cond_type = self.tokens.current()["type"]
            self.tokens.advance()
            loop_condition = {"type": cond_type, "expr": self.parse_expr()}

        # optional linebreak
        if self.tokens.current()["type"] == "LINEBREAK":
            self.tokens.advance()

        # parse body
        body = self.parse_statement_list(until_keywords=["IM_OUTTA_YR"])

        # IM OUTTA YR <varident>
        self.tokens.expect("IM_OUTTA_YR")
        out_var_token = self.tokens.expect("IDENTIFIER")
        if out_var_token["value"] != loop_var:
            raise ParseError(f"Loop exit variable must match entry variable {loop_var}", out_var_token)

        return create_node(
            "Loop",
            loop_var=loop_var,
            loop_op=loop_op,
            target_var=target_var,
            condition=loop_condition,
            body=body,
            start_line=start["line"]
        )

    def parse_function_list(self):
        functions = [] 
        while not self.tokens.at_end() and self.tokens.current()["type"] == "HOW_IZ_I":
            func = self.parse_function_def() # parse the function definition
            functions.append(func) # add the function to the list
            if self.tokens.current()["type"] == "LINEBREAK": 
                self.tokens.advance() 
        return functions

    def parse_function_def(self):
        start = self.tokens.current()
        self.tokens.expect("HOW_IZ_I")
        name_token = self.tokens.expect("IDENTIFIER")
        func_name = name_token["value"]

        # optional parameters
        params = []
        if self.tokens.current()["type"] == "YR":
            self.tokens.advance()
            params = self.parse_param_list()

        # function body
        self.inside_function = True
        body = self.parse_statement_list(until_keywords=["IF_U_SAY_SO"])
        self.inside_function = False  # exit function body

        self.tokens.expect("IF_U_SAY_SO")

        return create_node("FunctionDef", name=func_name, params=params, body=body, start_line=start["line"])

  
    def parse_param_list(self):
        params = []
        param_token = self.tokens.expect("IDENTIFIER")
        params.append(param_token["value"])

        while self.tokens.current()["type"] == "AN":
            self.tokens.advance()
            self.tokens.expect("YR")
            param_token = self.tokens.expect("IDENTIFIER")
            params.append(param_token["value"]) # add the parameter to the list
        return params


    def parse_function_call(self):
        start = self.tokens.current()
        self.tokens.expect("I_IZ")

        func_token = self.tokens.expect("IDENTIFIER")
        func_name = func_token["value"]

        args = [] # list of arguments
        if self.tokens.current()["type"] == "YR":
            self.tokens.advance()
            args = self.parse_arg_list() # parse the argument list

        # MKAY is required for function calls 
        self.tokens.expect("MKAY")

        return create_node("FunctionCall", name=func_name, args=args, start_line=start["line"])

    def parse_arg_list(self):
        args = [self.parse_expr()]
        while self.tokens.current()["type"] == "AN":
            self.tokens.advance()
            self.tokens.expect("YR")
            args.append(self.parse_expr())
        return args
    
    def parse_return(self):
        if not getattr(self, "inside_function", False):
            raise ParseError("Return found outside function", self.tokens.current())

        start = self.tokens.current()
        self.tokens.expect("FOUND_YR")
        expr = self.parse_expr()

        self.tokens.skip_comments()
        return create_node("Return", expr=expr, start_line=start["line"])

    def parse_break(self):
        start = self.tokens.current()
        self.tokens.expect("GTFO")
        
        # GTFO in function context returns NOOB (no value)
        if getattr(self, "inside_function", False):
            noob_literal = create_node("Literal", value="NOOB", data_type="NOOB_LITERAL")
            return create_node("Return", expr=noob_literal, start_line=start["line"])
        
        # GTFO outside function is a break statement (for loops)
        return create_node("Break", start_line=start["line"])

