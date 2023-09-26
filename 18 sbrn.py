# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

import matplotlib.pyplot as plt # importing the pyplot object of the Matplotlib module in your code
import seaborn as sns # importing seaborn module
 
# Plotting a Distplot

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Distplot Without the Histogram

sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # We will be using: sns.distplot(arr, hist=False) to visualize random distributions
# if here True it means histogram is also display 
# but we does not want to use histogram hence value is False
plt.show()
