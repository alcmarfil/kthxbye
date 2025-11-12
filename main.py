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

def main():
    # get paths relative to project root
    project_root = Path(__file__).parent
    src_dir = project_root / "src"
    
    input_file = src_dir / "sample_code.lol"
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
    
    # print tokens to console
    # print("\n=== Tokenized Output (JSON) ===")
    # print(json.dumps(tokens_dict, indent=4))
    
    print(f"\nTotal tokens: {len(tokens)}")
    print(f"Tokens written to: {output_file}")

    # parser
    parser = Parser(tokens_dict)
    ast = parser.parse()
    ast_output_file = src_dir / "ast_output.json"
    with open(ast_output_file, "w") as f:
        print(f"Writing AST to: {ast_output_file.resolve()}")
        json.dump(ast, f, indent=4)

if __name__ == "__main__":
    main()
