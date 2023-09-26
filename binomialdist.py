# Binomial Distribution is a Discrete Distribution.

# Given 10 trials for coin toss generate 10 data points:
from numpy import random

x = random.binomial(n=10, p=0.5, size=10) # n for the number of trials and p for the probability of occurence
print(x)

# Visualization of Binomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False) # it will plot the histogram 
# and kde means kernel density estimate which means KDE represents the data using a continuous probability density 
# curve in one or more dimensions. and here value is false it means the curve is not visible
plt.show()

# Difference Between Normal and Binomial Distribution
# the main difference is that normal distribution is continuos where the binomial is the discrete
#  if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial') # here label shows the label binomial

plt.show()