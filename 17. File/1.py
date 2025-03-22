file = open('hi.txt', 'r')
text = file.read()
print(text)
file.close()

''' File is opened in read mode. The content of the file is read 
and stored in the variable text. The file is closed after reading the content. '''