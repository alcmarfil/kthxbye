#file reading/file output

#run this file to see tokens printed out from sample_code.lol hehe
from tokenizer import tokenize
import json
from pathlib import Path

def readSourceFile(file_path):
    with open(file_path, "r") as f:
        return f.read()

def tokensToDict(tokens):
    """Convert Token objects to a list of dictionaries."""
    return [
        {
            "type": token.type,
            "value": token.value,
            "line": token.line,
            "column": token.column
        }
        for token in tokens
    ]

def outputTokensToJSON(tokens, output_path, tokens_dict=None):
    """Write tokens to a JSON file.
    
    Args:
        tokens: List of Token objects
        output_path: Path to output JSON file
        tokens_dict: Optional pre-converted dictionary (to avoid duplicate conversion)
    """
    if tokens_dict is None:
        tokens_dict = tokensToDict(tokens)
    with open(output_path, "w") as f:
        json.dump(tokens_dict, f, indent=4)

# onnly run this code when utils.py is executed directly not when imported
if __name__ == "__main__":
    # get the script directory and io files
    script_dir = Path(__file__).parent
    input_file = script_dir / "sample_code.lol"
    output_file = script_dir / "tokens_output.json"
    
    code = readSourceFile(str(input_file))
    tokens = tokenize(code)
    
    # Convert tokens to dictionary format (once)
    tokens_dict = tokensToDict(tokens)
    
    # Write tokens to JSON file (pass dict to avoid duplicate conversion)
    outputTokensToJSON(tokens, str(output_file), tokens_dict)
    
    # Print the tokens
    print("\n=== Tokenized Output (JSON) ===")
    print(json.dumps(tokens_dict, indent=4))
    print(f"Length of Tokens: {len(tokens)}")
