HAI
    WAZZUP
        I HAS A choice
        I HAS A subchoice
        I HAS A input
        I HAS A result
        I HAS A counter
        I HAS A temp
    BUHBYE
    
    BTW Test 1: Basic switch with arithmetic in cases
    VISIBLE "=== Test 1: Basic Switch ==="
    choice R "calc"
    input R "10"
    
    choice
    WTF?
        OMG "calc"
            VISIBLE "Calculator mode"
            VISIBLE SUM OF MAEK input A NUMBR AN 5
            GTFO
        OMG "exit"
            VISIBLE "Exiting..."
            GTFO
        OMGWTF
            VISIBLE "Unknown command"
    OIC
    
    BTW Test 2: Nested switches
    VISIBLE "=== Test 2: Nested Switches ==="
    choice R "menu1"
    subchoice R "sub1"
    
    choice
    WTF?
        OMG "menu1"
            VISIBLE "In menu1"
            subchoice
            WTF?
                OMG "sub1"
                    VISIBLE "In submenu1"
                    GTFO
                OMG "sub2"
                    VISIBLE "In submenu2"
                    GTFO
                OMGWTF
                    VISIBLE "Unknown submenu"
            OIC
            GTFO
        OMG "menu2"
            VISIBLE "In menu2"
            GTFO
        OMGWTF
            VISIBLE "Unknown menu"
    OIC
    
    BTW Test 3: Switch with complex expressions in cases
    VISIBLE "=== Test 3: Complex Expressions ==="
    counter R 0
    temp R SMOOSH "test" AN counter
    
    temp
    WTF?
        OMG "test0"
            VISIBLE "Matched test0"
            counter R SUM OF counter AN 1
            GTFO
        OMG "test1"
            VISIBLE "Matched test1"
            GTFO
        OMG "test2"
            VISIBLE "Matched test2"
            GTFO
        OMGWTF
            VISIBLE "No match"
    OIC
    
    BTW Test 4: Switch with operations in case values
    VISIBLE "=== Test 4: Operations in Cases ==="
    input R "5"
    result R SMOOSH "result" AN PRODUKT OF MAEK input A NUMBR AN 2
    
    result
    WTF?
        OMG "result10"
            VISIBLE "Result is 10"
            GTFO
        OMG "result20"
            VISIBLE "Result is 20"
            GTFO
        OMGWTF
            VISIBLE "Result: " + result
    OIC
    
    BTW Test 5: Switch with type casting
    VISIBLE "=== Test 5: Type Casting ==="
    choice R MAEK 1 A YARN
    
    choice
    WTF?
        OMG "1"
            VISIBLE "Matched string '1'"
            GTFO
        OMG "2"
            VISIBLE "Matched string '2'"
            GTFO
        OMGWTF
            VISIBLE "No match for: " + choice
    OIC
    
    BTW Test 6: Multiple cases without GTFO (fall-through simulation)
    VISIBLE "=== Test 6: Multiple Cases ==="
    counter R 0
    temp R "case1"
    
    temp
    WTF?
        OMG "case1"
            VISIBLE "Case 1 executed"
            counter R SUM OF counter AN 1
            GTFO
        OMG "case2"
            VISIBLE "Case 2 executed"
            counter R SUM OF counter AN 2
            GTFO
        OMG "case3"
            VISIBLE "Case 3 executed"
            counter R SUM OF counter AN 3
            GTFO
        OMGWTF
            VISIBLE "Default case"
            counter R 999
    OIC
    
    VISIBLE "Final counter: " + counter
    
    BTW Test 7: Switch with boolean operations
    VISIBLE "=== Test 7: Boolean Operations ==="
    input R "yes"
    temp R BOTH OF BOTH SAEM input AN "yes" AN WIN
    
    BTW Convert boolean to string for switch
    choice R MAEK temp A YARN
    
    choice
    WTF?
        OMG "WIN"
            VISIBLE "Boolean was WIN"
            GTFO
        OMG "FAIL"
            VISIBLE "Boolean was FAIL"
            GTFO
        OMGWTF
            VISIBLE "Unexpected boolean value"
    OIC
    
    BTW Test 8: Switch with empty string and special cases
    VISIBLE "=== Test 8: Edge Cases ==="
    choice R ""
    
    choice
    WTF?
        OMG ""
            VISIBLE "Empty string matched"
            GTFO
        OMG " "
            VISIBLE "Space matched"
            GTFO
        OMGWTF
            VISIBLE "No match for empty string"
    OIC
    
    BTW Test 9: Switch with concatenated strings
    VISIBLE "=== Test 9: String Concatenation ==="
    input R "hello"
    temp R SMOOSH input AN " " AN "world"
    
    temp
    WTF?
        OMG "hello world"
            VISIBLE "Matched concatenated string"
            GTFO
        OMG "hello world!"
            VISIBLE "Matched alternative string"
            GTFO
        OMGWTF
            VISIBLE "No match: " + temp
    OIC
    
    BTW Test 10: Switch with numeric strings
    VISIBLE "=== Test 10: Numeric Strings ==="
    result R MAEK 42 A YARN
    
    result
    WTF?
        OMG "42"
            VISIBLE "Matched numeric string 42"
            GTFO
        OMG "0"
            VISIBLE "Matched zero"
            GTFO
        OMGWTF
            VISIBLE "No match: " + result
    OIC

KTHXBYE

