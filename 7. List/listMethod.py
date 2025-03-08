l = [3,4,1,6,3,20,5,7,8,9,10]
print(l)

# Append
l.append(11)
print(l) # Output: [3, 4, 1, 6, 3, 20, 5, 7, 8, 9, 10, 11]

# Insert
l.insert(2, 100)
print(l) # Output: [3, 4, 100, 1, 6, 3, 20, 5, 7, 8, 9, 10, 11]

# Remove
l.remove(100)
print(l) # Output: [3, 4, 1, 6, 3, 20, 5, 7, 8, 9, 10, 11]

# Pop
l.pop()
# remove the last element from the list defaulty.
print(l) # Output: [3, 4, 1, 6, 3, 20, 5, 7, 8, 9, 10]

l.pop(2)
# remove the element from the list based on the index.
print(l) # Output: [3, 4, 6, 3, 20, 5, 7, 8, 9, 10]

# Index
print(l.index(20)) # Output: 4

# Count
print(l.count(3)) # Output: 2

# Sort
l.sort()
print(l) # Output: [3, 3, 4, 5, 6, 7, 8, 9, 10, 20]

# Reverse
l.reverse()
print(l) # Output: [20, 10, 9, 8, 7, 6, 5, 4, 3, 3]

# Copy
l2 = l.copy() # Copy the list
l2.append(100)
print(l2) # Output: [20, 10, 9, 8, 7, 6, 5, 4, 3, 3, 100]


# Extend
m = [1, 2, 3]
n = [4, 5, 6]

m.extend(n)
print(m) # Output: [1, 2, 3, 4, 5, 6]