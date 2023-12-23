# map, Filter and Reduce

# map 
# map(function,iterable)
l=[1,2,4,5,7,8]
map= list(map(lambda x :x*2,l))
print(map)

# Filter
# filter(predictable, iterable) 
def filter_fun(a):
    return a>3
filter= list(filter(filter_fun,l))
print(filter)

# Reduce
# reduce(function,iterable)
from functools import reduce
def mysum(x,y):
    return x+y
sum= reduce(mysum,l)
print(sum)