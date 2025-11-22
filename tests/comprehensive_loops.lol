HAI
    WAZZUP
        I HAS A i
        I HAS A j
        I HAS A k
        I HAS A sum
        I HAS A product
        I HAS A counter
        I HAS A flag
        I HAS A temp
        I HAS A result
        I HAS A max
        I HAS A pattern
    BUHBYE
    
    BTW Test 1: Nested loops
    VISIBLE "=== Test 1: Nested Loops ==="
    sum R 0
    
    IM IN YR outer UPPIN YR i WILE SMALLR OF i AN 3
        IM IN YR inner UPPIN YR j WILE SMALLR OF j AN 2
            sum R SUM OF sum AN PRODUKT OF i AN j
            VISIBLE "i=" + i + ", j=" + j + ", sum=" + sum
        IM OUTTA YR inner
    IM OUTTA YR outer
    
    VISIBLE "Final sum: " + sum
    
    BTW Test 2: Loop with complex condition
    VISIBLE "=== Test 2: Complex Loop Condition ==="
    counter R 0
    max R 10
    
    IM IN YR test1 UPPIN YR counter WILE BOTH OF SMALLR OF counter AN max AN WIN
        VISIBLE "Counter: " + counter
        temp R counter
        BOTH SAEM temp AN 5
        O RLY?
            YA RLY
                VISIBLE "Reached 5, continuing..."
        OIC
    IM OUTTA YR test1
    
    BTW Test 3: Loop with arithmetic in condition
    VISIBLE "=== Test 3: Arithmetic in Condition ==="
    i R 0
    sum R 0
    max R 10
    
    IM IN YR test2 UPPIN YR i WILE SMALLR OF i AN max
        sum R SUM OF sum AN i
        VISIBLE "i=" + i + ", sum=" + sum
    IM OUTTA YR test2
    
    VISIBLE "Final sum: " + sum
    
    BTW Test 4: NERFIN loop
    VISIBLE "=== Test 4: NERFIN Loop ==="
    counter R 10
    
    IM IN YR test3 NERFIN YR counter TIL BOTH SAEM counter AN 0
        VISIBLE "Counter: " + counter
    IM OUTTA YR test3
    
    BTW Test 5: Loop with type casting
    VISIBLE "=== Test 5: Type Casting in Loops ==="
    i R 0
    temp R "0"
    
    IM IN YR test4 UPPIN YR i WILE SMALLR OF i AN 5
        temp R MAEK i A YARN
        VISIBLE "i=" + i + ", as string: " + temp
    IM OUTTA YR test4
    
    BTW Test 6: Loop with string operations
    VISIBLE "=== Test 6: String Operations in Loops ==="
    i R 1
    result R ""
    max R 4
    
    IM IN YR test5 UPPIN YR i WILE SMALLR OF i AN max
        result R SMOOSH result AN i AN " "
        VISIBLE "Iteration " + i + ": result=" + result
    IM OUTTA YR test5
    
    VISIBLE "Final result: " + result
    
    BTW Test 7: Triple nested loops
    VISIBLE "=== Test 7: Triple Nested Loops ==="
    product R 1
    
    IM IN YR outer2 UPPIN YR i WILE SMALLR OF i AN 2
        IM IN YR middle UPPIN YR j WILE SMALLR OF j AN 2
            IM IN YR inner2 UPPIN YR k WILE SMALLR OF k AN 2
                product R PRODUKT OF product AN SUM OF SUM OF i AN j AN k
                VISIBLE "i=" + i + ", j=" + j + ", k=" + k + ", product=" + product
            IM OUTTA YR inner2
        IM OUTTA YR middle
    IM OUTTA YR outer2
    
    VISIBLE "Final product: " + product
    
    BTW Test 8: Loop with boolean conditions
    VISIBLE "=== Test 8: Boolean Conditions ==="
    flag R WIN
    counter R 0
    
    IM IN YR test6 UPPIN YR counter WILE BOTH OF SMALLR OF counter AN 5 AN flag
        VISIBLE "Counter: " + counter + ", flag: " + flag
        temp R counter
        BOTH SAEM temp AN 3
        O RLY?
            YA RLY
                flag R FAIL
                VISIBLE "Flag set to FAIL"
        OIC
    IM OUTTA YR test6
    
    BTW Test 9: Loop with comparison operations
    VISIBLE "=== Test 9: Comparison Operations ==="
    i R 0
    max R 7
    
    IM IN YR test7 UPPIN YR i WILE BOTH OF SMALLR OF i AN max AN DIFFRINT i AN max
        BOTH SAEM MOD OF i AN 2 AN 0
        O RLY?
            YA RLY
                VISIBLE "Even: " + i
            NO WAI
                VISIBLE "Odd: " + i
        OIC
    IM OUTTA YR test7
    
    BTW Test 10: Loop with WILE and complex expression
    VISIBLE "=== Test 10: Complex WILE Expression ==="
    i R 1
    j R 10
    sum R 0
    
    IM IN YR test8 UPPIN YR i WILE BOTH OF SMALLR OF i AN j AN BIGGR OF SUM OF i AN j AN 5
        sum R SUM OF sum AN i
        VISIBLE "i=" + i + ", j=" + j + ", sum=" + sum
        j R DIFF OF j AN 1
    IM OUTTA YR test8
    
    VISIBLE "Final sum: " + sum
    
    BTW Test 11: Loop with arithmetic operations in body
    VISIBLE "=== Test 11: Arithmetic in Loop Body ==="
    i R 0
    result R 0
    
    IM IN YR test9 UPPIN YR i WILE SMALLR OF i AN 6
        result R SUM OF result AN PRODUKT OF i AN i
        VISIBLE "i=" + i + ", i*i=" + PRODUKT OF i AN i + ", result=" + result
    IM OUTTA YR test9
    
    VISIBLE "Sum of squares: " + result
    
    BTW Test 12: NERFIN with arithmetic
    VISIBLE "=== Test 12: NERFIN with Arithmetic ==="
    counter R 20
    
    IM IN YR test10 NERFIN YR counter TIL SMALLR OF counter AN 10
        VISIBLE "Counter: " + counter + ", Counter/2: " + QUOSHUNT OF counter AN 2
    IM OUTTA YR test10
    
    BTW Test 13: Loop with string concatenation
    VISIBLE "=== Test 13: String Concatenation in Loop ==="
    i R 1
    pattern R ""
    
    IM IN YR test11 UPPIN YR i WILE SMALLR OF i AN 5
        pattern R SMOOSH pattern AN "*"
        VISIBLE "Iteration " + i + ": " + pattern
    IM OUTTA YR test11
    
    BTW Test 14: Nested loops with different loop types
    VISIBLE "=== Test 14: Mixed Loop Types ==="
    i R 0
    j R 5
    
    IM IN YR outer3 UPPIN YR i WILE SMALLR OF i AN 3
        VISIBLE "Outer: " + i
        IM IN YR inner3 NERFIN YR j TIL SMALLR OF j AN 2
            VISIBLE "  Inner: " + j
        IM OUTTA YR inner3
        j R 5
    IM OUTTA YR outer3

KTHXBYE

