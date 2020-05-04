"""
CTEC 121
<Garrett>
<Mod 3 Lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    '''
    # conditional expressions

    # literal
    print("\nBoolean Literals\n")
    print(True)
    print(False)
    print(type(True))
    print()

    # relational operators
    print("Relational Operators\n")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("Using Variables\n")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    # Simple If Statements
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("End Simple If Example")
    print()

    # If/Else Statement
    print("If/Else Statement\n")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6
    print ("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    print("End If/Else Example")
    print()

    # Exercise 3-1
    print("Exercise\n")
    for i in range(1,11,1):
        if (i % 2) == 0:
            outputString = "Even"
        else:
            outputString = "Odd"
        print(i, outputString)
    print("End Exercise")
    print()

    # Alphabetize Names
    name = "Bill"
    firstLetterOfName = "B"

    print("Multi-way If Example\n")
    if firstLetterOfName == "A":
        print("A")
    elif firstLetterOfName == "B":
        print("B")
    elif firstLetterOfName == "C":
        print("C")
    # ...
    elif firstLetterOfName == "Y":
        print("Y")
    else:           # Default Case: Name starts with "Z"
        print("Z")
    print()
    '''
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting.\n")
        exit()

main()    