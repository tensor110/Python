# Class Methods
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company= newCompany

e1 = Employee()
e1.name= "Lucky"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)   # with classmethod it gives Tesla but without classmethod the output is apple

# class method as alternative constructors 
class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1= Employee("Lucky",120000)
print(e1.name)
print(e1.salary)

string= "Rohan-20000"
e2= Employee.fromStr(string)   # The class method split the string
print(e2.name)
print(e2.salary)