# Function, function arguments and Recursion

def mean(a,b):
    mean=(a+b)/2
    print(mean)
mean(5,9)

# Default arguments
def mean(a=5,b=9):
    mean=(a+b)/2
    print(mean)
mean(3)  #a=3 and b=9(default)

# Keyword arguments
def mean(a=5,b=9):
    mean=(a+b)/2
    print(mean)
mean(a=1,b=7)

# Required arguments
def mean(a,b=9):  #Here a is required
    mean=(a+b)/2
    print(mean)
mean(a=1)

# Arbitary arguments
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print("average=",sum/len(numbers))
avg(1,2,3,4,5)

def name(**name):
    print("Hello",name['fname'],name['mname'],name['lname'])
name(mname="Brace",fname="hue",lname="Johnathon")

# Return statement 
def mean(a,b):
    mean=(a+b)/2
    return mean
c=mean(5,9)
print(c)

# Recursive Function 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))