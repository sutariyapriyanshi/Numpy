# Exponential distribution is used for describing time till next event e.g. failure/success etc.

# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:

from numpy import random

x = random.exponential(scale=2, size=(2, 3))
print(x)

# Visualization of Exponential Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time 
# between these events.
