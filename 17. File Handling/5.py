with open("file.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.write("Line 4\n")

with open("file.txt", "w") as file:
    line =['Mango\n', 'Banana\n', 'Apple\n']
    
    file.writelines(line)

with open("file.txt", "r") as file:
    text = file.read()
    print(text)
# output: Mango
# Banana
# Apple

'''writeLines() method is used to write a list of strings to a file.
It does not add a newline character to the end of the string.'''