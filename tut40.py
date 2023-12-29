# super keyword

# super() gives us access to methods in a super-class from the subclass that inherits from it
class Parent:
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    def child_method(self):
        print("This is child method")
        super().parent_method()
    def parent_method(self):
        print("This is child's parent method")
child_object = Child()
child_object.child_method()
child_object.parent_method()