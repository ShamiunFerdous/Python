# Creating dictionary with elements
# Dictionary with key-value pairs
student = {
    "name": "Shamiun",
    "age": 21,
    "department": "CSE",
    "university": "DU"
}
# Here student is a dictionary with four key-value pairs
# Keys are name, age, department, and university
# Values are Shamiun, 21, CSE, and DU respectively
# Keys are unique in a dictionary
# Values can be of any data type

# print(student)
print(student["name"])  # Output: Shamiun
print(student["age"])  # Output: 21
print(student["department"])  # Output: CSE
print(student["university"])  # Output: DU

# Updating dictionary
student["university"] = "University of Dhaka"
print(student["university"])  # Output: University of Dhaka

# Adding new key-value pair
student["roll"] = 42

# Printing Dictionary using loop
for key, value in student.items():
    print(f"{key}: {value}")
    