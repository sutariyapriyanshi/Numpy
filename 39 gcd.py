# Find the HCF of the following two numbers

import numpy as np

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x) # 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).

# Find the GCD for all of the numbers in the following array

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x) # 4 because that is the highest number all values can be divided by.
