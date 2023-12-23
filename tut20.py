# How Import Works

import math
print(math.sqrt(9))

# from keyword 
from math import sqrt,pi
res= sqrt(9)*pi
print(res)

# importing everything 
from math import *

# The "as" keyword
import math as m
print(m.sqrt(9))
print(m.pi)

# The "dir" function
import math
print(dir(math))  # Output will be a list of all the names defined in the amth module
print(type(math.nan))

from tut20ref import welcome, lucky
welcome()
print(lucky)