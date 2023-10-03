# Find log at base 2 of all elements of following array

import numpy as np

arr = np.arange(1, 10)
print(np.log2(arr))

# Find log at base 10 of all elements of following array

arr = np.arange(1, 10)
print(np.log10(arr))

# Find log at base e of all elements of following array:

arr = np.arange(1, 10)
print(np.log(arr))

# NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() 
# with two input parameters and one output parameter

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
