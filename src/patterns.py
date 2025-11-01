#regex patterns

import re

PATTERNS = {
    # KEYWORDS
    # Core structure
    "HAI": re.compile(r"^HAI$"),
    "KTHXBYE": re.compile(r"^KTHXBYE$"),

    # Comments
    "BTW": re.compile(r"^BTW$"),
    "OBTW": re.compile(r"^OBTW$"),
    "TLDR": re.compile(r"^TLDR$"),

    # Variable declaration
    "I_HAS_A": re.compile(r"^I HAS A$"),
    "ITZ": re.compile(r"^ITZ$"),
    "R": re.compile(r"^R$"),

    # Arithmetic
    "SUM_OF": re.compile(r"^SUM OF$"),
    "DIFF_OF": re.compile(r"^DIFF OF$"),
    "PRODUKT_OF": re.compile(r"^PRODUKT OF$"),
    "QUOSHUNT_OF": re.compile(r"^QUOSHUNT OF$"),
    "MOD_OF": re.compile(r"^MOD OF$"),
    "BIGGR_OF": re.compile(r"^BIGGR OF$"),
    "SMALLR_OF": re.compile(r"^SMALLR OF$"),

    # Boolean
    "BOTH_OF": re.compile(r"^BOTH OF$"),
    "EITHER_OF": re.compile(r"^EITHER OF$"),
    "WON_OF": re.compile(r"^WON OF$"),
    "NOT": re.compile(r"^NOT$"),
    "ANY_OF": re.compile(r"^ANY OF$"),
    "ALL_OF": re.compile(r"^ALL OF$"),

    # Comparison
    "BOTH_SAEM": re.compile(r"^BOTH SAEM$"),
    "DIFFRINT": re.compile(r"^DIFFRINT$"),

    # String concatenation
    "SMOOSH": re.compile(r"^SMOOSH$"),

    # Typecasting 
    "MAEK": re.compile(r"^MAEK$"),
    "A": re.compile(r"^A$"),
    "IS_NOW_A": re.compile(r"^IS NOW A$"),

    # I/O
    "VISIBLE": re.compile(r"^VISIBLE$"),
    "GIMMEH": re.compile(r"^GIMMEH$"),

    # Switch/Case
    "WTF": re.compile(r"^WTF\?$"),
    "OMG": re.compile(r"^OMG$"),
    "OMGWTF": re.compile(r"^OMGWTF$"),

    # Conditionals
    "O_RLY": re.compile(r"^O RLY\?$"),
    "YA_RLY": re.compile(r"^YA RLY$"),
    "MEBBE": re.compile(r"^MEBBE$"),
    "NO_WAI": re.compile(r"^NO WAI$"),
    "OIC": re.compile(r"^OIC$"),

    # Loops
    "IM_IN_YR": re.compile(r"^IM IN YR$"),
    "UPPIN": re.compile(r"^UPPIN$"),
    "NERFIN": re.compile(r"^NERFIN$"),
    "YR": re.compile(r"^YR$"),
    "TIL": re.compile(r"^TIL$"),
    "WILE": re.compile(r"^WILE$"),
    "IM_OUTTA_YR": re.compile(r"^IM OUTTA YR$"),

    # Functions
    "HOW_IZ_I": re.compile(r"^HOW IZ I$"),
    "IF_U_SAY_SO": re.compile(r"^IF U SAY SO$"),
    "GTFO": re.compile(r"^GTFO$"),
    "FOUND_YR": re.compile(r"^FOUND YR$"),
    "I_IZ": re.compile(r"^I IZ$"),
    "MKAY": re.compile(r"^MKAY$"),

    # Others
    "WAZZUP": re.compile(r"^WAZZUP$"),
    "BUHBYE": re.compile(r"^BUHBYE$"),

    # CONNECTOR
     "AN": re.compile(r"^AN$"),      

    # LITERALS 
    "NUMBR_LITERAL": re.compile(r"^-?[0-9]+$"),
    "NUMBAR_LITERAL": re.compile(r"^-?[0-9]+\.[0-9]+$"),
    "YARN_LITERAL": re.compile(r'^"[^"\n]*"$'),
    "TROOF_LITERAL": re.compile(r"^(WIN|FAIL)$"),
    "TYPE_LITERAL": re.compile(r"^(NUMBR|NUMBAR|YARN|TROOF|NOOB|TYPE)$"),        

   # IDENTIFIERS 
    "VAR_IDENTIFIER": re.compile(r"^[A-Za-z][A-Za-z0-9_]*$"),
    "FUNC_IDENTIFIER": re.compile(r"^[A-Za-z][A-Za-z0-9_]*$"),
    "LOOP_IDENTIFIER": re.compile(r"^[A-Za-z][A-Za-z0-9_]*$"),


    # STRUCTURE (catch-all)
    "LINEBREAK": re.compile(r"^\n$"),        
    "EXCLAMATION": re.compile(r"^!$"),      
    "TEXT": re.compile(r"^[^\n\r]*$"),      
  
}

