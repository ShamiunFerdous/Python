class Person:
  name = "Shamiun"
  occupation = "Bekar"
  networth = 10
  
  def info(self):
    print(f"{self.name} is a {self.occupation} and has a net worth of {self.networth} Taka.")


a = Person()
b = Person()
c = Person()

a.name = "karim"
a.occupation = "Accountant"
a.networth = 1000000

b.name = "Rahim"
b.occupation = "HR"
b.networth = 2000000


# print(a.name, a.occupation)
a.info()
b.info()
c.info()

# "self" is a reference to the current instance of the class.
# It allows you to access instance variables and methods from within the class. 
# When you call a method on an instance, Python automatically passes 
# the instance as the first argument to the method, allowing you to work with that 
# specific instance's data. In this case, "self" is used to refer to the instance of the
# Person class that is calling the info() method.