HAI
    WAZZUP
        I HAS A name ITZ "Alice"
        I HAS A age ITZ 25
    BUHBYE

    BTW Test VISIBLE with exclamation mark (no newline suppression)
    VISIBLE "Hello " + name + "!" BTW This should print with newline

    BTW Test VISIBLE without exclamation mark (normal behavior)
    VISIBLE "You are " + age + " years old" BTW This should print with newline

    BTW Test VISIBLE with ! at end to suppress newline
    VISIBLE "Counting: " !
    VISIBLE "1, " !
    VISIBLE "2, " !
    VISIBLE "3!"

    VISIBLE "" BTW Empty line for separation

    BTW Another example
    VISIBLE "Progress: [" !
    VISIBLE "25%" !
    VISIBLE "] Complete"

KTHXBYE

