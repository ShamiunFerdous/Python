'''filter function is used to filter the given iterables(list,sets etc) with the
help of another function passed as an argument to test all the elements to be 
True or False. Syntax: filter(function,iterables)'''

def is_even(x):
    return x % 2 == 0

l = [1,2,3,4,5,6,7,8,9,10]
result = filter(is_even,l)
print(list(result))  # Output: [2, 4, 6, 8, 10]


# using lambda function
result = filter(lambda x: x%3 == 0,l)
print(list(result))  # Output: [3, 6, 9]