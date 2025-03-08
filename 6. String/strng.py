FirstName = "Shamiun"
LastName  = "Ferdous"
name = FirstName + " " + LastName

# Concatenation
print(FirstName + " " + LastName)

# Repetition
print(FirstName * 3)


a = "hello"
b = "world"

c = a + " " + b
print(len(c)) # Length of the string "hello world"

#indexing
print(c[0]) # h
print(name[3]) # m 
print(c[-1]) # d if index with a negative number(-i), it means (string length - i). 

#slicing
# Syntax: string[i:j] where i is the starting index including and j is 
# the ending index excluding
print(c[0:4]) # hell
print(c[:5]) # hello
print(c[6:]) # world
print(c[:]) # hello world
print(c[-5:]) # world
print(c[-5:-1]) # worl


