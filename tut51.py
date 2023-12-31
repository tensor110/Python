# Function Caching 

# Function caching allows us to cache the return values of a function depending on the arguments.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func(n):
    time.sleep(5)
    return n*n
print(func(1))
print("Done for 1")
print(func(2))
print("Done for 2")
# Due to caching code will execute faster
print(func(1))
print("Done for 1")
print(func(2))
print("Done for 2")
# Code will wait for 5 sec because for 3 function is not cached 
print(func(3))
print("Done for 3")