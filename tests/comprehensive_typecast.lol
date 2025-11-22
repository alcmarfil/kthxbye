HAI
    WAZZUP
        I HAS A numbr_var
        I HAS A numbar_var
        I HAS A yarn_var
        I HAS A troof_var
        I HAS A result
        I HAS A temp
        I HAS A input
        I HAS A counter
    BUHBYE
    
    BTW Test 1: NUMBR to all types
    VISIBLE "=== Test 1: NUMBR Conversions ==="
    numbr_var R 42
    
    VISIBLE "Original NUMBR: " + numbr_var
    
    numbar_var R MAEK numbr_var A NUMBAR
    VISIBLE "NUMBR to NUMBAR: " + numbar_var
    
    yarn_var R MAEK numbr_var A YARN
    VISIBLE "NUMBR to YARN: " + yarn_var
    
    troof_var R MAEK numbr_var A TROOF
    VISIBLE "NUMBR to TROOF: " + troof_var
    
    BTW Test 2: NUMBAR to all types
    VISIBLE "=== Test 2: NUMBAR Conversions ==="
    numbar_var R 3.14159
    
    VISIBLE "Original NUMBAR: " + numbar_var
    
    numbr_var R MAEK numbar_var A NUMBR
    VISIBLE "NUMBAR to NUMBR (truncated): " + numbr_var
    
    yarn_var R MAEK numbar_var A YARN
    VISIBLE "NUMBAR to YARN (2 decimals): " + yarn_var
    
    troof_var R MAEK numbar_var A TROOF
    VISIBLE "NUMBAR to TROOF: " + troof_var
    
    BTW Test 3: YARN to all types
    VISIBLE "=== Test 3: YARN Conversions ==="
    yarn_var R "123"
    
    VISIBLE "Original YARN: " + yarn_var
    
    numbr_var R MAEK yarn_var A NUMBR
    VISIBLE "YARN '123' to NUMBR: " + numbr_var
    
    numbar_var R MAEK yarn_var A NUMBAR
    VISIBLE "YARN '123' to NUMBAR: " + numbar_var
    
    troof_var R MAEK yarn_var A TROOF
    VISIBLE "YARN '123' to TROOF: " + troof_var
    
    yarn_var R "0"
    troof_var R MAEK yarn_var A TROOF
    VISIBLE "YARN '0' to TROOF: " + troof_var
    
    yarn_var R ""
    troof_var R MAEK yarn_var A TROOF
    VISIBLE "YARN '' to TROOF: " + troof_var
    
    BTW Test 4: TROOF to all types
    VISIBLE "=== Test 4: TROOF Conversions ==="
    troof_var R WIN
    
    VISIBLE "Original TROOF: " + troof_var
    
    numbr_var R MAEK troof_var A NUMBR
    VISIBLE "TROOF WIN to NUMBR: " + numbr_var
    
    numbar_var R MAEK troof_var A NUMBAR
    VISIBLE "TROOF WIN to NUMBAR: " + numbar_var
    
    yarn_var R MAEK troof_var A YARN
    VISIBLE "TROOF WIN to YARN: " + yarn_var
    
    troof_var R FAIL
    numbr_var R MAEK troof_var A NUMBR
    VISIBLE "TROOF FAIL to NUMBR: " + numbr_var
    
    BTW Test 5: Chained type casts
    VISIBLE "=== Test 5: Chained Type Casts ==="
    numbr_var R 100
    
    result R MAEK MAEK MAEK numbr_var A YARN A NUMBR A NUMBAR
    VISIBLE "100 -> YARN -> NUMBR -> NUMBAR: " + result
    
    result R MAEK MAEK MAEK WIN A NUMBR A YARN A TROOF
    VISIBLE "WIN -> NUMBR -> YARN -> TROOF: " + result
    
    BTW Test 6: Type casting in expressions
    VISIBLE "=== Test 6: Type Casting in Expressions ==="
    numbr_var R 10
    numbar_var R 2.5
    
    result R SUM OF numbr_var AN MAEK numbar_var A NUMBR
    VISIBLE "10 + (2.5 as NUMBR): " + result
    
    result R PRODUKT OF MAEK numbr_var A NUMBAR AN numbar_var
    VISIBLE "(10 as NUMBAR) * 2.5: " + result
    
    yarn_var R "5"
    result R SUM OF MAEK yarn_var A NUMBR AN numbr_var
    VISIBLE "('5' as NUMBR) + 10: " + result
    
    BTW Test 7: Type casting with zero values
    VISIBLE "=== Test 7: Zero Value Conversions ==="
    numbr_var R 0
    numbar_var R 0.0
    yarn_var R "0"
    
    VISIBLE "0 to TROOF: " + MAEK numbr_var A TROOF
    VISIBLE "0.0 to TROOF: " + MAEK numbar_var A TROOF
    VISIBLE "'0' to TROOF: " + MAEK yarn_var A TROOF
    VISIBLE "'' to TROOF: " + MAEK "" A TROOF
    
    BTW Test 8: Type casting with negative numbers
    VISIBLE "=== Test 8: Negative Number Conversions ==="
    numbr_var R -42
    numbar_var R -3.14
    
    VISIBLE "-42 to YARN: " + MAEK numbr_var A YARN
    VISIBLE "-3.14 to NUMBR: " + MAEK numbar_var A NUMBR
    VISIBLE "-42 to TROOF: " + MAEK numbr_var A TROOF
    VISIBLE "-3.14 to TROOF: " + MAEK numbar_var A TROOF
    
    BTW Test 9: Type casting in conditionals
    VISIBLE "=== Test 9: Type Casting in Conditionals ==="
    yarn_var R "42"
    
    BOTH SAEM MAEK yarn_var A NUMBR AN 42
    O RLY?
        YA RLY
            VISIBLE "String '42' cast to NUMBR equals 42"
        NO WAI
            VISIBLE "Type cast comparison failed"
    OIC
    
    BOTH SAEM MAEK 1 A TROOF AN WIN
    O RLY?
        YA RLY
            VISIBLE "1 cast to TROOF equals WIN"
        NO WAI
            VISIBLE "1 cast to TROOF does not equal WIN"
    OIC
    
    BTW Test 10: Type casting with SMOOSH
    VISIBLE "=== Test 10: Type Casting with SMOOSH ==="
    numbr_var R 10
    numbar_var R 20.5
    troof_var R WIN
    
    result R SMOOSH "Number: " AN MAEK numbr_var A YARN AN ", Float: " AN MAEK numbar_var A YARN AN ", Bool: " AN MAEK troof_var A YARN
    VISIBLE result
    
    BTW Test 11: Type casting in loops
    VISIBLE "=== Test 11: Type Casting in Loops ==="
    counter R 0
    
    IM IN YR test1 UPPIN YR counter WILE SMALLR OF counter AN 5
        temp R MAEK counter A YARN
        VISIBLE "Counter as NUMBR: " + counter + ", as YARN: " + temp
        troof_var R MAEK counter A TROOF
        VISIBLE "  Counter as TROOF: " + troof_var
    IM OUTTA YR test1
    
    BTW Test 12: Type casting with arithmetic operations
    VISIBLE "=== Test 12: Type Casting with Arithmetic ==="
    yarn_var R "10"
    numbar_var R 5.5
    
    result R SUM OF MAEK yarn_var A NUMBR AN MAEK numbar_var A NUMBR
    VISIBLE "('10' as NUMBR) + (5.5 as NUMBR): " + result
    
    result R PRODUKT OF MAEK yarn_var A NUMBAR AN numbar_var
    VISIBLE "('10' as NUMBAR) * 5.5: " + result
    
    BTW Test 13: Type casting edge cases
    VISIBLE "=== Test 13: Edge Cases ==="
    yarn_var R "3.14"
    
    numbar_var R MAEK yarn_var A NUMBAR
    VISIBLE "'3.14' to NUMBAR: " + numbar_var
    
    numbr_var R MAEK numbar_var A NUMBR
    VISIBLE "3.14 to NUMBR (truncated): " + numbr_var
    
    yarn_var R "-100"
    numbr_var R MAEK yarn_var A NUMBR
    VISIBLE "'-100' to NUMBR: " + numbr_var
    
    BTW Test 14: Type casting with comparison operations
    VISIBLE "=== Test 14: Type Casting with Comparisons ==="
    yarn_var R "50"
    numbr_var R 50
    
    BOTH SAEM MAEK yarn_var A NUMBR AN numbr_var
    O RLY?
        YA RLY
            VISIBLE "String '50' cast to NUMBR equals 50"
        NO WAI
            VISIBLE "Comparison failed"
    OIC
    
    BIGGR OF MAEK "100" A NUMBR AN 50
    O RLY?
        YA RLY
            VISIBLE "'100' cast to NUMBR > 50"
        NO WAI
            VISIBLE "Comparison failed"
    OIC
    
    BTW Test 15: Complex type casting scenarios
    VISIBLE "=== Test 15: Complex Scenarios ==="
    numbr_var R 7
    numbar_var R 2.718
    
    result R MAEK SUM OF numbr_var AN MAEK numbar_var A NUMBR A YARN
    VISIBLE "(7 + (2.718 as NUMBR)) as YARN: " + result
    
    result R MAEK PRODUKT OF MAEK numbr_var A NUMBAR AN numbar_var A NUMBR
    VISIBLE "((7 as NUMBAR) * 2.718) as NUMBR: " + result
    
    troof_var R BOTH OF BIGGR OF numbr_var AN 5 AN WIN
    result R MAEK troof_var A YARN
    VISIBLE "Complex boolean expression as YARN: " + result

KTHXBYE

