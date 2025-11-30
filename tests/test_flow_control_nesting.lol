HAI
    WAZZUP
        I HAS A i
        I HAS A j
        I HAS A choice
        I HAS A x
        I HAS A y
        I HAS A temp
    BUHBYE
    
    BTW ========================================
    BTW Test: Nesting of Different Flow Control Statements
    BTW ========================================
    BTW This test demonstrates nesting of conditionals, switches, and loops
    
    VISIBLE "=== Flow Control Nesting Test ==="
    
    BTW Test 1: Conditional inside Loop
    VISIBLE "Test 1: Conditional Inside Loop"
    i R 0
    IM IN YR outer_loop UPPIN YR i WILE DIFFRINT BIGGR OF i AN 5 AN i
        temp R i
        BOTH SAEM MOD OF i AN 2 AN 0
        O RLY?
            YA RLY
                VISIBLE "  i=" + temp + " is even"
            NO WAI
                VISIBLE "  i=" + temp + " is odd"
        OIC
    IM OUTTA YR outer_loop
    
    VISIBLE ""
    
    BTW Test 2: Switch inside Conditional
    VISIBLE "Test 2: Switch Inside Conditional"
    choice R "menu1"
    x R 5
    
    BOTH SAEM BIGGR OF x AN 0 AN x
    O RLY?
        YA RLY
            VISIBLE "  x is positive"
            choice
            WTF?
                OMG "menu1"
                    VISIBLE "    In menu1"
                    GTFO
                OMG "menu2"
                    VISIBLE "    In menu2"
                    GTFO
                OMGWTF
                    VISIBLE "    Unknown menu"
            OIC
        NO WAI
            VISIBLE "  x is not positive"
    OIC
    
    VISIBLE ""
    
    BTW Test 3: Loop inside Switch
    VISIBLE "Test 3: Loop Inside Switch"
    choice R "loop"
    
    choice
    WTF?
        OMG "loop"
            VISIBLE "    Starting loop in switch"
            j R 0
            IM IN YR inner_loop UPPIN YR j WILE DIFFRINT BIGGR OF j AN 3 AN j
                temp R j
                VISIBLE "      j=" + temp
            IM OUTTA YR inner_loop
            VISIBLE "    Loop completed"
            GTFO
        OMG "skip"
            VISIBLE "    Skipping loop"
            GTFO
        OMGWTF
            VISIBLE "    Default case"
    OIC
    
    VISIBLE ""
    
    BTW Test 4: Conditional inside Switch inside Loop
    VISIBLE "Test 4: Conditional Inside Switch Inside Loop"
    i R 0
    choice R "test"
    
    IM IN YR nested_loop UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        temp R i
        VISIBLE "  Loop iteration: " + temp
        choice
        WTF?
            OMG "test"
                BOTH SAEM MOD OF i AN 2 AN 0
                O RLY?
                    YA RLY
                        VISIBLE "    Even iteration"
                    NO WAI
                        VISIBLE "    Odd iteration"
                OIC
                GTFO
            OMGWTF
                VISIBLE "    Default"
        OIC
    IM OUTTA YR nested_loop
    
    VISIBLE ""
    
    BTW Test 5: Switch inside Conditional inside Loop
    VISIBLE "Test 5: Switch Inside Conditional Inside Loop"
    i R 0
    
    IM IN YR complex_loop UPPIN YR i WILE DIFFRINT BIGGR OF i AN 4 AN i
        temp R i
        BOTH SAEM BIGGR OF i AN 2 AN i
        O RLY?
            YA RLY
                VISIBLE "  i=" + temp + " >= 2"
                choice R "high"
                choice
                WTF?
                    OMG "high"
                        VISIBLE "    High value"
                        GTFO
                    OMG "low"
                        VISIBLE "    Low value"
                        GTFO
                    OMGWTF
                        VISIBLE "    Other"
                OIC
            NO WAI
                VISIBLE "  i=" + temp + " < 2"
        OIC
    IM OUTTA YR complex_loop
    
    VISIBLE ""
    
    BTW Test 6: Multiple levels of nesting
    VISIBLE "Test 6: Multiple Levels of Nesting"
    i R 0
    j R 0
    
    IM IN YR level1 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 2 AN i
        temp R i
        VISIBLE "  Level 1: i=" + temp
        BOTH SAEM i AN 1
        O RLY?
            YA RLY
                VISIBLE "    Level 2: Conditional true"
                j R 0
                IM IN YR level3 UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
                    temp R j
                    VISIBLE "      Level 3: Loop j=" + temp
                    choice R "nested"
                    choice
                    WTF?
                        OMG "nested"
                            VISIBLE "        Level 4: Switch case"
                            GTFO
                        OMGWTF
                            VISIBLE "        Level 4: Default"
                    OIC
                IM OUTTA YR level3
            NO WAI
                VISIBLE "    Level 2: Conditional false"
        OIC
    IM OUTTA YR level1
    
    VISIBLE ""
    VISIBLE "=== Flow Control Nesting Test Complete ==="

KTHXBYE
