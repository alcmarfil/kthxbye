BTW This is a comment before HAI - should be allowed

BTW Functions can be defined BEFORE HAI (per spec)
HOW IZ I helperBefore YR x
    FOUND YR SUM OF x AN 1
IF U SAY SO

HAI
    BTW Program must start with HAI (after optional functions)

    WAZZUP
        I HAS A name
        I HAS A num1
        I HAS A num2
    BUHBYE
    
    BTW Functions can be defined after HAI (before WAZZUP or after statements)
    HOW IZ I addNum YR x AN YR y
        FOUND YR SUM OF x AN y
    IF U SAY SO

    HOW IZ I printName YR person
        VISIBLE "Hello, " AN person
        GTFO
    IF U SAY SO

    HOW IZ I printNum YR x
        FOUND YR x
    IF U SAY SO

    BTW Test function with no explicit return - should implicitly return NOOB
    HOW IZ I doSomething YR value
        VISIBLE "Processing: " AN value
        VISIBLE "Done processing"
    IF U SAY SO

    GIMMEH num1
    GIMMEH num2

    I IZ addNum YR num1 AN YR num2 MKAY
    VISIBLE IT 

    GIMMEH name
    I IZ printName YR name MKAY
    VISIBLE IT

    I IZ printNum YR SUM OF num1 AN 2 MKAY
    VISIBLE IT

    BTW Test implicit NOOB return
    I IZ doSomething YR "test" MKAY
    VISIBLE IT

    BTW Test function defined before HAI
    I IZ helperBefore YR 5 MKAY
    VISIBLE IT

KTHXBYE

BTW Functions can be defined AFTER KTHXBYE (per spec)
HOW IZ I helperAfter YR x
    FOUND YR DIFF OF x AN 1
IF U SAY SO

BTW This comment after KTHXBYE should be allowed (filtered by lexer)