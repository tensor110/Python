# Inheritance 
# Inheritance allows us to inherit the properties of a class i.e. base class to another i.e. derived class.

# Single Inheritance 
# In single inheritance we derive a single base class from the single parent class or the existing class 
class ParentClass:
    pass
class ChildClass(ParentClass):
    pass

# Multiple Inheritance 
# In multiple inheritance we derive a single base class from the multiple parent classes 
class ParentClass1:
    pass
class ParentClass2:
    pass
class ParentClass3:
    pass
class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    pass

# Multi-level Inheritance
# Multilevel Inheritance in Python is a type of Inheritance that involves inheriting a class that has already inherited some other class. 
class ParentClass:
    pass
class ChildClass1(ParentClass):
    pass
class ChildClass2(ChildClass1):
    pass

# Hybrid Inheritance
# It combines multiple inheritances with multilevel inheritance.
class ParentClass:
    pass
class ChildClass1(ParentClass):
    pass
class ChildClass2(ChildClass1):
    pass
class ChildClass3(ChildClass1, ChildClass2):
    pass

# Hierarchical Inheritance 
# If multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance
class ParentClass:
    pass
class ChildClass1(ParentClass):
    pass
class ChildClass2(ParentClass):
    pass
class ChildClass3(ParentClass):
    pass