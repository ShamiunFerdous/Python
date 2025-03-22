''' map function is used to apply a function to all the elements
of a sequence. It returns a new list with the elements changed by the function. 
Syntax: map(function, sequence)'''

def square(x):
    return x*x

l = [1,2,3,4,5]
result = map(square,l)
print(list(result))  # Output: [1, 4, 9, 16, 25]

# using lambda function

result = map(lambda x : x**3,l)
print(list(result))  # Output: [1, 8, 27, 64, 125]