HAI
    WAZZUP
        I HAS A i
        I HAS A j
        I HAS A k
        I HAS A result
        I HAS A temp
    BUHBYE
    
    BTW ========================================
    BTW Test: Loop Nesting (Extra Credit Feature)
    BTW ========================================
    BTW This test demonstrates nested loops at multiple levels
    
    VISIBLE "=== Loop Nesting Test ==="
    
    BTW Test 1: Double nested loops
    VISIBLE "Test 1: Double Nested Loops"
    i R 0
    j R 0
    result R 0
    
    IM IN YR outer UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        j R 0
        IM IN YR inner UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
            result R SUM OF result AN PRODUKT OF i AN j
            temp R i
            VISIBLE "  Outer i=" + temp
            temp R j
            VISIBLE "    Inner j=" + temp
        IM OUTTA YR inner
    IM OUTTA YR outer
    
    VISIBLE "Final result: " + result
    VISIBLE ""
    
    BTW Test 2: Triple nested loops
    VISIBLE "Test 2: Triple Nested Loops"
    i R 0
    j R 0
    k R 0
    result R 0
    
    IM IN YR level1 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 2 AN i
        j R 0
        IM IN YR level2 UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
            k R 0
            IM IN YR level3 UPPIN YR k WILE DIFFRINT BIGGR OF k AN 2 AN k
                result R SUM OF result AN SUM OF SUM OF i AN j AN k
                temp R i
                VISIBLE "    Level 1: " + temp
                temp R j
                VISIBLE "      Level 2: " + temp
                temp R k
                VISIBLE "        Level 3: " + temp
            IM OUTTA YR level3
        IM OUTTA YR level2
    IM OUTTA YR level1
    
    VISIBLE "Final result: " + result
    VISIBLE ""
    
    BTW Test 3: Mixed nested loops (UPPIN and NERFIN)
    VISIBLE "Test 3: Mixed Loop Types (UPPIN and NERFIN)"
    i R 0
    j R 5
    
    IM IN YR outer_mixed UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        j R 5
        IM IN YR inner_mixed NERFIN YR j TIL BOTH SAEM j AN 2
            temp R i
            VISIBLE "  Outer (UPPIN) i=" + temp
            temp R j
            VISIBLE "    Inner (NERFIN) j=" + temp
        IM OUTTA YR inner_mixed
    IM OUTTA YR outer_mixed
    
    VISIBLE ""
    VISIBLE "=== Loop Nesting Test Complete ==="

KTHXBYE
