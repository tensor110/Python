import cmath
import math as m
x = complex(input())
a = x.real
b = x.imag
z1 = abs(complex(a,b))
z2 = cmath.phase(complex(a,b))
print(z1)
print(z2)