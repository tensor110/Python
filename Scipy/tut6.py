# Scipy Matlab Arrays: 
# Used for exporting data in matlab format

# For exporting data we use savemat(). It has 3 parameters: filename, mdict, do_compression 
# eg: Export array as avriable name "vec" to mat file 

import numpy as np
from scipy import io
array = np.arange(10)
io.savemat("tut6.mat", {"vec": array})

# For importing existing mat file, it has 1 argument i.e. filename
array_new = io.loadmat('tut6.mat', squeeze_me = True)  # Squeeze_me is used to convert the 2-D array into 1-D array
print(array_new)
print(array_new['vec'])