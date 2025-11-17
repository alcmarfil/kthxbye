# runs the tokenizer

import sys
import json
from pathlib import Path

# add src directory to path 
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# imports from lexer folder
from lexer.utils import readSourceFile
from lexer.tokenizer import tokenize

# imports from the parser folder
from parser.parser import Parser

#imports from the semantics folder
from semantics.interpreter import Interpreter
from semantics.environment import Environment

def main():
    import sys
    
    # get paths relative to project root
    project_root = Path(__file__).parent
    src_dir = project_root / "src"
    
    # accept command-line argument for input file, or use default
    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
        if not input_file.is_absolute():
            input_file = project_root / input_file
    else:
        input_file = src_dir / "sample_code2.lol"
    
    if not input_file.exists():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    output_file = src_dir / "tokens_output.json"
    
    # read, tokenize, then write the output to file
    code = readSourceFile(str(input_file))
    tokens = tokenize(code)
    
    # convert tokens to list of dictionaries for JSON 
    tokens_dict = [
        {
            "type": token.type,
            "value": token.value,
            "line": token.line,
            "column": token.column
        }
        for token in tokens
    ]
    
    # write to JSON file
    with open(str(output_file), "w") as f:
        json.dump(tokens_dict, f, indent=4)
        
    print(f"\nTotal tokens: {len(tokens)}")
    print(f"Tokens written to: {output_file}")

    # parser
    parser = Parser(tokens_dict)
    ast = parser.parse()
    ast_output_file = src_dir / "ast_output.json"
    with open(ast_output_file, "w") as f:
        json.dump(ast, f, indent=4)
    
    # interpreter
    env = Environment()
    interpreter = Interpreter()
    if isinstance(ast, dict) and  ast.get("error",False):
        print(ast["message"], file=sys.stderr)
        sys.exit(1)
    else:
        # evaluate declarations
        for dec in ast["wazzup"]["declarations"]:
            interpreter.evaluate(dec, env)

        # evaluate statements
        for stmt in ast["statements"]:
            interpreter.evaluate(stmt, env)

if __name__ == "__main__":
    main()
