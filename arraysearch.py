# You can search an array for a certain value, and return the indexes that get a match.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # Find the indexes where the value is 4
print(x) # o/p -> The example above will return a tuple: (array([3, 5, 6],)

# x = np.where(arr%2 == 0)
# x = np.where(arr%2 == 1) # it will check and return index of odd number

# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value
#  would be inserted to maintain the search order. The searchsorted() method is assumed to be used on sorted arrays.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7) # Find the indexes where the value 7 should be inserted
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right') # Find the indexes where the value 7 should be inserted, starting from the right
print(x)

# Multiple Values -> To search for more than one value, use an array with the specified values.

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) # Find the indexes where the values 2, 4, and 6 should be inserted
print(x)