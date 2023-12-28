# dir, __dict__, help method

# The dir() function returns a list of all the attributes and methods available for an object.
x = [1,2,3]
print(dir(x))
print(x.__add__)

x = (1,2,3)
print(dir(x))

# __dict__ attribute returns a dictionary representation Of an object's attributes.
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

p= Person("Lucky", 21)
print(p.__dict__)

# The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person))
print(help(str))