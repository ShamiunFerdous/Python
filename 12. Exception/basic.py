try:
    a = int(input("Enter a number: "))
    print(10//a)
    
except ZeroDivisionError as e:
    print("Error occurred: ", e)

# Output:
# Enter a number: 0
# Error occurred:  division by zero


# Multiple except blocks
try:
    a = int(input("Enter a number: "))
    print(10/a)

except ZeroDivisionError as e:
    print("Error occurred: ", e)
except ValueError as e:
    print("Invalide input: ", e)