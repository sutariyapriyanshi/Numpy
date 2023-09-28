# Chi Square distribution is used as a basis to verify the hypothesis.

# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3

from numpy import random

x = random.chisquare(df=2, size=(2, 3)) # where df is the degree of freedom
print(x)

# Visualization of Chi Square Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()