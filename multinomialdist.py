# Multinomial distribution is a generalization of binomial distribution.

# Draw out a sample for dice roll:

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

# Multinomial samples will NOT produce a single value! They will produce one value for each pval.
# where pval is - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).