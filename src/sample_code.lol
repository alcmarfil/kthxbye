BTW This is a comment before HAI - should be allowed

BTW Functions can be defined BEFORE HAI (per spec)
HOW IZ I helperBefore YR x
    FOUND YR SUM OF x AN 1
IF U SAY SO

BTW Another comment before HAI
OBTW 
This is a multi-line comment
that should also be allowed
TLDR
HAI
    BTW Program must start with HAI (after optional functions)

    WAZZUP
        I HAS A name BTW this is a variable declaration
        I HAS A num1
        I HAS A num2
        I HAS A animal
    BUHBYE
    IM IN YR print10 UPPIN YR temp TIL BOTH SAEM temp AN 10
        VISIBLE temp
    IM OUTTA YR print10

    GIMMEH num1

    OBTW HADSHHSAD
    TLDR BOTH SAEM num1 AN BIGGR OF num1 AN 0 
    O RLY? 
        YA RLY 
            VISIBLE "The number is positive or zero."
        NO WAI
            VISIBLE "The number is negative."
    OIC

    VISIBLE "Enter an animal (cat/dog/cow):"
    GIMMEH animal
    WTF? 
        OMG "cat" 
            VISIBLE "Meow! It's a cat."
            GTFO
        OMG "dog"
            VISIBLE "Woof! It's a dog."
            GTFO
        OMG "cow"
            VISIBLE "Moo! It's a cow."
            GTFO
        OMGWTF
            VISIBLE "I don't know that animal!"
        BTW AHAH
    OIC BTW HAHAH

    BTW Functions can be defined after HAI (before WAZZUP or after statements)
    HOW IZ I addNum YR x AN YR y 
        FOUND YR SUM OF x AN y BTW AHSHSH
    IF U SAY SO 

    HOW IZ I printName YR person
        VISIBLE "Hello, " person
        GTFO
    IF U SAY SO BTW HAHSDUIHUAS

    HOW IZ I printNum YR x
        FOUND YR x 
    IF U SAY SO

    BTW Test function with no explicit return - should implicitly return NOOB
    HOW IZ I doSomething YR value
        VISIBLE "Processing: " AN value
        VISIBLE "Done processing"
    IF U SAY SO

    GIMMEH num1 BTWHHAS 
    GIMMEH num2

    I IZ addNum YR num1 AN YR num2 MKAY BTW HASHDHAUS
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
    I IZ helperBefore YR 5 MKAY BTW HAHASH
    VISIBLE IT

    BTW Test function defined after KTHXBYE

KTHXBYE

BTW Functions can be defined AFTER KTHXBYE (per spec)
HOW IZ I helperAfter YR x
    FOUND YR DIFF OF x AN 1
IF U SAY SO

BTW This comment after KTHXBYE should be allowed (filtered by lexer)