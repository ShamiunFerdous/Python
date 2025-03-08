# Empty list
my_list = []

# List with values
fruits = ["apple", "banana", "cherry"]

# List with mixed data types
mixed_list = [10, "hello", 3.14, True]

# Nested list
nested_list = [[1, 2, 3], ["a", "b", "c"]]
print(nested_list)


fruits = ["apple","banana","mango","orange","cherry"]
print(fruits[0]) # Output: apple
print(fruits[-2]) # Output: orange (Negative indexing) means (length - 2)

# Slicing
print(fruits[1:4]) # Output: ['banana', 'mango', 'orange']
print(fruits[:3]) # Output: ['apple', 'banana', 'mango']
print(fruits[2:]) # Output: ['mango', 'orange', 'cherry']

# Change the value of a specific item
fruits[1] = "blackcurrant"
print(fruits) # Output: ['apple', 'blackcurrant', 'mango', 'orange', 'cherry']

# List Comprehension
squares = [i**2 for i in range(10)]
print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube = [i**3 for i in range(10) if i%3 ==  0]
print(cube) # Output: [0, 27, 216, 729]