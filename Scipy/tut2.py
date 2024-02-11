# Optimizers 

# To find root of an equation root(), uses 2 arguments 'fun', x0
from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot)
print(myroot.x)

# To find minima minimize(), uses 3 arguments 'fun', x0 and method: it also has some legal values: 'CG', 'BFGS', 'NEWTON-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP'.
# eg- minimize the function x^2+x+2 with BFGS
from scipy.optimize import minimize
def eqn(x):
    return x**2+x+2
mymin = minimize(eqn, 0, method= 'BFGS')
print(mymin)
print(mymin.x)