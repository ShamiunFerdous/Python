tup1 = (1,2,3)
tup2 = (4,5,6)

# Adding elements to a tuple
# We cannot add elements to a tuple. Tuples are immutable.
# Though, we can add two tuples using the + operator to create a new tuple.

tup = tup1 + tup2 # we merge two tuples
print(tup) # Output: (1, 2, 3, 4, 5, 6)

# However, we can do it by converting the tuple to a list, adding elements to the list, 
# and converting the list back to a tuple.

country = ("Italy", "Germany", "USA", "Japan", "Brazil")
c = list(country)
c.append("Turkey")
country = tuple(c)
print(country) # Output: ('Italy', 'Germany', 'USA', 'Japan', 'Brazil', 'Turkey')

# Deleting elements from a tuple
# As discussed above, we cannot change the elements in a tuple.
# That also means we cannot delete or remove items from a tuple.
# But deleting a tuple entirely is possible using the del keyword.

del country
# print(country) # NameError: name 'country' is not defined


# Count and Index
# These two methods are used to count the number of elements in a tuple and
# return the index of a specified element in the tuple.
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1)
print(tup.count(1)) # Output: 5
print(tup.index(5)) # Output: 4

# Membership Test
print(1 in tup) # Output: True
print(11 in tup) # Output: False