# Magic/ Dunder Method

# Magic methods are special methods in python that have double underscores on both sides of the method name 
# Magic methods are predominantly used for operator overloading

class Employee:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"The name of Employee is {self.name} str"
    def __repr__(self):
        return f"The name of Employee is {self.name} repr"
    def __call__(self):
        print("Call method is called")

e = Employee("Ram")
print(len(e))
print(e)
print(str(e))
print(repr(e))
e()