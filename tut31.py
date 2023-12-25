# Constructors 
class Person:
    def __init__(self,n,o):
        print("Hey")
        self.name= n
        self.occ= o
        print(f"{self.name} is a {self.occ}")
        print(f"{n} is a {o}")

a= Person("Lucky", "Developer")
b= Person("Divya","HR")
