student = {
    "name": "Shamiun",
    "age": 21,
    "department": "CSE",
    "university": "DU"
}

# Dictionary copy
studentCopy = student.copy()
print(studentCopy)

# Dictionary clear
student.clear()
print(student) # It will print an empty dictionary


# Dictionary get
student = {
    "name": "Shamiun",
    "age": 21,
    "department": "CSE",
    "university": "DU"
}

print(student.get("name"))  # Output: Shamiun
print(student.get("roll"))  # Output: None
# get() method returns the value of the specified key
# If the key is not present in the dictionary, it returns "None"


# Dictionary items
print(student.items())
# items() method returns  dictionary's key-value tuple pairs
# dict_items([('name', 'Shamiun'), ('age', 21), ('department', 'CSE'), ('university', 'DU')])


# Dictionary keys and values
print(student.keys())
# keys() method returns the keys of the dictionary 

print(student.values())
# values() method returns the values of the dictionary


# Dictionary pop
student.pop("age") 
print(student)
# pop() method removes the specified key and its value from the dictionary
# It returns the value of the removed key
# If the key is not present in the dictionary, it raises an error


# Dictionary popitem
student.popitem()
print(student)
# popitem() method removes the last inserted key-value pair from the dictionary
# It returns the removed key-value pair as a tuple
# If the dictionary is empty, it raises an error


# Deleting dictionary
mark = {
    "math": 90,
    "physics": 85,
    "chemistry": 80
}
del mark
# print(mark)  # Output: NameError: name 'mark' is not defined
# del keyword deletes the dictionary completely 