# tuples and operations on tuples

# Tuples are immutable 
tup= (1,5,9,35,567,"Lucky",True)
print(tup, type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
if 567 in tup:
    print("Yes")
tup1= tup[1:6:2]
print(tup1)

tuple1=(1,2,3,4,5,3,2,4,3,1)
res=tuple1.count(3)
res=tuple1.index(3)
res=tuple1.index(3,4,8)  #Index of 3 between(4,8)
print(res)