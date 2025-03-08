num = int(input("Enter a number: "))

if(num > 0):
    print("Positive")

elif(num == 0):
    print("Zero")
    
else:
    print("Negative")
    

# Nested if-else

x = int(input("Enter a number: "))
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than 15 ")

elif x < 5:
    if(x > 0):
        print("x is between 0 and 5")   
    else:
        print("x is less than 0")