a = int(input("Enter your age:"))

if(a < 18):
    raise ValueError("You are not eligible to vote")

else:
    print("You are eligible to vote")


# with function.

def divide(a,b):
    if(b == 0):
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a/b

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(divide(a,b))