# Interpolation
# It is a method for generating points between the given points and the method of filling the values is called imputation

# 1D interpolation: interp1d()
# here for given xs and ys interpolate values from 2.1, 2.3, 2.3,...., 2.9
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys= 2 * xs + 1
interp_func = interp1d(xs, ys)
arr = interp_func(np.arange(2.1, 3, 0.1))
print(arr)

# spline interpolation 
# here now we will find the univariate spline interpolation for 2.1, 2.3, 2.3,...., 2.9
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys= xs**2 + np.sin(xs) + 1
spline_func = UnivariateSpline(xs, ys)
arr1 = spline_func(np.arange(2.1, 3, 0.1))
print(arr1)

# Interpolation with Radial basis Function(Rbf)
from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys= xs**2 + np.sin(xs) + 1 
rbf_func = Rbf(xs, ys)
arr2 = rbf_func(np.arange(2.1, 3, 0.1))
print(arr2)