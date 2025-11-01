# regex patterns

import re

PATTERNS = {
    # KEYWORDS
    # Core structure
    "HAI": re.compile(r"\bHAI\b"),
    "KTHXBYE": re.compile(r"\bKTHXBYE\b"),

    # Comments
    "BTW": re.compile(r"\bBTW.*\b"),
    "MULTI_LINE_COMMENT": re.compile(r"\bOBTW\b(.*?)\bTLDR\b", re.DOTALL),

    # Variable declaration
    "I_HAS_A": re.compile(r"\bI HAS A\b"),
    "ITZ": re.compile(r"\bITZ\b"),
    "R": re.compile(r"\bR\b"),

    # Arithmetic
    "SUM_OF": re.compile(r"\bSUM OF\b"),
    "DIFF_OF": re.compile(r"\bDIFF OF\b"),
    "PRODUKT_OF": re.compile(r"\bPRODUKT OF\b"),
    "QUOSHUNT_OF": re.compile(r"\bQUOSHUNT OF\b"),
    "MOD_OF": re.compile(r"\bMOD OF\b"),
    "BIGGR_OF": re.compile(r"\bBIGGR OF\b"),
    "SMALLR_OF": re.compile(r"\bSMALLR OF\b"),

    # Boolean
    "BOTH_OF": re.compile(r"\bBOTH OF\b"),
    "EITHER_OF": re.compile(r"\bEITHER OF\b"),
    "WON_OF": re.compile(r"\bWON OF\b"),
    "NOT": re.compile(r"\bNOT\b"),
    "ANY_OF": re.compile(r"\bANY OF\b"),
    "ALL_OF": re.compile(r"\bALL OF\b"),

    # Comparison
    "BOTH_SAEM": re.compile(r"\bBOTH SAEM\b"),
    "DIFFRINT": re.compile(r"\bDIFFRINT\b"),

    # String concatenation
    "SMOOSH": re.compile(r"\bSMOOSH\b"),

    # Typecasting 
    "MAEK": re.compile(r"\bMAEK\b"),
    "A": re.compile(r"\bA\b"),
    "IS_NOW_A": re.compile(r"\bIS NOW A\b"),

    # I/O
    "VISIBLE": re.compile(r"\bVISIBLE\b"),
    "GIMMEH": re.compile(r"\bGIMMEH\b"),

    # Switch/Case
    "WTF": re.compile(r"\bWTF\?\b"),
    "OMG": re.compile(r"\bOMG\b"),
    "OMGWTF": re.compile(r"\bOMGWTF\b"),

    # Conditionals
    "O_RLY": re.compile(r"\bO RLY\?\b"),
    "YA_RLY": re.compile(r"\bYA RLY\b"),
    "MEBBE": re.compile(r"\bMEBBE\b"),
    "NO_WAI": re.compile(r"\bNO WAI\b"),
    "OIC": re.compile(r"\bOIC\b"),

    # Loops
    "IM_IN_YR": re.compile(r"\bIM IN YR\b"),
    "UPPIN": re.compile(r"\bUPPIN\b"),
    "NERFIN": re.compile(r"\bNERFIN\b"),
    "YR": re.compile(r"\bYR\b"),
    "TIL": re.compile(r"\bTIL\b"),
    "WILE": re.compile(r"\bWILE\b"),
    "IM_OUTTA_YR": re.compile(r"\bIM OUTTA YR\b"),

    # Functions
    "HOW_IZ_I": re.compile(r"\bHOW IZ I\b"),
    "IF_U_SAY_SO": re.compile(r"\bIF U SAY SO\b"),
    "GTFO": re.compile(r"\bGTFO\b"),
    "FOUND_YR": re.compile(r"\bFOUND YR\b"),
    "I_IZ": re.compile(r"\bI IZ\b"),
    "MKAY": re.compile(r"\bMKAY\b"),

    # Others
    "WAZZUP": re.compile(r"\bWAZZUP\b"),
    "BUHBYE": re.compile(r"\bBUHBYE\b"),

    # CONNECTOR
    "AN": re.compile(r"\bAN\b"),      

    # LITERALS (should still match the entire token)
    "NUMBR_LITERAL": re.compile(r"-?[0-9]+"),
    "NUMBAR_LITERAL": re.compile(r"-?[0-9]+\.[0-9]+"),
    "YARN_LITERAL": re.compile(r'"[^"\n]*"'),
    "TROOF_LITERAL": re.compile(r"(WIN|FAIL)"),
    "TYPE_LITERAL": re.compile(r"(NUMBR|NUMBAR|YARN|TROOF|NOOB|TYPE)"),        

    # IDENTIFIERS (entire token match)
    "IDENTIFIER": re.compile(r"[A-Za-z][A-Za-z0-9_]*"),

    # STRUCTURE
    "LINEBREAK": re.compile(r"^\n$"),        
    "EXCLAMATION": re.compile(r"^!$"),      
    "TEXT": re.compile(r"^[^\n\r]*$"),      

    # WHITESPACE
    "WHITESPACE": re.compile(r"\s+")

}
