HAI
    WAZZUP
        I HAS A counter ITZ 0
        I HAS A i ITZ 0
        I HAS A sum ITZ 0
        I HAS A test_var ITZ 5
        I HAS A result
    BUHBYE

    VISIBLE "=== Test 1: Loops ==="
    
    BTW Test loop with UPPIN and TIL
    counter R 0
    IM IN YR loop1 UPPIN YR counter TIL BOTH SAEM counter AN 3
        VISIBLE "Loop iteration: " AN counter
    IM OUTTA YR loop1
    
    BTW Test loop with NERFIN and WILE
    counter R 3
    IM IN YR loop2 NERFIN YR counter WILE BOTH SAEM counter AN 0
        VISIBLE "Countdown: " AN counter
    IM OUTTA YR loop2
    
    BTW Test loop with GTFO (break)
    counter R 0
    IM IN YR loop3 UPPIN YR counter TIL BOTH SAEM counter AN 10
        VISIBLE "Counter: " AN counter
        I HAS A temp ITZ SUM OF counter AN 1
        BOTH SAEM temp AN 3
        O RLY?
            YA RLY
                VISIBLE "Breaking at counter=2!"
                GTFO
        OIC
    IM OUTTA YR loop3
    
    VISIBLE ""
    VISIBLE "=== Test 2: Switch (WTF?) ==="
    
    test_var R 1
    test_var
    WTF?
        OMG 1
            VISIBLE "Case 1: test_var is 1"
            GTFO
        OMG 2
            VISIBLE "Case 2: test_var is 2"
            GTFO
        OMG 3
            VISIBLE "Case 3: test_var is 3"
            GTFO
        OMGWTF
            VISIBLE "Default: test_var is something else"
    OIC
    
    BTW Test switch with expression
    SUM OF test_var AN 1
    WTF?
        OMG 2
            VISIBLE "Sum is 2!"
            GTFO
        OMGWTF
            VISIBLE "Sum is not 2"
    OIC
    
    VISIBLE ""
    VISIBLE "=== Test 3: Conditionals (O RLY?) ==="
    
    BOTH SAEM test_var AN 1
    O RLY?
        YA RLY
            VISIBLE "test_var is 1!"
        NO WAI
            VISIBLE "test_var is not 1"
    OIC
    
    BTW Test conditional with MEBBE
    test_var R 2
    BOTH SAEM test_var AN 1
    O RLY?
        YA RLY
            VISIBLE "test_var is 1"
        MEBBE BOTH SAEM test_var AN 2
            VISIBLE "test_var is 2"
        MEBBE BOTH SAEM test_var AN 3
            VISIBLE "test_var is 3"
        NO WAI
            VISIBLE "test_var is something else"
    OIC
    
    VISIBLE ""
    VISIBLE "=== Test 4: Arithmetic Operations ==="
    
    result R SUM OF 2 AN 4
    VISIBLE "SUM OF 2 AN 4 = " AN result
    
    result R DIFF OF 4 AN 3.14
    VISIBLE "DIFF OF 4 AN 3.14 = " AN result
    
    result R QUOSHUNT OF 5 AN "12"
    VISIBLE "QUOSHUNT OF 5 AN 12 = " AN result
    
    VISIBLE ""
    VISIBLE "=== Test 5: SMOOSH (String Concatenation) ==="
    
    result R SMOOSH "Hello" AN " " AN "World" AN "!"
    VISIBLE "SMOOSH result: " AN result
    
    result R SMOOSH "Number: " AN 42 AN " Float: " AN 3.14
    VISIBLE "SMOOSH with numbers: " AN result
    
    VISIBLE ""
    VISIBLE "=== Test 6: MAEK (Typecasting) ==="
    
    test_var R 12
    VISIBLE "test_var before MAEK: " AN test_var
    MAEK test_var A NUMBAR
    VISIBLE "IT after MAEK test_var A NUMBAR: " AN IT
    VISIBLE "test_var after MAEK (should still be 12): " AN test_var
    
    MAEK test_var A YARN
    VISIBLE "IT after MAEK test_var A YARN: " AN IT
    
    VISIBLE ""
    VISIBLE "=== Test 7: IS NOW A (Type Change) ==="
    
    test_var R 17
    VISIBLE "test_var before IS NOW A: " AN test_var
    test_var IS NOW A NUMBAR
    VISIBLE "test_var after IS NOW A NUMBAR: " AN test_var
    
    test_var IS NOW A YARN
    VISIBLE "test_var after IS NOW A YARN: " AN test_var
    
    VISIBLE ""
    VISIBLE "=== Test 8: Comparisons ==="
    
    result R BOTH SAEM 5 AN 5
    VISIBLE "BOTH SAEM 5 AN 5 = " AN result
    
    result R BOTH SAEM 5 AN 5.0
    VISIBLE "BOTH SAEM 5 AN 5.0 = " AN result
    
    result R DIFFRINT 3 AN 4
    VISIBLE "DIFFRINT 3 AN 4 = " AN result

KTHXBYE

