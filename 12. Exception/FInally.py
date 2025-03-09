try:
    print("Hello World")
    a = int(input("Enter a number: "))
    print(10//a)

except ZeroDivisionError as e:
    print("Error occurred: ", e)

finally:
    print("Finally block executed")


# The finally block is executed no matter what happens in the try block.
# The finally block is used to clean up the resources.
# The finally block is executed even if an exception occurs in the try block.