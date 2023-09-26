
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# it will generate the 1-D array with using element 3,5,7,9 and with including the probability which is given it means 9 probability is 0.0
#  hence it will not occur single time
print(x)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)) # 2-D array with 3 array and 5 element each
print(x)