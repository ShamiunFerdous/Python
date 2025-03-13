def greet():
    message = "Hello, Shamiun!"  # Local variable
    print(message)

greet()
# print(message)  # ❌ This will cause an error: NameError: name 'message' 
# is not defined


def func1():
    x = 5  # Local variable for func1
    print("Func1:", x)

def func2():
    x = 10  # Different local variable for func2
    print("Func2:", x)

func1()  # Output: Func1: 5
func2()  # Output: Func2: 10
