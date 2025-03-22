'''reduce function is used to apply a particular function passed in its 
argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.'''

from functools import reduce

def comp(x, y):
    return x > y

def even(x, y):
    # Check if both numbers are even, if so, return the larger of the two
    if x % 2 == 0 and y % 2 == 0:
        return max(x, y)
    # If one is not even, continue with the next number
    return x if x % 2 == 0 else y

l = [1, 2, 3, 4, 5] 

# Find the largest even number using reduce
result = reduce(even, l)
print(result)  # Output: 4 

result = reduce(comp, l)
print(result)  # Output: False 
