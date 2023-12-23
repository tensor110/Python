# readline() & writelines() method 

f = open("tut25a.txt", "r")
while True:
    line= f.readline()
    if not line:
        break
    print(line)


f = open("tut25b.txt", "r")
i=0
while True:
    i=i+1
    line= f.readline()
    print(line)
    if not line:
        break
    m1= line.split(",")[0]
    m2= line.split(",")[1]
    m3= line.split(",")[2]
    print(f"Marks of student {i} in Maths is {m1}")
    print(f"Marks of student {i} in Phy is {m2}")
    print(f"Marks of student {i} in Chem is {m3}")

f= open("tut25c.txt", "w")
lines= ['line 1\n','line 2\n','line 3\n'] 
f.writelines(lines)
f.close()

f= open("tut25d.txt", "w")
lines= ['line 1','line 2','line 3'] 
for line in lines:
    f.writelines(line + '\n')
f.close()