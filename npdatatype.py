import numpy as np

arr = np.array([1, 2, 3, 4]) #integer datatype
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry']) #string datatype

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S') #Create an array with data type string

print(arr)
print(arr.dtype)

# Create an array with data type 4 bytes integer

arr = np.array([1, 2, 3, 4], dtype='i4') # integer datatype with size 4

print(arr)
print(arr.dtype)

# Change data type from float to integer by using 'i' as parameter value

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i') #astype is used to change datatype

print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)