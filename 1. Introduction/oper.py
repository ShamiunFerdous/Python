# Define two numbers
a = 10
b = 3

# Arithmetic operations
print("Addition:", a + b)        # 10 + 3 = 13
print("Subtraction:", a - b)     # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)        # 10 / 3 = 3.3333
print("Floor Division:", a // b) # 10 // 3 = 3
print("Modulus:", a % b)         # 10 % 3 = 1 (remainder)
print("Exponentiation:", a ** b) # 10^3 = 1000


# 'is' vs '=='
# 'is' is used to compare the memory location of two objects
# '==' is used to compare the values of two objects
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  (values are equal)
print(a is b)  # False (different memory locations)

c = a  # Both variables point to the same object
print(a is c)  # True

# 'in' and 'not in' operators
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # True
print('grapes' not in fruits)  # True

# 'not' operator
print(not True)  # False
print(not False)  # True

