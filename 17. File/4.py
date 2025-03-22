''' Using 'With' keyword in filr handling 
It closes the file automatically after the block of 
code is executed'''

with open('hi.txt', 'r') as file:
    text = file.read()
    print(text)
# output: Hello World


with open("hello.txt",'w') as file:
    file.write("Hello World")
    
# Now the content of hello.txt is "Hello World"