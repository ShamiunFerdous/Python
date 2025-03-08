# Set union
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {5,0,3,9,19}

print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8} . '|' is the union operator
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8} . union() method

# Set intersection
print(s1 & s2)  # Output: {4, 5} . '&' is the intersection operator
print(s1.intersection(s2))  # Output: {4, 5} . intersection() method



# Set update
s1.update(s2)  # s1 = s1 | s2
print(s1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

s2.intersection_update(s3)  # s2 = s2 & s3
print(s2)  # Output: {5} . intersection_update() method


# Set difference
print(s1 - s2)  # Output: {1, 2, 3, 4, 6, 7, 8} . '-' is the difference operator
print(s1.difference(s2))  # Output: {1, 2, 3, 4, 6, 7, 8} . difference() method
# Set difference means the elements that are only in s1 but not in s2



# Set symmetric difference
s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

print(s1 ^ s2)  # Output: {'banana', 'cherry', 'google', 'microsoft'} . '^' is the symmetric difference operator
print(s1.symmetric_difference(s2))  # Output: {'banana', 'cherry', 'google', 'microsoft'} . symmetric_difference() method
# Symmetric difference means the elements that are in either of the sets but not in both
# (s1 | s2) - (s1 & s2). It means removing the common elements from the union of two sets




# Set isdisjoint
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = {3, 4, 5}

print(s1.isdisjoint(s2))  # Output: True . No common elements
print(s1.isdisjoint(s3))  # Output: False . Common element 3




# Set issubset and issuperset
s1 = {"a", "b", "c", "d", "e"}
s2 = {"c", "d"}
s3 = {"a", "b"}

print(s1.issubset(s2))  # Output: False . s2 is not a subset of s1
print(s2.issubset(s1))  # Output: True . All elements of s2 are in s1
# issubset() method returns that if s2 is a subset of s1 or not


print(s1.issuperset(s2))  # Output: True . s1 is a superset of s2
print(s2.issuperset(s1))  # Output: False . s2 is not a superset of s1
# issuperset() method returns that if s1 is a superset of s2 or not 
# (i.e., all elements of s2 are in s1)



# Set copy
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # Output: {1, 2, 3}
# copy() method returns a shallow copy of the set
# (i.e., it creates a new set and copies all elements of the original set to the new set)



# Set clear
s1.clear()
print(s1)  # Output: set()
# clear() method removes all elements from the set 




# Set add 
sa = {"cat", "dog", "elephant"}
sa.add("fish")
print(sa)  # Output: {'cat', 'dog', 'elephant', 'fish'}
# add() method adds an element to the



# Set remove
sb = {"hen", "goat", "pig"}
sb.remove("pig")
print(sb)  # Output: {'hen', 'goat'}
# remove() method removes the specified element from the set
# If the element is not present in the set, it raises an error
# sb.remove("tiger")  # Output: KeyError: 'tiger'



# Set discard
sc = {"apple", "banana", "cherry"}
sc.discard("banana")
print(sc)  # Output: {'apple', 'cherry'}
# discard() method removes the specified element from the set
sc.discard("tiger")  # Output: {'apple', 'cherry'}
# If the element is not present in the set, it doesn't raise an error


# Set pop
sd = {"apple", "banana", "cherry"}
sd.pop()
print(sd)  # removes a random element from the set



#Set len
se = {"apple", "banana", "cherry"}
print(len(se))  # Output: 3 . len() method returns the number of elements in the set


# Set del
sf = {"apple", "banana", "cherry"}
del sf
# print(sf)  # Output: NameError: name 'sf' is not defined
# del keyword deletes the set completely


#Frozen set
# Frozen set is an immutable version of a set
# It is created using the frozenset() constructor
# It is similar to a set but it cannot be changed
# It doesn't have add(), remove(), or pop() methods
# It doesn't have union, intersection, difference, or symmetric_difference methods
