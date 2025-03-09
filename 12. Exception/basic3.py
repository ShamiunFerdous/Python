try:
    a = int(input("Enter a number:"))
    
    print(10//a)

except(ZeroDivisionError, ValueError) as e:
    print("Error occurred: ", e)


# Handling multiple exceptions using a single except block