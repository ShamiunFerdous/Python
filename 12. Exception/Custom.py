class myexception (Exception):
    def drive(name, age):
        if(age < 18):
            raise myexception(f"{name} is not eligible to drive")
        else:
            print(f"{name} is eligible to drive")
        

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    myexception.drive(name, age)
except myexception as e:
    print("Error occurred: ", e)