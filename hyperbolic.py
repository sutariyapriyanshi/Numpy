# Find sinh value of PI/2

# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
import numpy as np

x = np.sinh(np.pi/2)
print(x)

# Find cosh values for all of the values in arr

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

# Find the angle of 1.0:

x = np.arcsinh(1.0) #vFinding Angles
print(x)

# Find the angle for all of the tanh values in array:

arr = np.array([0.1, 0.2, 0.5]) # Angles of Each Value in Arrays
x = np.arctanh(arr)
print(x)