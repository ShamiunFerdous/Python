def greet():
    print("Hello, world!")

greet()  # Calling the function


# Required Arguments
def avarage(a,b):
    print((a+b)/2)

avarage(10,20)  # Output: 15.0

#DEFAULT ARGUMENTS
def greet(name ="Shamiun", msg="Good morning!"):
    print("Hello", name + ', ' + msg)

greet() # Output: Hello Shamiun, Good morning!
greet("Papon") # Output: Hello Papon, Good morning!
greet("Papon", "How do you do?") # Output: Hello Papon, How do you do?
greet(msg="How do you do?", name="Papon") # Output: Hello Papon, How do you do?
greet(msg = "How are you?") # Output: Hello Shamiun, How are you?



# Arbitrary Arguments
def add(*number): # *number is a tuple
    sum = 0
    for i in number:
        sum += i
       
    return sum

print(add(10,20,30,30,50))

def avg(**number): # **number is a dictionary
    sum = 0
    for i in number.values():
        sum += i
       
    return sum/len(number)

print(avg(a=10,b=20,c=30,d=30,e=50))



# Keyword Arguments
def greet(name, msg):
    print("Hello", name + ', ' + msg)
    

        
    
