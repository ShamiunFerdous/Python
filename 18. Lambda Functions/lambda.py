'''Lambda Function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax:
lambda arguments : expression'''

sum = lambda a,b : a+b
print(sum(10,20))  # Output: 30


square = lambda x : x*x
print(square(3))  # Output: 9

avg = lambda a,b,c : (a+b+c)/3
print(avg(10,20,30))  # Output: 20.0
