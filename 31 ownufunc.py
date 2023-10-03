# you add it to your NumPy ufunc library with the frompyfunc() method.
# Create your own ufunc for addition

import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1) # it will add the own function to this using the frompyfunc method
print(myadd([1, 2, 3, 4], [5, 6, 7, 8])) 

print(type(np.add)) # here add is ufunc so it will check and return the type of it

print(type(np.concatenate)) # here this is not an ufunc so it will return other type,like this built-in NumPy function for joining two or more arrays
# If the function is not recognized at all, it will return an error

# Use an if statement to check if the function is a ufunc or not:

import numpy as np

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')
