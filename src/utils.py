#file reading/file output

#run this file to see tokens printed out from sample_code.lol hehe
from tokenizer import tokenize

def readSourceFile(file_path):
    with open(file_path, "r") as f:
        return f.read()

def outputTokenstoFile(tokens, output_path):
    with open(output_path, "w") as f:
        for token in tokens:
            f.write(f"{token}\n")
            
code = readSourceFile("sample_code.lol")
tokens = tokenize(code)
outputTokenstoFile(tokens, "tokens_output.txt")
for token in tokens:
    print(token)
print("Length of Tokens: ", len(tokens))


#Write tokens to JSON file containing yung type, value, line, column

# [
#     {
#         "type": "HAI",
#         "value": "HAI",
#         "line": 1,
#         "column": 1
#     },
#     {
#         "type": "IDENTIFIER",
#         "value": "VAR",
#         "line": 2,
#         "column": 5
#     }
# ]