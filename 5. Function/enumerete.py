''' The enumerate() function in Python is used to iterate over 
a sequence (like a list, tuple, or string) while keeping track of the 
index of each element. It returns an enumerate object, which produces 
pairs containing an index and the corresponding element from the sequence.'''

fruits = ['apple','banana','cherry']
for index,fruits in enumerate(fruits):
    print(index,fruits)


# custom indexing
fruits = ['apple','cherry','banana']
for index, fruits in enumerate(fruits, start = 1):
    print(index,fruits)
    


# using it with tuple
color = ('red','green','blue')
for index,color in enumerate(color,start = 1):
    print(f"{index}.{color}")
    


# Converting enumerate into a list
numbers = [10, 20, 30]
indexed_numbers = list(enumerate(numbers, start=100))
print(indexed_numbers)
