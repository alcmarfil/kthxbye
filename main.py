#runs the tokenizer

import sys
import json
from pathlib import Path

# add src directory to path 
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from utils import readSourceFile
from tokenizer import tokenize

def main():
    # get paths relative to project root
    project_root = Path(__file__).parent
    src_dir = project_root / "src"
    
    input_file = src_dir / "sample_code.lol"
    output_file = src_dir / "tokens_output.json"
    
    # read, tokenize, then write the output sa output file
    code = readSourceFile(str(input_file))
    tokens = tokenize(code)
    
    # convert tokens to list of dictionaries for json 
    tokens_dict = [
        {
            "type": token.type,
            "value": token.value,
            "line": token.line,
            "column": token.column
        }
        for token in tokens
    ]
    
    # write to json file
    with open(str(output_file), "w") as f:
        json.dump(tokens_dict, f, indent=4)
    
    #print the tokens 
    print("\n=== Tokenized Output (JSON) ===")
    print(json.dumps(tokens_dict, indent=4))
    
    print(f"\nTotal tokens: {len(tokens)}")
    print(f"\nTokens written to: {output_file}")

if __name__ == "__main__":
    main()