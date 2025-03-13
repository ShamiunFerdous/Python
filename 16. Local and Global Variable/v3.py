# Using local and global variable together 
score = 100  # Global variable

def game():
    bonus = 10  # Local variable
    print("Global score:", score)  # Accessing global variable
    print("Local bonus:", bonus)  # Accessing local variable

game()
# print(bonus)  # ❌ This will cause an error: NameError: name 'bonus' is not defined


#Non-Local variable
def outer():
    x = 5  # Local variable for outer function

    def inner():
        nonlocal x  # Refers to x in outer()
        x += 1
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
