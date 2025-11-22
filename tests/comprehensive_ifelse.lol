HAI
    WAZZUP
        I HAS A x
        I HAS A y
        I HAS A z
        I HAS A result
        I HAS A flag
        I HAS A counter
        I HAS A temp
        I HAS A input
    BUHBYE
    
    BTW Test 1: Nested if-else statements
    VISIBLE "=== Test 1: Nested Conditionals ==="
    x R 10
    y R 20
    z R 30
    
    BOTH SAEM BIGGR OF x AN y AN x
    O RLY?
        YA RLY
            VISIBLE "x >= y"
            temp R BIGGR OF z AN x
            BOTH SAEM temp AN z
            O RLY?
                YA RLY
                    VISIBLE "z >= x"
                    temp R SUM OF x AN y
                    BOTH SAEM z AN temp
                    O RLY?
                        YA RLY
                            VISIBLE "z == x + y (nested level 3)"
                        NO WAI
                            VISIBLE "z != x + y"
                    OIC
                NO WAI
                    VISIBLE "z < x"
            OIC
        NO WAI
            VISIBLE "x < y"
    OIC
    
    BTW Test 2: Complex boolean expressions
    VISIBLE "=== Test 2: Complex Boolean Logic ==="
    x R WIN
    y R FAIL
    z R WIN
    
    BOTH OF BOTH OF x AN y AN z
    O RLY?
        YA RLY
            VISIBLE "All true (should be false)"
        NO WAI
            VISIBLE "Not all true (correct)"
    OIC
    
    EITHER OF BOTH OF x AN y AN z
    O RLY?
        YA RLY
            VISIBLE "Either (x AND y) OR z (should be true)"
        NO WAI
            VISIBLE "Neither (x AND y) nor z"
    OIC
    
    WON OF x AN y
    O RLY?
        YA RLY
            VISIBLE "Exactly one of x or y is true (correct)"
        NO WAI
            VISIBLE "Both or neither are true"
    OIC
    
    BTW Test 3: Multiple MEBBE clauses
    VISIBLE "=== Test 3: Multiple MEBBE ==="
    counter R 3
    
    BOTH SAEM counter AN 1
    O RLY?
        YA RLY
            VISIBLE "Counter is 1"
        MEBBE BOTH SAEM counter AN 2
            VISIBLE "Counter is 2"
        MEBBE BOTH SAEM counter AN 3
            VISIBLE "Counter is 3 (should match)"
        MEBBE BIGGR OF counter AN 3
            VISIBLE "Counter > 3"
        NO WAI
            VISIBLE "Counter is something else"
    OIC
    
    BTW Test 4: If-else with type casting
    VISIBLE "=== Test 4: Type Casting in Conditions ==="
    input R "42"
    result R MAEK input A NUMBR
    
    BOTH SAEM result AN 42
    O RLY?
        YA RLY
            VISIBLE "String '42' cast to NUMBR equals 42"
        NO WAI
            VISIBLE "Type cast failed"
    OIC
    
    BOTH SAEM MAEK 0 A TROOF AN FAIL
    O RLY?
        YA RLY
            VISIBLE "0 cast to TROOF is FAIL"
        NO WAI
            VISIBLE "0 cast to TROOF is not FAIL"
    OIC
    
    BTW Test 5: Arithmetic operations in conditions
    VISIBLE "=== Test 5: Arithmetic in Conditions ==="
    x R 10
    y R 5
    z R 15
    
    BOTH SAEM SUM OF x AN y AN z
    O RLY?
        YA RLY
            VISIBLE "x + y == z (10 + 5 == 15)"
        NO WAI
            VISIBLE "x + y != z"
    OIC
    
    DIFFRINT PRODUKT OF x AN 2 AN z
    O RLY?
        YA RLY
            VISIBLE "x * 2 != z (10 * 2 != 15)"
        NO WAI
            VISIBLE "x * 2 == z"
    OIC
    
    BTW Test 6: String comparisons
    VISIBLE "=== Test 6: String Comparisons ==="
    x R "hello"
    y R "world"
    temp R SMOOSH x AN " " AN y
    
    BOTH SAEM temp AN "hello world"
    O RLY?
        YA RLY
            VISIBLE "Concatenated string matches"
        NO WAI
            VISIBLE "Concatenated string doesn't match"
    OIC
    
    DIFFRINT x AN y
    O RLY?
        YA RLY
            VISIBLE "x != y (strings are different)"
        NO WAI
            VISIBLE "x == y"
    OIC
    
    BTW Test 7: Nested with operations
    VISIBLE "=== Test 7: Nested with Operations ==="
    x R 100
    y R 50
    z R 25
    
    BIGGR OF x AN y
    O RLY?
        YA RLY
            VISIBLE "x > y"
            temp R SMALLR OF y AN z
            temp
            O RLY?
                YA RLY
                    VISIBLE "y < z (should be false)"
                NO WAI
                    VISIBLE "y >= z (correct)"
                    temp R QUOSHUNT OF x AN z
                    BOTH SAEM temp AN 4
                    O RLY?
                        YA RLY
                            VISIBLE "x / z == 4 (100 / 25 == 4)"
                        NO WAI
                            VISIBLE "x / z != 4"
                    OIC
            OIC
        NO WAI
            VISIBLE "x <= y"
    OIC
    
    BTW Test 8: Boolean negation
    VISIBLE "=== Test 8: Boolean Negation ==="
    flag R WIN
    
    NOT flag
    O RLY?
        YA RLY
            VISIBLE "NOT flag is true (flag is false)"
        NO WAI
            VISIBLE "NOT flag is false (flag is true, correct)"
    OIC
    
    flag R FAIL
    
    NOT flag
    O RLY?
        YA RLY
            VISIBLE "NOT flag is true (flag is false, correct)"
        NO WAI
            VISIBLE "NOT flag is false (flag is true)"
    OIC
    
    BTW Test 9: Complex nested with ALL_OF and ANY_OF
    VISIBLE "=== Test 9: ALL_OF and ANY_OF ==="
    x R WIN
    y R WIN
    z R FAIL
    
    ALL OF x AN y AN z MKAY
    O RLY?
        YA RLY
            VISIBLE "ALL OF x, y, z is true (should be false)"
        NO WAI
            VISIBLE "ALL OF x, y, z is false (correct)"
    OIC
    
    ANY OF x AN y AN z MKAY
    O RLY?
        YA RLY
            VISIBLE "ANY OF x, y, z is true (correct)"
        NO WAI
            VISIBLE "ANY OF x, y, z is false"
    OIC
    
    BTW Test 10: Edge cases with zero and empty strings
    VISIBLE "=== Test 10: Edge Cases ==="
    x R 0
    y R ""
    
    BOTH SAEM x AN 0
    O RLY?
        YA RLY
            VISIBLE "x == 0"
        NO WAI
            VISIBLE "x != 0"
    OIC
    
    BOTH SAEM y AN ""
    O RLY?
        YA RLY
            VISIBLE "y is empty string"
        NO WAI
            VISIBLE "y is not empty"
    OIC
    
    BOTH SAEM MAEK x A TROOF AN FAIL
    O RLY?
        YA RLY
            VISIBLE "0 cast to TROOF is FAIL"
        NO WAI
            VISIBLE "0 cast to TROOF is not FAIL"
    OIC
    
    BOTH SAEM MAEK y A TROOF AN FAIL
    O RLY?
        YA RLY
            VISIBLE "Empty string cast to TROOF is FAIL"
        NO WAI
            VISIBLE "Empty string cast to TROOF is not FAIL"
    OIC

KTHXBYE

