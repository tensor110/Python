# Access Modifiers
# Public  Access Modifiers
class Employee:
    def __init__(self):
        self.name = "Lucky"

a = Employee()
print(a.name)

# Private Access Modifiers
class Employee:
    def __init__(self):
        self.__name = "Lucky"

a = Employee()
# print(a.__name)   #Cannot be accessed directly
print(a._Employee__name)   #Can be accessed indirectly

# Protected Access Modifiers
class Employee:
    def __init__(self):
        self._name = "Lucky"

a = Employee()
print(a._name)