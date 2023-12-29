# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
lst = []
s = []
xi = []
r = 0
for i in range(0, x):
    print("Enter shoe size")
    ele = int(input())
    lst.append(ele)
n = int(input())
for i in range(0, n):
    print("Enter shoe size")
    ele1 = int(input())
    s.append(ele1)
    print("Enetr rate")
    ele2 = int(input())
    xi.append(ele2)

print(lst)
print(s)
print(xi)
for j in range(0, n):
    for i in range(0, x):
        if s[j] == lst[i]:
            lst.remove(lst[i])
            print("Respective rate")
            print(xi[j])
            r = r + xi[j]
            x = x-1
print(r)