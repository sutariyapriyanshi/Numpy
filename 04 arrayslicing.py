import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a[4:])

b = np.array([1, 2, 3, 4, 5, 6, 7])
print(b[:4])

# negative slicing
c = np.array([1, 2, 3, 4, 5, 6, 7])
print(c[-3:-1])

# Return every other element from index 1 to index 5
d = np.array([1, 2, 3, 4, 5, 6, 7])
print(d[1:5:2])

# Return every other element from the entire array
e = np.array([1, 2, 3, 4, 5, 6, 7])
print(e[::2])

# From the second element, slice elements from index 1 to index 4 (not included)
f = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f[1, 1:4])

# From both elements, return index 2
g = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(g[0:2, 2])

# slice index 1 to index 4 (not included), this will return a 2-D array
h = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(h[0:2, 1:4])
