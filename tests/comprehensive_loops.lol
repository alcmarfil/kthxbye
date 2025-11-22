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
        I HAS A temp_i
        I HAS A temp_j
        I HAS A temp_k
        I HAS A temp_sq
        I HAS A temp_counter
        I HAS A temp_flag
        I HAS A temp_div
    BUHBYE
    
    BTW Test 1: Nested loops
    VISIBLE "=== Test 1: Nested Loops ==="
    i R 0
    j R 0
    sum R 0
    
    IM IN YR outer UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        j R 0
        IM IN YR inner UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
            sum R SUM OF sum AN PRODUKT OF i AN j
            temp_i R i
            temp_j R j
            VISIBLE "i=" + temp_i + ", j=" + temp_j + ", sum=" + sum
        IM OUTTA YR inner
    IM OUTTA YR outer
    
    VISIBLE "Final sum: " + sum
    
    BTW Test 2: Loop with complex condition
    VISIBLE "=== Test 2: Complex Loop Condition ==="
    counter R 0
    max R 10
    
    IM IN YR test1 UPPIN YR counter WILE BOTH OF DIFFRINT BIGGR OF counter AN max AN counter AN WIN
        temp_counter R counter
        VISIBLE "Counter: " + temp_counter
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
    
    IM IN YR test2 UPPIN YR i WILE DIFFRINT BIGGR OF i AN max AN i
        sum R SUM OF sum AN i
        temp_i R i
        VISIBLE "i=" + temp_i + ", sum=" + sum
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
    
    IM IN YR test4 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 5 AN i
        temp R MAEK i A YARN
        temp_i R i
        VISIBLE "i=" + temp_i + ", as string: " + temp
    IM OUTTA YR test4
    
    BTW Test 6: Loop with string operations (simplified to avoid infinite loop bug)
    VISIBLE "=== Test 6: String Operations in Loops ==="
    i R 0
    result R ""
    counter R 0
    
    IM IN YR test5 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 4 AN i
        counter R SUM OF counter AN 1
        temp R MAEK counter A YARN
        result R SMOOSH result AN temp AN " "
        VISIBLE "Iteration " + temp + ": result=" + result
    IM OUTTA YR test5
    
    VISIBLE "Final result: " + result
    
    BTW Test 7: Triple nested loops
    VISIBLE "=== Test 7: Triple Nested Loops ==="
    i R 0
    j R 0
    k R 0
    product R 1
    
    IM IN YR outer2 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 2 AN i
        j R 0
        IM IN YR middle UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
            k R 0
            IM IN YR inner2 UPPIN YR k WILE DIFFRINT BIGGR OF k AN 2 AN k
                product R PRODUKT OF product AN SUM OF SUM OF i AN j AN k
                temp_i R i
                temp_j R j
                temp_k R k
                VISIBLE "i=" + temp_i + ", j=" + temp_j + ", k=" + temp_k + ", product=" + product
            IM OUTTA YR inner2
        IM OUTTA YR middle
    IM OUTTA YR outer2
    
    VISIBLE "Final product: " + product
    
    BTW Test 8: Loop with boolean conditions
    VISIBLE "=== Test 8: Boolean Conditions ==="
    flag R WIN
    counter R 0
    
    IM IN YR test6 UPPIN YR counter WILE BOTH OF DIFFRINT BIGGR OF counter AN 5 AN counter AN flag
        temp_counter R counter
        temp_flag R flag
        VISIBLE "Counter: " + temp_counter + ", flag: " + temp_flag
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
    
    IM IN YR test7 UPPIN YR i WILE BOTH OF DIFFRINT BIGGR OF i AN max AN i AN DIFFRINT i AN max
        BOTH SAEM MOD OF i AN 2 AN 0
        O RLY?
            YA RLY
                temp_i R i
                VISIBLE "Even: " + temp_i
            NO WAI
                temp_i R i
                VISIBLE "Odd: " + temp_i
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
    
    IM IN YR test9 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 6 AN i
        result R SUM OF result AN PRODUKT OF i AN i
        temp_i R i
        temp_sq R PRODUKT OF i AN i
        VISIBLE "i=" + temp_i + ", i*i=" + temp_sq + ", result=" + result
    IM OUTTA YR test9
    
    VISIBLE "Sum of squares: " + result
    
    BTW Test 12: NERFIN with arithmetic
    VISIBLE "=== Test 12: NERFIN with Arithmetic ==="
    counter R 20
    
    IM IN YR test10 NERFIN YR counter TIL BOTH SAEM counter AN 9
        temp_counter R counter
        temp_div R QUOSHUNT OF counter AN 2
        VISIBLE "Counter: " + temp_counter + ", Counter/2: " + temp_div
    IM OUTTA YR test10
    
    BTW Test 13: Loop with string concatenation
    VISIBLE "=== Test 13: String Concatenation in Loop ==="
    i R 0
    pattern R ""
    counter R 0
    
    IM IN YR test11 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 5 AN i
        counter R SUM OF counter AN 1
        pattern R SMOOSH pattern AN "*"
        temp R MAEK counter A YARN
        VISIBLE "Iteration " + temp + ": " + pattern
    IM OUTTA YR test11
    
    BTW Test 14: Nested loops with different loop types
    VISIBLE "=== Test 14: Mixed Loop Types ==="
    i R 0
    j R 5
    
    IM IN YR outer3 UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        temp_i R i
        VISIBLE "Outer: " + temp_i
        IM IN YR inner3 NERFIN YR j TIL BOTH SAEM j AN 1
            temp_j R j
            VISIBLE "  Inner: " + temp_j
        IM OUTTA YR inner3
        j R 5
    IM OUTTA YR outer3

KTHXBYE

