
from semantics.environment import Environment

class Interpreter:
    #evaluator (dynamic)
    def evaluate(self, node, env):
        node_type = node['node_type']
        method_name = f'eval_{node_type.lower()}'
        # print(method_name)
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(node,env)
        else:
            raise Exception(f"No eval method for node type: {node_type}")

    #declaration statemetns
    def eval_declaration(self, node, env):
        var_name = node['name']
        if node['value'] is not None:
            initial_value = self.evaluate(node['value'], env)
        else:
            initial_value = None

        env.set_var(var_name, initial_value)
    
    # assignment statements
    def eval_assignment(self, node, env):
        var_name = node['target']
        value = self.evaluate(node['value'],env)
        env.set_var(var_name, value)
        return value

    #literals
    def eval_literal(self, node, env):
        if node["data_type"] == "NUMBR_LITERAL":
            return int(node["value"])
        elif node["data_type"] == "NUMBAR_LITERAL":
            return float(node["value"])
        elif node["data_type"] == "YARN_LITERAL":
            return node["value"]
        elif node["data_type"] == "TROOF_LITERAL":
            if node["value"] == "WIN":
                return True
            elif node["value"] == "FAIL":
                return False
            else:
                raise Exception(f"Invalid troof literal: {node['value']}")
        elif node["data_type"] == "NOOB_LITERAL":
            return None
        else:
                raise Exception(f"Unknown literal type: {node['data_type']}")
    
    # variables
    def eval_variable(self, node, env):
            var_name = node['name']
            if var_name not in env.var_table:
                raise Exception(f"Variable '{var_name}' not declared.")
            return env.get_var(var_name)
    
    #print statements
    def eval_printstatement(self, node, env):
            for arg in node['arguments']:
                value = self.evaluate(arg, env)
                print(value, end="")
            print()  # new line after printing all arguments
            
    #arithmetic ops
    def eval_binaryexpression(self, node, env):
        op = node["operator"]
        left = self.evaluate(node["left"],env)
        right = self.evaluate(node["right"], env)

        if (op == "SUM OF"):
            return left + right
        elif (op == "DIFF OF"):
            return left - right
        elif (op == "PRODUKT OF"):
            return left * right
        elif (op == "QUOSHUNT OF"):
            return float(left/right)
        elif (op == "MOD OF"):
            return left % right
        elif (op == "BIGGR OF"):
            return max(left, right)
        elif (op == "SMALLR OF"):
            return min(left, right)

    #concatenation
    def eval_expressionstatement(self, node, env):
        expr = node["expression"]
        return self.evaluate(expr, env)
    
    def eval_stringexpression(self, node, env):
        string = ""
        for expr in node["expressions"]:
            value = self.evaluate(expr, env)
            # print(value)
            if not isinstance(value, str):
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
        op = node["operator"]
        left = self.evaluate(node["left"],env)
        right = self.evaluate(node["right"], env)

        left = self.typecast_troof(left)
        right = self.typecast_troof(right)

        if op == "BOTH OF":
            return left and right
        elif op == "EITHER OF":
            return left or right
        elif op == "WON OF":
            return left ^ right

    # evaluate NOT
    def eval_booleannotexpression(self, node, env):
        op = node["operator"]
        expr = self.evaluate(node["expr"], env)
        expr = self.typecast_troof(expr)
        return not(expr)

    #eval ALL OF or ANY OF 
    def eval_booleanlistexpression(self, node, env):
        op = node["operator"]
        expressions = node["expressions"]

        list_expr = []
        for expr in expressions:
            value = self.evaluate(expr, env)
            value = self.typecast_troof(value)
            list_expr.append(value)
        if op == "ALL OF":
            return all(list_expr)
        elif op == "ANY OF":
            return any(list_expr)
    #equalit expressions
    def eval_equalityexpression(self, node, env):
        op = node["operator"]
        left = self.evaluate(node["left"],env)
        right = self.evaluate(node["right"],env)

        if op == "BOTH SAEM":
            return left == right
        elif op == "DIFFRINT":
            return left != right
