# Set and Set Methods
info={"Lucky",19,True,2.3,19}
print(info)
print(type(info))
# To create empty set 
em_set=set()   # em_set={}->This is a empty dictionary
print(type(em_set))
for value in info:
    print(value)

# Union & Update
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
#Intersection & Intersection_update
s1={1,2,5,6}
s2={3,6,7}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)
#Symmetic_difference & Symmetic_difference_update
s1={1,2,5,6}
s2={3,6,7}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1,s2)
# difference & difference_update
s1={1,2,5,6}
s2={3,6,7}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1,s2)
# isdisjoint() 
s1={1,2,5,6}
s2={3,6,7}
print(s1.isdisjoint(s2))
# issuperset() 
s1={1,2,5,6}
s2={3,6,7}
print(s1.issuperset(s2))
# issubset() 
s1={1,2,5,6}
s2={3,6,7}
print(s1.issubset(s2))
# add() and update()
s1={1,2,5,6}
s2={3,6,7}
s1.add(9)  #We can add values to set but do not add sets
print(s1)
s1.update(s2)  #We can updates sets to set but do not update values
print(s1)
# Remove() and discard() 
s1={1,2,5,6}
s1.remove(5)
# s1.remove(10) #error occurs b/c 10 is not in set
s1.discard(1)
s1.discard(10) #In case of dicard error not coming if the element is not in the set
print(s1)
# pop() (pop cuts the last value but we don't knoe which element will be cut because sets are unordered)
s1={1,2,5,6}
item= s1.pop()
print(s1)
print(item)
# del
s1={1,2,5,6}
del s1
# print(s1) #Error occured because s1 is deleted
# clear()
s1={1,2,5,6}
s1.clear()
print(s1)