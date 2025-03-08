'''
Typecasting is the process of converting one data type to another data type.
There are two types of typecasting:
1. Implicit Typecasting
2. Explicit Typecasting

'''
#Explicit Typecasting
#You manually convert a variable from one type to another using built-in functions.
a = 2
b = str(a) # int to string
print(a,type(a),b,type(b))

x = "hello"
y = int(x)
# print(x,type(x),y,type(y)) 
# This will give error because string can't be converted to integer
# This will work if x is a number in string format like "5"

m = "123"
n = int(m) # string to int
print(m,type(m),n,type(n))


# Implicit Typecasting
# Python automatically converts one data type to another data type.
# This is also known as coercion.
# This is done when an operator is applied to two operands of different types.
# The operand with the "lower" type is converted to the "higher" type.

c = 2 # int
d = 3.5 # float

e = c + d # float (Python converts int to float)

print(c,type(c),d,type(d),e,type(e))


