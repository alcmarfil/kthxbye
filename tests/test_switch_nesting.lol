HAI
    WAZZUP
        I HAS A menu
        I HAS A submenu
        I HAS A action
        I HAS A level
        I HAS A temp
    BUHBYE
    
    BTW ========================================
    BTW Test: Switch Nesting - Extra Credit
    BTW ========================================
    BTW This test demonstrates nested switch statements
    
    VISIBLE "=== Switch Nesting Test ==="
    
    BTW Test 1: Double nested switches
    VISIBLE "Test 1: Double Nested Switches"
    menu R "main"
    submenu R "settings"
    
    menu
    WTF?
        OMG "main"
            VISIBLE "  In main menu"
            submenu
            WTF?
                OMG "settings"
                    VISIBLE "    In settings submenu"
                    GTFO
                OMG "profile"
                    VISIBLE "    In profile submenu"
                    GTFO
                OMGWTF
                    VISIBLE "    Unknown submenu"
            OIC
            GTFO
        OMG "help"
            VISIBLE "  In help menu"
            submenu
            WTF?
                OMG "faq"
                    VISIBLE "    In FAQ"
                    GTFO
                OMG "contact"
                    VISIBLE "    In contact"
                    GTFO
                OMGWTF
                    VISIBLE "    Unknown help option"
            OIC
            GTFO
        OMGWTF
            VISIBLE "  Unknown main menu"
    OIC
    
    VISIBLE ""
    
    BTW Test 2: Triple nested switches
    VISIBLE "Test 2: Triple Nested Switches"
    menu R "level1"
    submenu R "level2"
    action R "level3"
    
    menu
    WTF?
        OMG "level1"
            VISIBLE "  Level 1 selected"
            submenu
            WTF?
                OMG "level2"
                    VISIBLE "    Level 2 selected"
                    action
                    WTF?
                        OMG "level3"
                            VISIBLE "      Level 3 selected - deepest nesting!"
                            GTFO
                        OMG "other"
                            VISIBLE "      Level 3 other option"
                            GTFO
                        OMGWTF
                            VISIBLE "      Level 3 default"
                    OIC
                    GTFO
                OMGWTF
                    VISIBLE "    Level 2 default"
            OIC
            GTFO
        OMGWTF
            VISIBLE "  Level 1 default"
    OIC
    
    VISIBLE ""
    
    BTW Test 3: Nested switches with different case types
    VISIBLE "Test 3: Nested Switches with Mixed Types"
    menu R "1"
    submenu R "optionA"
    
    menu
    WTF?
        OMG "1"
            VISIBLE "  Menu 1 selected"
            submenu
            WTF?
                OMG "optionA"
                    VISIBLE "    Option A in Menu 1"
                    GTFO
                OMG "optionB"
                    VISIBLE "    Option B in Menu 1"
                    GTFO
                OMGWTF
                    VISIBLE "    Default in Menu 1"
            OIC
            GTFO
        OMG "2"
            VISIBLE "  Menu 2 selected"
            submenu
            WTF?
                OMG "optionA"
                    VISIBLE "    Option A in Menu 2"
                    GTFO
                OMG "optionB"
                    VISIBLE "    Option B in Menu 2"
                    GTFO
                OMGWTF
                    VISIBLE "    Default in Menu 2"
            OIC
            GTFO
        OMGWTF
            VISIBLE "  Unknown menu"
    OIC
    
    VISIBLE ""
    
    BTW Test 4: Nested switches with expressions
    VISIBLE "Test 4: Nested Switches with Computed Values"
    level R 1
    temp R SMOOSH "sub" AN level
    
    level
    WTF?
        OMG 1
            VISIBLE "  Level 1"
            temp
            WTF?
                OMG "sub1"
                    VISIBLE "    Submenu 1"
                    GTFO
                OMG "sub2"
                    VISIBLE "    Submenu 2"
                    GTFO
                OMGWTF
                    VISIBLE "    Default submenu"
            OIC
            GTFO
        OMG 2
            VISIBLE "  Level 2"
            temp
            WTF?
                OMG "sub1"
                    VISIBLE "    Submenu 1 in Level 2"
                    GTFO
                OMGWTF
                    VISIBLE "    Default in Level 2"
            OIC
            GTFO
        OMGWTF
            VISIBLE "  Unknown level"
    OIC
    
    VISIBLE ""
    VISIBLE "=== Switch Nesting Test Complete ==="

KTHXBYE
