# summation in ufunc numpy

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr) # it will return an integer

# Perform summation in the following array over 1st axis

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)
print(newarr) # it will return [6 6] for default the axis is 0 and it return [2 4 6]

# Perform cummulative summation in the following array:

import numpy as np

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr) # return 6
