# Global variables can be accessable from any where of the program.

name = "Shamiun"  # Global variable

def show_name():
    print("My name is", name)  # Accessing global variable inside function

show_name()  # Output: My name is Shamiun
print(name)  # Output: Shamiun



# Modifying a global variable
counter = 0  # Global variable

def increment():
    global counter  # Using global keyword to modify it
    counter += 1
    print("Inside function:", counter)

increment()  # Output: Inside function: 1
print("Outside function:", counter)  # Output: 1


'''By default, if you try to modify a global variable 
inside a function without global, Python will treat 
it as a new local variable instead of modifying the existing 
global variable. This leads to unexpected behavior or errors.'''

x = 50  # Global variable

def test():
    x = 10  # Local variable (shadows global x)
    print("Inside function:", x)

test()  # Output: Inside function: 10
print("Outside function:", x)  # Output: 50
