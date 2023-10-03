# Truncate elements of following array

import numpy as np

arr = np.trunc([-3.1666, 3.6667])
print(arr)

# Same example, using fix()

arr = np.fix([-3.1666, 3.6667])
print(arr)

# Round off 3.1666 to 2 decimal places

arr = np.around(3.1666, 2)
print(arr)

# Floor the elements of following array

arr = np.floor([-3.1666, 3.6667])
print(arr)

# Ceil the elements of following array

arr = np.ceil([-3.1666, 3.6667])
print(arr)
