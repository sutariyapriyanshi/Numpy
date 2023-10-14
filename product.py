# Find the product of the elements of this array

import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x) # 24 because 1*2*3*4 = 24

# Find the product of the elements of two arrays

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x) # 40320 because 1*2*3*4*5*6*7*8 = 40320

# Perform summation in the following array over 1st axis

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr) # [24 1680]

# Take cummulative product of all elements for following array

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr) #  [5 30 210 1680]