file = open("hello.txt",'w')
file.write("Hello World")
file.close()

'''Here it create a file first. Then  write "Hello World" in
the file. It is open in write mode. After writing the content
it is closed. '''

file = open("hello.txt",'r')
text = file.read()
print(text)
file.close()
# output: Hello World

file = open("hello.txt",'w')
file.write("How are you?")
file.close()

file = open("hello.txt",'r')
text = file.read()
print(text)
file.close()
# output: How are you?

''' In write mode, it will overwrite the content of the file. 
 Now the content of the file is "How are you?" '''