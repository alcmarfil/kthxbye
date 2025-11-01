#file reading/file output

#run this file to see tokens printed out from sample_code.lol hehe
from tokenizer import tokenize

def readSourceFile(file_path):
    with open(file_path, "r") as f:
        return f.read()

code = readSourceFile("sample_code.lol")
tokens = tokenize(code)

for token in tokens:
    print(token)


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