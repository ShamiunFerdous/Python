''' An f-string (formatted string literal) in Python is a way to embed expressions 
inside string literals using curly braces {}. It is prefixed with f or F 
before the opening quote of the string.'''

# Example 1
FirstName = "Shamiun"
LastName  = "Ferdous"
age  = 21

print(f"My nam is {FirstName} {LastName}. I am {age} years old.")

# Math
x = 10
y = 5
print(f"Sum: {x + y} , Substraction: {x-y}, Type : {type(x+y)}")  # Output: Sum: 15 Substraction: 5


# Function calling inside of a f-string
def greet(name):
    return f"Hello, {name}"

print(f"greet({"Shamiun"})")  # Output: Hello, Shamiun


# Using methods inside of a f-string
name = "shamiun Ferdous"
print(f"Uppercase: {name.upper()}, Title: {name.title()}")
#output: Uppercase: SHAMIUN FERDOUS, Title: Shamiun Ferdous


# numbers formating
pie = 3.14159265359
print(f"Value of pie:{pie:.4f}") # Output: Value of pie:3.1416