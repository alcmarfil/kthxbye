HAI
    WAZZUP
        I HAS A i
        I HAS A j
        I HAS A choice ITZ "nested"
        I HAS A condition ITZ WIN
        I HAS A counter ITZ 0
    BUHBYE

    BTW Test: Mixed nesting of different flow control statements
    VISIBLE "=== Mixed Flow Control Nesting Demo ==="

    BTW Loop containing conditional containing switch
    i R 0
    IM IN YR outer_loop UPPIN YR i WILE DIFFRINT BIGGR OF i AN 3 AN i
        VISIBLE "Outer loop iteration: " AN i

        BTW Conditional inside loop
        condition
        O RLY?
            YA RLY
                VISIBLE "  Condition is true"

                BTW Switch inside conditional inside loop
                choice
                WTF?
                    OMG "nested"
                        VISIBLE "    Switch case 'nested' matched"
                        j R 0
                        IM IN YR inner_loop UPPIN YR j WILE DIFFRINT BIGGR OF j AN 2 AN j
                            VISIBLE "      Inner loop in switch: " AN j
                        IM OUTTA YR inner_loop
                        GTFO
                    OMG "simple"
                        VISIBLE "    Switch case 'simple' matched"
                        GTFO
                    OMGWTF
                        VISIBLE "    Switch default case"
                OIC

            NO WAI
                VISIBLE "  Condition is false"
        OIC

    IM OUTTA YR outer_loop

    VISIBLE ""
    VISIBLE "=== Complex Nested Structure Complete ==="

KTHXBYE
