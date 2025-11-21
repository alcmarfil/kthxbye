
from semantics.environment import Environment
from parser.errors import RuntimeError
from parser.errors import ReturnValue

# Exception for breaking out of loops
class BreakException(Exception):
    pass

class Interpreter:
    #evaluator (dynamic)
    def evaluate(self, node, env):
        node_type = node.get('node_type')
        if node_type is None:
            raise RuntimeError("AST node missing 'node_type' field", node)
        method_name = f'eval_{node_type.lower()}'
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(node,env)
        else:
            raise RuntimeError(f"No eval method for node type: {node_type}", node)

    #declaration statemetns
    def eval_declaration(self, node, env):
        var_name = node.get('name')
        if var_name is None:
            raise RuntimeError("Declaration missing variable name", node)
        if node.get('value') is not None:
            initial_value = self.evaluate(node['value'], env)
        else:
            initial_value = None

        env.set_var(var_name, initial_value)
    
    # assignment statements
    def eval_assignment(self, node, env):
        var_name = node.get('target')
        value_node = node.get('value')
        if var_name is None:
            raise RuntimeError("Assignment missing target variable", node)
        if value_node is None:
            raise RuntimeError("Assignment missing value expression", node)
        value = self.evaluate(value_node, env)
        env.set_var(var_name, value)
        # Update IT variable with the assigned value
        env.set_var("IT", value)
        return value

    #literals
    def eval_literal(self, node, env):
        data_type = node.get("data_type")
        value = node.get("value")
        if data_type is None:
            raise RuntimeError("Literal missing data_type", node)
        
        if data_type == "NUMBR_LITERAL":
            return int(value)
        elif data_type == "NUMBAR_LITERAL":
            return float(value)
        elif data_type == "YARN_LITERAL":
            return value
        elif data_type == "TROOF_LITERAL":
            if value == "WIN":
                return True
            elif value == "FAIL":
                return False
            else:
                raise RuntimeError(f"Invalid troof literal: {value}", node)
        elif data_type == "NOOB_LITERAL":
            return None
        else:
            raise RuntimeError(f"Unknown literal type: {data_type}", node)
    
    # variables
    def eval_variable(self, node, env):
        var_name = node.get('name')
        if var_name is None:
            raise RuntimeError("Variable node missing name", node)
        return env.get_var(var_name)
    
    #print statements
    def eval_printstatement(self, node, env):
        arguments = node.get('arguments', [])
        if not isinstance(arguments, list):
            raise RuntimeError("VISIBLE statement must have a list of arguments", node)
        
        output_parts = []
        for arg in arguments:
            value = self.evaluate(arg, env)
            # cast to yarn (string)
            if isinstance(value, str):
                yarn_value = value
            elif isinstance(value, bool):
                yarn_value = "WIN" if value else "FAIL"
            elif isinstance(value, int):
                yarn_value = str(value)
            elif isinstance(value, float):
                yarn_value = str(value)
            elif value is None:
                yarn_value = ""
            else:
                yarn_value = str(value)
            output_parts.append(yarn_value)
        
        # Join with '+' separator and print
        output = "".join(output_parts)
        print(output, end="")
        
        # only print newline if exclamation mark is not present
        exclamation = node.get('exclamation', False)
        if not exclamation:
            print()  # new line after printing all arguments
            
    # helper method to cast value to numeric type (NUMBR or NUMBAR)
    def cast_to_numeric(self, value, node=None):
        if isinstance(value, int):
            return value, False  # NUMBR
        if isinstance(value, float):
            return value, True  # NUMBAR
        
        # try to cast to numeric if ndi 
        try:
            if isinstance(value, str):
                if self.is_valid_numeric_yarn(value):
                    if '.' in value:
                        return float(value), True  # NUMBAR
                    else:
                        return int(float(value)), False  # NUMBR
                else:
                    raise RuntimeError(f"Cannot cast YARN '{value}' to numeric type for arithmetic operation", node)
            
            elif isinstance(value, bool):
                return (1 if value else 0), False  # NUMBR
            
            elif value is None:
                return 0, False  # NUMBR (NOOB -> 0) kc need daw itypecast lahat ng ndi numbr or numbar
            
            else:
                raise RuntimeError(f"Cannot cast {type(value).__name__} to numeric type for arithmetic operation", node)
        
        except (ValueError, TypeError) as e:
            raise RuntimeError(f"Cannot cast value to numeric type for arithmetic operation: {e}", node)
    
    #arithmetic ops
    def eval_binaryexpression(self, node, env):
        op = node.get("operator")
        left_raw = self.evaluate(node.get("left"), env)
        right_raw = self.evaluate(node.get("right"), env)
        
        # cast operands to numeric types
        left, left_is_float = self.cast_to_numeric(left_raw, node)
        right, right_is_float = self.cast_to_numeric(right_raw, node)
        
        # determine result type (NUMBAR if at least one operand is NUMBAR, else NUMBR)
        result_is_float = left_is_float or right_is_float
        
        # perform operation
        if op == "SUM OF":
            result = left + right
        elif op == "DIFF OF":
            result = left - right
        elif op == "PRODUKT OF":
            result = left * right
        elif op == "QUOSHUNT OF":
            if right == 0:
                raise RuntimeError("Division by zero", node)
            if not result_is_float:
                result = left // right  # integer division for NUMBR
            else:
                result = left / right  # float division for NUMBAR
        elif op == "MOD OF":
            if right == 0:
                raise RuntimeError("Modulo by zero", node)
            result = left % right
        elif op == "BIGGR OF":
            result = max(left, right)
        elif op == "SMALLR OF":
            result = min(left, right)
        else:
            raise RuntimeError(f"Unknown binary operator: {op}", node)
        
        # return appropriate type
        if result_is_float:
            return float(result)  # NUMBAR
        else:
            return int(result)  # NUMBR

    #concatenation
    def eval_expressionstatement(self, node, env):
        expr = node.get("expression")
        if expr is None:
            raise RuntimeError("ExpressionStatement missing expression", node)
        result = self.evaluate(expr, env)
        # implicit variable for last expression 
        env.set_var("IT", result) #this is needed for conditionals and loops
        return result
    
    def eval_stringexpression(self, node, env):
        expressions = node.get("expressions", [])
        if not isinstance(expressions, list):
            raise RuntimeError("SMOOSH expression must have a list of expressions", node)
        string = ""
        for expr in expressions:
            value = self.evaluate(expr, env)
            # implicitly typecast to YARN 
            if isinstance(value, str):
                pass
            elif isinstance(value, bool):
                value = "WIN" if value else "FAIL"
            elif isinstance(value, int):
                value = str(value)
            elif isinstance(value, float):
                value = str(value)
            elif value is None:
                value = ""
            else:
                # fallback: convert to string
                value = str(value)
            string = string + value
        return string
    
    #boolean ops
    #typecast to troof
    def typecast_troof(self, value):
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return len(value) > 0
        if isinstance(value, int):
            return value !=0
        if isinstance(value, float):
            return value != 0
        return False
        
    #evaluate boolean expressions
    def eval_booleanexpression(self, node, env):
        op = node.get("operator")
        left = self.evaluate(node.get("left"), env)
        right = self.evaluate(node.get("right"), env)

        left = self.typecast_troof(left)
        right = self.typecast_troof(right)

        if op == "BOTH OF":
            return left and right
        elif op == "EITHER OF":
            return left or right
        elif op == "WON OF":
            return left ^ right
        else:
            raise RuntimeError(f"Unknown boolean operator: {op}", node)

    # evaluate NOT
    def eval_booleannotexpression(self, node, env):
        expr = self.evaluate(node.get("expr"), env)
        expr = self.typecast_troof(expr)
        return not(expr)

    #eval ALL OF or ANY OF 
    def eval_booleanlistexpression(self, node, env):
        op = node.get("operator")
        expressions = node.get("expressions", [])
        
        if not isinstance(expressions, list):
            raise RuntimeError("Boolean list expression must have a list of expressions", node)

        list_expr = []
        for expr in expressions:
            value = self.evaluate(expr, env)
            value = self.typecast_troof(value)
            list_expr.append(value)
        if op == "ALL OF":
            return all(list_expr)
        elif op == "ANY OF":
            return any(list_expr)
        else:
            raise RuntimeError(f"Unknown boolean list operator: {op}", node)
    
    #equality expressions
    def eval_equalityexpression(self, node, env):
        op = node.get("operator")
        left = self.evaluate(node.get("left"), env)
        right = self.evaluate(node.get("right"), env)

        if isinstance(left, int) and isinstance(right, int):
            if op == "BOTH SAEM":
                return left == right
            elif op == "DIFFRINT":
                return left != right
        elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
            # convert numbr to numbar for comparison
            left_float = float(left) if isinstance(left, int) else left
            right_float = float(right) if isinstance(right, int) else right
            if op == "BOTH SAEM":
                return left_float == right_float
            elif op == "DIFFRINT":
                return left_float != right_float
        else:
            if op == "BOTH SAEM":
                return left == right
            elif op == "DIFFRINT":
                return left != right
        
        raise RuntimeError(f"Unknown equality operator: {op}", node)

    # validate YARN for numeric conversion
    def is_valid_numeric_yarn(self, yarn):
        import re
        return bool(re.match(r'^-?[0-9]+\.?[0-9]*$', yarn))
    
    # core typecasting logic 
    def cast_value(self, value, target_type, node=None):
        # handle NOOB (None)
        if value is None:
            cast_map = {
                "NUMBR": 0,
                "NUMBAR": 0.0,
                "YARN": "",
                "TROOF": False,
                "NOOB": None
            }
            if target_type in cast_map:
                return cast_map[target_type]
        
        # handle TROOF 
        elif isinstance(value, bool):
            cast_map = {
                "NUMBR": 1 if value else 0,
                "NUMBAR": 1.0 if value else 0.0,
                "YARN": "WIN" if value else "FAIL",
                "TROOF": value,
                "NOOB": None
            }
            if target_type in cast_map:
                return cast_map[target_type]
        
        # handle NUMBAR 
        elif isinstance(value, float):
            cast_map = {
                "NUMBR": int(value),  # truncates decimal
                "NUMBAR": value,
                "YARN": f"{value:.2f}",  # two decimal places
                "TROOF": value != 0.0,
                "NOOB": None
            }
            if target_type in cast_map:
                return cast_map[target_type]
        
        # handle NUMBR (int)
        elif isinstance(value, int):
            cast_map = {
                "NUMBR": value,
                "NUMBAR": float(value), 
                "YARN": str(value),
                "TROOF": value != 0,
                "NOOB": None
            }
            if target_type in cast_map:
                return cast_map[target_type]
        
        # handle YARN (str)
        elif isinstance(value, str):
            if target_type == "NUMBR":
                if self.is_valid_numeric_yarn(value):
                    return int(float(value)) 
                else:
                    error_msg = f"Cannot cast YARN '{value}' to NUMBR: contains invalid characters"
                    raise RuntimeError(error_msg, node) if node else RuntimeError(error_msg)
            elif target_type == "NUMBAR":
                if self.is_valid_numeric_yarn(value):
                    return float(value)
                else:
                    error_msg = f"Cannot cast YARN '{value}' to NUMBAR: contains invalid characters"
                    raise RuntimeError(error_msg, node) if node else RuntimeError(error_msg)
            elif target_type == "YARN":
                return value
            elif target_type == "TROOF":
                return value != "" and value != "0" 
            elif target_type == "NOOB":
                return None
        
        # unknown value type or target type
        error_msg = f"Unknown value type for typecasting: {type(value).__name__}"
        raise RuntimeError(error_msg, node) if node else RuntimeError(error_msg)
    
    #typecasting 
    def eval_typecast(self, node, env):
        expr = node.get("expr")
        type_name = node.get("type_name")
        if expr is None:
            raise RuntimeError("TypeCast missing expression", node)
        if type_name is None:
            raise RuntimeError("TypeCast missing target type", node)
        value = self.evaluate(expr, env)
        return self.cast_value(value, type_name, node)
    
    #typechange statements 
    def eval_typechange(self, node, env):
        var_name = node.get("variable")
        new_type = node.get("new_type")
        
        if var_name is None:
            raise RuntimeError("TypeChange missing variable name", node)
        if new_type is None:
            raise RuntimeError("TypeChange missing target type", node)
    
        # get the current value from the environment 
        current_value = env.get_var(var_name)
        converted_value = self.cast_value(current_value, new_type, node)
        
        env.set_var(var_name, converted_value) # update the variable in the environment
        return converted_value

    #conditionals 
    def eval_conditional(self, node, env):
        condition_expr = node.get("condition")
        yes_block = node.get("yes_block")
        maybe_blocks = node.get("maybe_blocks", [])
        else_block = node.get("else_block")
        
        # validate required fields
        if yes_block is None:
            raise RuntimeError("Conditional statement must have YA RLY block", node)
        
        if not isinstance(yes_block, list):
            raise RuntimeError("YA RLY block must have statements", node)
        
        # evaluate the condition expression before O RLY and store in IT
        condition_result = None
        if condition_expr:
            condition_result = self.evaluate(condition_expr, env)
            env.set_var("IT", condition_result)
            # check if IT can be cast to true/false
            condition_result = self.typecast_troof(condition_result)
        else:
            # if no condition, check IT variable
            if "IT" in env.var_table: 
                condition_result = self.typecast_troof(env.get_var("IT"))
            else:
                condition_result = True
        
        if condition_result:
            for statement in yes_block:
                self.evaluate(statement, env)
            return None
        
        # check MEBBE blocks (optional)
        for maybe_block in maybe_blocks:
            if not isinstance(maybe_block, dict):
                raise RuntimeError("MEBBE block must have 'condition' and 'statements'", node)
            if "condition" not in maybe_block:
                raise RuntimeError("MEBBE block must have 'condition'", node)
            if "statements" not in maybe_block:
                raise RuntimeError("MEBBE block must have 'statements'", node)
            
            if self.evaluate(maybe_block["condition"], env):
                for statement in maybe_block["statements"]:
                    self.evaluate(statement, env)
                return None
        
        # execute else block 
        if else_block:
            if not isinstance(else_block, list):
                raise RuntimeError("NO WAI block must be a list of statements", node)
            for statement in else_block:
                self.evaluate(statement, env)
        
        return None
    
    #switch statements
    def eval_switch(self, node, env):
        switch_value_expr = node.get("switch_value") #can also be from GIMMEH
        cases = node.get("cases", [])
        default = node.get("default")
        
        # validate cases structure
        if not isinstance(cases, list):
            raise RuntimeError("Switch cases must be a list", node)
        
        # evaluate the switch value expression before WTF? and store in IT
        switch_value = None
        if switch_value_expr:
            switch_value = self.evaluate(switch_value_expr, env)
            env.set_var("IT", switch_value)
        else:
            # if no expression, use IT variable
            if "IT" in env.var_table:
                switch_value = env.get_var("IT")
            else:
                raise RuntimeError("Switch statement missing switch value expression and IT variable not set", node)
        
        # compare IT with each case 
        matched = False
        for case in cases:
            # for validtation
            if not isinstance(case, dict):
                raise RuntimeError("Switch case must have 'literal' and 'statements'", node)
            if "literal" not in case:
                raise RuntimeError("Switch case must have 'literal'", node)
            if "statements" not in case:
                raise RuntimeError("Switch case must have 'statements'", node)
            
            case_literal = self.evaluate(case["literal"], env)
            if switch_value == case_literal:
                matched = True
                # execute matching case statements
                try:
                    if not isinstance(case["statements"], list):
                        raise RuntimeError("Switch case statements must be a list", node)
                    for statement in case["statements"]:
                        self.evaluate(statement, env)
                except BreakException:
                    pass #break out of switch
                break  # exit switch after matching case
        
        # execute default case (OMGWTF) pag walang case na match
        if not matched and default:
            if not isinstance(default, list):
                raise RuntimeError("Switch default case must be a list of statements", node)
            for statement in default:
                self.evaluate(statement, env)
        
        return None 
    
    #loops 
    def eval_loop(self, node, env):
        loop_var = node.get("loop_var")
        loop_op = node.get("loop_op")
        target_var = node.get("target_var")
        condition = node.get("condition") 
        body = node.get("body")
        
        # validate required fields
        if loop_var is None:
            raise RuntimeError("Loop missing loop variable", node)
        if loop_op is None:
            raise RuntimeError("Loop missing loop operation (UPPIN/NERFIN)", node)
        if target_var is None:
            raise RuntimeError("Loop missing target variable", node)
        if body is None:
            raise RuntimeError("Loop missing body statements", node)
        if not isinstance(body, list):
            raise RuntimeError("Loop body must be a list of statements", node)
        
        env.get_var(target_var)  # check if variable exists before loop
        
        while True:
            if condition:
                if not isinstance(condition, dict):
                    raise RuntimeError("Loop condition must be a dictionary with 'type' and 'expr'", node)
                if "type" not in condition:
                    raise RuntimeError("Loop condition missing 'type' field", node)
                if "expr" not in condition:
                    raise RuntimeError("Loop condition missing 'expr' field", node)
                
                cond_type = condition["type"]  # "TIL" or "WILE"
                cond_expr = condition["expr"]
                cond_result = self.evaluate(cond_expr, env)
                cond_result = self.typecast_troof(cond_result)

                if cond_type == "TIL":
                    if cond_result: 
                        break
                elif cond_type == "WILE":
                    if not cond_result: 
                        break
                else:
                    raise RuntimeError(f"Unknown loop condition type: {cond_type}", node)
            
            # evaluate body
            try:
                for statement in body:
                    self.evaluate(statement, env)
            except BreakException:
                break  # break out of loop
            
            # update target variable 
            if loop_op == "UPPIN": # increment
                current_val = env.get_var(target_var)
                if not isinstance(current_val, (int, float)): # check if var is numeric
                    raise RuntimeError(f"Cannot increment non-numeric variable '{target_var}'", node)
                env.set_var(target_var, current_val + 1)
           
            elif loop_op == "NERFIN": # decrement
                current_val = env.get_var(target_var)
                if not isinstance(current_val, (int, float)):
                    raise RuntimeError(f"Cannot decrement non-numeric variable '{target_var}'", node)
                env.set_var(target_var, current_val - 1)
            
            else:
                raise RuntimeError(f"Unknown loop operator: {loop_op}", node)
            
            if condition is None:
                break
        
        return None

    #break statement 
    def eval_break(self, node, env):
        raise BreakException() #di ko alam if ok na to
        
    def eval_inputstatement(self, node, env):
        var = node.get("target")

        input_value = input()

        value = env.get_var(var)
        env.set_var(var, input_value)
        env.set_var("IT", input_value)
        return input_value

    def eval_functiondef(self, node, env):

        func_def = {
            "params": node.get("params"),
            "body":node.get("body"),
            "parent_env": env
        }
        env.set_func(node.get("name"), func_def)
    
    def eval_functioncall(self, node, env):
        func = env.get_func(node.get("name"))

        params = func.get("params")
        args = node.get("args")

        if len(params) != len(args):
            raise RuntimeError("Argument does not match function parameters count")
        

        local_env = Environment(parent=func.get("parent_env"))

        for param_name, arg in zip(params, args):
            local_env.set_var(param_name, self.evaluate(arg, env))

        
        try:
            for line in func.get("body"):
                self.evaluate(line, local_env)

        except ReturnValue as ret_value:
            env.set_var("IT", ret_value)
            return ret_value.value
    
        return None


    def eval_return(self, node, env):
        ret_value = self.evaluate(node.get("expr"), env)
        env.set_var("IT", ret_value)
        raise ReturnValue(ret_value)



