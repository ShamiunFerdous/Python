#type() function is used to get the type of an object

# Numeric Types
a = 10        # int
b = 3.14      # float
c = complex(2,3)    # complex
print(a,b,c,type(a),type(b),type(c))


# Sequence Types
name = "Shamiun"  # str
numbers = [1, 2, 3]  # list
coordinates = (4, 5) # tuple
print(name,numbers,coordinates,type(name),type(numbers),type(coordinates))

# Mapping Type
person = {"name": "Shamiun", "age": 21}  # dict
print(person,type(person))

# Set Types
unique_numbers = {1, 2, 3}# set
print(unique_numbers,type(unique_numbers))

# Boolean Type
is_student = True  # bool
print(is_student,type(is_student))

# None Type
nothing = None  # None
print(nothing,type(nothing))
