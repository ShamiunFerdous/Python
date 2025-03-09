a = "!!!Hello, World!!!"
b = "why so serious?"

print(a.lower()) # convert all the characters to lower case

print(b.upper()) # convert all the characters to upper case

print(a.strip("!")) # remove all the leading and trailing characters

print(b.replace("?","!"))# replace a character with another character

print(b.capitalize()) # capitalize the first character of the string

print(b.title()) # capitalize the first character of each word

print(b.swapcase()) #  Swaps uppercase to lowercase and vice versa.

print(b.center(50)) # center the string with a specific width

c = "Shamiun Shamiun Shamiun"
print(c.count("Shamiun")) # count the number of occurences of a substring

print(c.find("Shamiun")) # Returns the first index of sub, or -1 if not found

print(c.index("Shamiun")) # Returns the first index of sub, or raises ValueError if not found

d = "S M Shamiun Ferdous"
print(d.split()) # split the string into a list

print(d.split("m")) # split the string into a list with a specific separator
# output: ['S M Sha', 'iun Ferdous']


e = "abcdefg"
f = "12345"
g = "abc123"
print(e.isalpha()) # check if all the characters are alphabets
print(f.isdigit()) # check if all the characters are digits
print(g.isalnum()) # check if all the characters are alphanumeric
print(e.isdigit()) 