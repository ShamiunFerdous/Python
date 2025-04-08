class student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
    
    def info(self):
        print(f"name: {self.name}, age: {self.age}, roll: {self.roll}")


a = student("Shamiun", 20, 101)
b = student("Karim", 21, 102)

a.info()
b.info()

'''
The __init__() method is a special method in Python classes.
It is called a constructor and is used to initialize the attributes of 
an object when it is created.'''