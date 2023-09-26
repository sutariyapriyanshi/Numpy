# Randomly shuffle elements of following array:

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# The shuffle() method makes changes to the original array.
random.shuffle(arr) # random module have shuffle method to shuffle the element 
print(arr)

# Generate a random permutation of elements of following array:

arr = np.array([1, 2, 3, 4, 5])
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
print(random.permutation(arr)) # it will generate the permutation of the array
# work same as shuffle method
