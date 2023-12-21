# Loops

# For loops
name="Maheswar"
for i in name:
    print(i)

colors=["red","orange","green","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k)
for k in range(1,9):
    print(k)
for k in range(1,20,2):
    print(k)

# While loops
i=0
while(i<=5):
    print(i)
    i=i+1

# similar of do-while loop 
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

# Loops with else
name="Maheswar"
for i in name:
    print(i)
else:                       #else statement is always executed after loop
    print("Out of loop")

i=0
while(i<=5):
    print(i)
    i=i+1
    if i==3:
        break   #When break statement is appied else condition will not printed
# When the loop complete fully all iterations then the else loop will run
else:
    print("Out of loop")
