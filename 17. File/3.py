''' open file in append mode . In this mode we can write
content in the file without overwriting the content. '''
file = open("hello.txt",'a')
file.write("I am fine.")
file.close()

file = open("hello.txt",'r')
text = file.read()
print(text)
file.close()
# output: How are you?I am fine.

