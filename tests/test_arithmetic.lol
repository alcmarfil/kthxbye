HAI
    WAZZUP
        I HAS A result
    BUHBYE

    BTW Test 1: SUM OF 2 AN 4 (both NUMBR -> NUMBR)
    result R SUM OF 2 AN 4
    VISIBLE "SUM OF 2 AN 4 = " AN result

    BTW Test 2: DIFF OF 4 AN 3.14 (one NUMBAR -> NUMBAR)
    result R DIFF OF 4 AN 3.14
    VISIBLE "DIFF OF 4 AN 3.14 = " AN result

    BTW Test 3: PRODUKT OF "2" AN "7" (both cast to NUMBR -> NUMBR)
    result R PRODUKT OF "2" AN "7"
    VISIBLE "PRODUKT OF 2 AN 7 = " AN result

    BTW Test 4: QUOSHUNT OF 5 AN "12" (both NUMBR -> NUMBR with integer division)
    result R QUOSHUNT OF 5 AN "12"
    VISIBLE "QUOSHUNT OF 5 AN 12 = " AN result

    BTW Test 5: MOD OF 3 AN "3.14" (one NUMBAR -> NUMBAR)
    result R MOD OF 3 AN "3.14"
    VISIBLE "MOD OF 3 AN 3.14 = " AN result

    BTW Test 6: Nested - SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1
    BTW ((3*4)/2)+1 = (12/2)+1 = 6+1 = 7
    result R SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1
    VISIBLE "SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1 = " AN result

    BTW Test 7: Nested - SUM OF SUM OF SUM OF 3 AN 4 AN 2 AN 1
    BTW ((3+4)+2)+1 = (7+2)+1 = 9+1 = 10
    result R SUM OF SUM OF SUM OF 3 AN 4 AN 2 AN 1
    VISIBLE "SUM OF SUM OF SUM OF 3 AN 4 AN 2 AN 1 = " AN result

    BTW Test 8: Test with TROOF (WIN = 1, FAIL = 0)
    result R SUM OF WIN AN 5
    VISIBLE "SUM OF WIN AN 5 = " AN result

    result R SUM OF FAIL AN 3
    VISIBLE "SUM OF FAIL AN 3 = " AN result

    BTW Test 9: Test with NOOB (should cast to 0)
    I HAS A noob_var
    result R SUM OF noob_var AN 10
    VISIBLE "SUM OF NOOB AN 10 = " AN result

    BTW Test 10: Test QUOSHUNT with NUMBAR (should use float division)
    result R QUOSHUNT OF 5.0 AN 2
    VISIBLE "QUOSHUNT OF 5.0 AN 2 = " AN result

KTHXBYE

