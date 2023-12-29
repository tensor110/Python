# Method Overriding 

# When a method in a subclass has the same name, same parametera and same return type as a method in its super-class, then the method in the subclass is said to be override the method in the super-class 

class Parent:
    def __init__(self):
        self.value = "Inside Parent"
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__(self):
        self.value = "Inside Child"
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()