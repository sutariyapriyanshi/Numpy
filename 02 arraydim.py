import numpy as np

a = np.array(42) # 0-D Array
b = np.array([1, 2, 3, 4, 5]) # 1-D Array
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D Array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3-D Array

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

a = np.array([1, 2, 3, 4], ndmin=5) # creating the array with 5 dimension 

print(a)
print('number of dimensions :', a.ndim)
