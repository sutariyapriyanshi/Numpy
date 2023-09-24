#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 2) #split into 2 parts
newarr1 = np.array_split(arr, 4)#If the array has less elements than required, it will adjust from the end accordingly.
print(newarr1)
print(newarr)

# If you split an array into 3 arrays, you can access them from the result just like any array element
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3) #Split the 2-D array into three 2-D arrays
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1) #Split the 2-D array into three 2-D arrays along rows
print(newarr)
