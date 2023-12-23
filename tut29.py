# is vs ==
# is operator compares the identity (location in the memory) of the objects 
# == compares the value 
a = 5
b = 5
print(a is b)
print(a == b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)