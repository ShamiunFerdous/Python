# A tuple in Python is an immutable ordered collection of elements. 
# It is similar to a list but cannot be modified after creation.

tup = (1, 2, 3, 4, 5) 
print(tup) # Output: (1, 2, 3, 4, 5)

tup[0] = 10 # TypeError: 'tuple' can't be changed

# Creating tuple
t1 = () # Empty tuple
t2 = (1,) # Tuple with single element. Here comma is must.
t3 = (1, 2, 3, 4, 5) # Tuple with multiple elements
t4 = (1, "hello", 3.14, True) # Tuple with mixed data types
t5 = ((1, 2, 3), ("a", "b", "c")) # Nested tuple
t6 = tuple([1, 2, 3, 4, 5]) # Convert list to tuple with tuple() constructor

# Slicing
print(t3[1:4]) # Output: (2, 3, 4)
# When you slice a tuple, Python doesn’t modify the original tuple.
# Instead, Python creates a new tuple containing the sliced elements.
# The original tuple remains unchanged, maintaining its immutability.
