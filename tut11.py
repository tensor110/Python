# Intrduction to list 

marks=[3,5,8,"Lucky",True]
print(marks)
print(marks[:]) #means[0:len(marks)]
print(marks[:4]) 
print(marks[1:-1])
print(marks[1:4:2])
print(len(marks))
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[-2])  #marks[len(marks)-2]
if "Lucky" in marks:
    print("Yes")
else:
    print("No")

if "uck" in "Lucky":
    print("Yes")
else:
    print("No")

list=[i for i in range(10) if i%2==0]
print(list)