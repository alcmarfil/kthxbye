# test_tokenizer.py
from src.lexer.patterns import PATTERNS

# sample tokens 
sample_tokens = [
    "HAI", "KTHXBYE", "I HAS A", "VAR",
    "SUM OF", "4", "AN", "5",
    "VISIBLE", '"HELLO WORLD"',
    "BOTH SAEM", "3", "AN", "3",
    "SMOOSH", '"A"', "AN", '"B"', "MKAY",
    "O RLY?", "YA RLY",
    "MAEK", "YARN", "FAIL", "NUMBR",
    "WTF?", "!", "BTW", "AN",
    "123", "12.34", '"no break allowed"'
]

def classify_token(token):
    for key, pattern in PATTERNS.items():
        if hasattr(pattern, 'match'):
            if pattern.match(token):
                return key
    return "TEXT"  # fallback if nothing matches

# Run tokenizer
for tok in sample_tokens:
    token_type = classify_token(tok)
    print(f"{tok:20} → {token_type}")

