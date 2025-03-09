'''
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

 Encoding:
 if the word contains atleast 3 characters, remove the first letter and append it at the end
   now append three random characters at the starting and the end
 else:
   simply reverse the string

 Decoding:
 if the word contains less than 3 characters, reverse it
 else:
   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
 Your program should ask whether you want to code or decode '''
 
msg = input("Enter your message :")
words = msg.split()

code = int(input("(1)for Encoding and (0) for Decoding. What do you want : "))


if(code == 1):
    new = []
    for i in words:
        if(len(i)>=3): 
            s1 = "gtr"
            s2 = "kit"
            news = s1 + i[1:] + i[0] + s2
            new.append(news)
        
        else:
            new.append(i[::-1])
        
    print(" ".join(new))

elif(code == 0):
    newd = []
    for i in words:
        if(len(i)>=3):
            newsd = i[3:-3]
            newsd = newsd[-1] + newsd[:-1]
            newd.append(newsd)
        else:
            newd.append(i[::-1])
    
    print(" ".join(newd)) 