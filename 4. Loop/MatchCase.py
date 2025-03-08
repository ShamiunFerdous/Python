x = int(input("Enter a number: "))

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")

# The match statement is a more powerful version of the switch statement 
# from other languages.

y = int(input("Enter a number: "))

match y:
    case 1 | 2 | 3:
        print("One or Two or Three")
    case 4 | 5 | 6:
        print("Four or Five or Six")
    case _ if y > 6:
        print("Greater than Six")
    case _: 
        print("Something else")
        
# The match statement can also be used with sequences.
# We can use if else statement in the case block.
    