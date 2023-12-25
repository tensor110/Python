# Classes and Objects 
class Person:
    name= 'Lucky'
    occupation= "Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a= Person()
a.name= "Shubham"
a.occupation= "Accountant"
a.info()

b= Person()
b.name= "Nikita"
b.occupation= "HR"
b.info()