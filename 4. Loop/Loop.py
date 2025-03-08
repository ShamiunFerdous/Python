for i in range(1, 11):
    print(i)
    
    if(i == 5):
        print("THIS IS SPECIAL")
        break
    
for num in range(10):
    if num == 5:
        break  # Stops the loop when num is 5
    
    print(num)


x = 0
while (x < 5):
    print(x)
    x += 1  # Increment x

x = 5
while(x > 0):
    print(x)
    x -= 1  # Decrement x

for i in range(5):
    print(i)
    # It will print 0, 1, 2, 3, 4.

for i in range(1, 6, 2):
    print(i)
    # It will print 1, 3, 5. It will start from 1 and increment by 2.


# Nested loop
for i in range(3):
    for j in range(2):
        print(i, j)