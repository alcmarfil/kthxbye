HAI
    WAZZUP
        I HAS A temp ITZ 0
        I HAS A x ITZ 3
        I HAS A y ITZ 2
        I HAS A z
        I HAS A num_var ITZ 42
        I HAS A float_var ITZ 3.14
        I HAS A choice ITZ 2
        I HAS A result
    BUHBYE

    temp R 3
    VISIBLE "Temp is " AN temp
    
    z R ALL OF BOTH OF x AN y MKAY
    
    VISIBLE "Testing type change:"
    VISIBLE "num_var before: " AN num_var
    num_var IS NOW A YARN
    VISIBLE "num_var after IS NOW A YARN: " AN num_var
    
    VISIBLE "float_var before: " AN float_var
    float_var IS NOW A NUMBR
    VISIBLE "float_var after IS NOW A NUMBR: " AN float_var
    
    temp IS NOW A TROOF
    VISIBLE "temp after IS NOW A TROOF: " AN temp
    
    VISIBLE ""
    VISIBLE "=== Testing Conditionals (O RLY?) ==="
    
    BTW Test 1: Simple conditional with expression before O RLY?
    BOTH SAEM choice AN 2
    O RLY?
        YA RLY
            VISIBLE "Choice is 2!"
        NO WAI
            VISIBLE "Choice is not 2"
    OIC
    
    BTW Test 2: Conditional with MEBBE blocks
    BOTH SAEM choice AN 1
    O RLY?
        YA RLY
            VISIBLE "Choice is 1"
        MEBBE BOTH SAEM choice AN 2
            VISIBLE "Choice is 2"
        MEBBE BOTH SAEM choice AN 3
            VISIBLE "Choice is 3"
        NO WAI
            VISIBLE "Choice is something else"
    OIC
    
    VISIBLE ""
    VISIBLE "=== Testing Switch (WTF?) ==="
    
    BTW Test 3: Switch with expression before WTF?
    choice
    WTF?
        OMG 1
            VISIBLE "Case 1 matched!"
            GTFO
        OMG 2
            VISIBLE "Case 2 matched!"
            GTFO
        OMG 3
            VISIBLE "Case 3 matched!"
            GTFO
        OMGWTF
            VISIBLE "Default case - no match"
    OIC
    
    BTW Test 4: Switch with variable expression
    SUM OF choice AN 1
    WTF?
        OMG 3
            VISIBLE "Sum is 3!"
            GTFO
        OMG 4
            VISIBLE "Sum is 4!"
            GTFO
        OMGWTF
            VISIBLE "Sum is something else: " AN SUM OF choice AN 1
    OIC
KTHXBYE