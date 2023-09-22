import numpy as np

# 1-D Array accessing 
a = np.array([1, 2, 3, 4])
print(a[0])

# 2-D Array accessing 
b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', b[0, 1])

# 3-D Array accessing 
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c[0, 1, 2])

# Negative indexing 
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) # last element of array
print('Last element from 2nd dim: ', arr[1, -2]) # len = 5 so 5-2 now array is 3