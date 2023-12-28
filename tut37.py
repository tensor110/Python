# Instance variable vs Class Variable 
class Employee:
    companyName = "Apple"   # Class Variable
    id=0
    def __init__ (self, name):
        self.name = name    # Instance Variable
        self.raise_amount= 0.02
        Employee.id +=1
    def showDetails( self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.id} id in {self.companyName} is {self.raise_amount}" )
# Employee. showDetails(emp1)
empl= Employee("Lucky")
empl.raise_amount= 0.3
empl.companyName= "Apple India"   #Changing company name for emp1
empl.showDetails( )

Employee.companyName= "Google"     #Changing company name for all emps
print(Employee.companyName)

emp2= Employee("Rohan")
emp2.showDetails()