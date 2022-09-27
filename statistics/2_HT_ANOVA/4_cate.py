# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy.stats as stats
import math

# <Chi-square test>

# 1. one-way test

# (1) case 1
# > source: Chen's book
# > by default, the expect situation is equally likely
data = np.array([6, 3, 6])
stats.chisquare(data)

# (2) case 2
# > source: book1
data = np.array([10, 6, 5, 4, 5, 3])
stats.chisquare(data)

# 2. contingency table
data = np.array([
    [63, 37, 60],
    [16, 17, 8],
])

Z, p, dof, expected = stats.chi2_contingency(data)
print(p)

#==============================================================================#

# <Fisher’s Exact Test>
# 1. case 1
# source: José Unpingco's book
data = np.array([
    [13, 11],
    [12, 1]
])

r1 = np.sum(data[0])
r2 = np.sum(data[1])

c1 = np.sum(data[:, :1])
c2 = np.sum(data[:, 1:])

# position 1 - total number
# position 3 - select sample size
# position 2 - belongs to row 1
hypergeom_dis = stats.hypergeom(r1 + r2, r1, c1)
hypergeom_dis.cdf(13)

stats.fisher_exact(data, alternative='less')

# 2. case 2
# source: book1
data = np.array([
    [3, 1],
    [1, 3]
])

r1 = np.sum(data[0])
r2 = np.sum(data[1])

c1 = np.sum(data[:, :1])
c2 = np.sum(data[:, 1:])

hypergeom_dis = stats.hypergeom(r1 + r2, r1, c1)

# 'greater' we use sf
# 2, because we want the prob. of 3 involved
hypergeom_dis.sf(2)

stats.fisher_exact(data, alternative='greater')

#==============================================================================#

# <McNemar’s Test>
# Source: book1(I noticed that there is a same example in Wikipedia)
# Besides, the mcnemar function seem should be import from a different place
from statsmodels.stats.contingency_tables import mcnemar

data = np.array([
    [101, 121],
    [59, 33]
])

# in these version or mcnemar function, 
# the correction is 1(Edward’s correction)
# So the results differ a bit
print(mcnemar(data, exact=False, correction=True))

# I also tried the code on book1, besides, I view the source code of the mcnemar
# function in statsmodels.sandbox.stats.runs
# the correction is also 1

#==============================================================================#

# <Cochran’s Q Test>
# Source: book1
# > The code on the book is wrong
data = np.array([
    [0, 1, 0],
    [1, 1, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1],
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

from statsmodels.stats.contingency_tables import cochrans_q

print(cochrans_q(data))
