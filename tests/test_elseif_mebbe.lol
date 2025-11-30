HAI
    WAZZUP
        I HAS A x
        I HAS A y
        I HAS A z
        I HAS A score
        I HAS A grade
        I HAS A temp
    BUHBYE
    
    BTW ========================================
    BTW Test: Else-If Clauses (MEBBE) - Extra Credit
    BTW ========================================
    BTW This test demonstrates multiple MEBBE clauses in conditionals
    
    VISIBLE "=== Else-If (MEBBE) Test ==="
    
    BTW Test 1: Multiple MEBBE clauses with numeric conditions
    VISIBLE "Test 1: Multiple MEBBE with Numeric Conditions"
    score R 85
    
    BOTH SAEM BIGGR OF score AN 90 AN score
    O RLY?
        YA RLY
            VISIBLE "  Grade: A (score >= 90)"
        MEBBE BOTH SAEM BIGGR OF score AN 80 AN score
            VISIBLE "  Grade: B (80 <= score < 90)"
        MEBBE BOTH SAEM BIGGR OF score AN 70 AN score
            VISIBLE "  Grade: C (70 <= score < 80)"
        MEBBE BOTH SAEM BIGGR OF score AN 60 AN score
            VISIBLE "  Grade: D (60 <= score < 70)"
        NO WAI
            VISIBLE "  Grade: F (score < 60)"
    OIC
    
    VISIBLE ""
    
    BTW Test 2: MEBBE with string comparisons
    VISIBLE "Test 2: MEBBE with String Comparisons"
    grade R "B"
    
    BOTH SAEM grade AN "A"
    O RLY?
        YA RLY
            VISIBLE "  Excellent!"
        MEBBE BOTH SAEM grade AN "B"
            VISIBLE "  Good job!"
        MEBBE BOTH SAEM grade AN "C"
            VISIBLE "  Average"
        MEBBE BOTH SAEM grade AN "D"
            VISIBLE "  Needs improvement"
        NO WAI
            VISIBLE "  Failed"
    OIC
    
    VISIBLE ""
    
    BTW Test 3: MEBBE with boolean expressions
    VISIBLE "Test 3: MEBBE with Boolean Expressions"
    x R 10
    y R 20
    z R 15
    
    BOTH SAEM BIGGR OF x AN y AN x
    O RLY?
        YA RLY
            VISIBLE "  x is the largest"
        MEBBE BOTH SAEM BIGGR OF y AN z AN y
            VISIBLE "  y is the largest"
        MEBBE BOTH SAEM BIGGR OF z AN x AN z
            VISIBLE "  z is the largest"
        NO WAI
            VISIBLE "  All values are equal"
    OIC
    
    VISIBLE ""
    
    BTW Test 4: Nested conditionals with MEBBE
    VISIBLE "Test 4: Nested Conditionals with MEBBE"
    x R 5
    y R 10
    
    BOTH SAEM BIGGR OF x AN 0 AN x
    O RLY?
        YA RLY
            VISIBLE "  x is positive"
            BOTH SAEM BIGGR OF y AN 0 AN y
            O RLY?
                YA RLY
                    VISIBLE "    Both x and y are positive"
                MEBBE BOTH SAEM y AN 0
                    VISIBLE "    x is positive, y is zero"
                NO WAI
                    VISIBLE "    x is positive, y is negative"
            OIC
        MEBBE BOTH SAEM x AN 0
            VISIBLE "  x is zero"
        NO WAI
            VISIBLE "  x is negative"
    OIC
    
    VISIBLE ""
    
    BTW Test 5: MEBBE with arithmetic expressions
    VISIBLE "Test 5: MEBBE with Arithmetic in Conditions"
    temp R 25
    
    BOTH SAEM BIGGR OF temp AN 30 AN temp
    O RLY?
        YA RLY
            VISIBLE "  Hot (temp >= 30)"
        MEBBE BOTH SAEM BIGGR OF temp AN 20 AN temp
            VISIBLE "  Warm (20 <= temp < 30)"
        MEBBE BOTH SAEM BIGGR OF temp AN 10 AN temp
            VISIBLE "  Cool (10 <= temp < 20)"
        NO WAI
            VISIBLE "  Cold (temp < 10)"
    OIC
    
    VISIBLE ""
    VISIBLE "=== Else-If (MEBBE) Test Complete ==="

KTHXBYE
