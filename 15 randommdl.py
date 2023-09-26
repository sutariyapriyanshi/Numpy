# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
# NumPy offers the random module to work with random numbers.

# Generate a random integer from 0 to 100
from numpy import random

x = random.randint(100) # it will display random one number between 0 to 100
print(x)

# The random module's rand() method returns a random float between 0 and 1.
x = random.rand() # Generate a random float from 0 to 1
print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100
x=random.randint(100, size=(5)) # generate 1-D array with size 5 random integer from 0 to 100
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
x = random.randint(100, size=(3, 5)) # here (3,5) tells that 2-D array with 3 array and all with 5 element 
print(x)

# The rand() method also allows you to specify the shape of the array.

x = random.rand(5) # Generate a 1-D array containing 5 random floats
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers
x = random.rand(3, 5)
print(x)

# Return one of the values in an array
x = random.choice([3, 5, 7, 9]) # return any value from array
print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
x = random.choice([3, 5, 7, 9], size=(3, 5)) # generate 2-D array with 3 array and all have 5 elements from given array parameter 
print(x)
