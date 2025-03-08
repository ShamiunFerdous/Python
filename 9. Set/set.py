# Creating set with elements
s1 = {1, 2, 3, 4, 5}

# Creating set with mixed data types
s2 = {1.0, "Hello", (1, 2, 3)}  # float, string, and tuple

# Creating set with duplicate elements
s3 = {1, 2, 3, 4, 3, 2}  # Duplicates will be removed

# Creating set from a list (fixed issue)
s4 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  

# Creating an empty set (not "null set")
s5 = set()  

# Printing sets
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


# Printing set elements doesn't follow the order of insertion