# Lamda functions 
def double(x):
    return x*2
print(double(10))

double= lambda x: x*2
print(double(10))

avg= lambda x,y,z: (x+y+z)/3
print(avg(2,4,6))

def app(fn,value):
    return 6+fn(value)
print(app(double,5))
print(app(lambda x:x*x,5))