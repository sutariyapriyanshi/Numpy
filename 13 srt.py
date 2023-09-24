# Sorting means putting elements in an ordered sequence.

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple']) # sort in alphabetically order
print(np.sort(arr))

arr = np.array([True, False, True]) # sort in boolean order
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]]) # sorting in 2-D array
print(np.sort(arr))
