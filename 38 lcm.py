# Find the LCM of the following two numbers

import numpy as np

num1 = 4 # first number
num2 = 6 # second number
x = np.lcm(num1, num2)
print(x) # 12 because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12)

# Find the LCM of the values of the following array

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x) # 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).

# Find the LCM of all values of an array where the array contains all integers from 1 to 10

arr = np.arange(1, 11) # it will arrange the all element from 1 to 11 means 10 element
x = np.lcm.reduce(arr) # finding the lcm form 1 to 10
print(arr)
print(x)
