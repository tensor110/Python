# if-else conditional, match-case statements, break & continue
a=int(input("Enter your age"))
if(a<18):
    print("You can't drive")
elif(a==18):
    print("You can drive from next year")
else:
    print("You can drive")

x=int(input("Enter a number"))
match x:
    case 0:
        print("x= 0")
    case 3:
        print("x= 3")
    # for default
    case _:
        print("x=",x)

for i in range(10):
    if(i==3):
        continue  # Skip the iteration
    elif(i==7):
        break  # Skip the loop
    print(i)

# short hand if-else
a=33
b=333
print("A") if a>b else print("=") if a==b else print("B")