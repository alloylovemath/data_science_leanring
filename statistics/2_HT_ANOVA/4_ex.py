# -*- coding: utf-8 -*-

'''
This is my solution for the exercise of book1 in Chapter 9
'''

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.style.use('seaborn')

import math

# (1)
data = np.array([
    [3, 1],
    [1, 3]
])

r1 = np.sum(data[0])
r2 = np.sum(data[1])

c1 = np.sum(data[:, :1])
c2 = np.sum(data[:, 1:])

stats.fisher_exact(data, alternative='greater')

# > more detailed way
hypergeom_dis = stats.hypergeom(r1+r2, r1 ,c1)
2 * hypergeom_dis.sf(3)

# (2)
# (2).1
data = np.array([
    [36, 14],
    [30, 25]
])

Z, p, dof, expected = stats.chi2_contingency(data)
print(p)

# (2).2
data = np.array([
    [36, 14],
    [29, 26]
])

# with Yates correction
Z, p, dof, expected = stats.chi2_contingency(data)
print(p)

# without Yates correction
Z, p, dof, expected = stats.chi2_contingency(data, correction=False)
print(p)

# (3)
data = np.array([4, 6, 14, 10, 16])

stats.chisquare(data)

# (4).1
data = np.array([
    [19, 1],
    [6, 14]
])

from statsmodels.stats.contingency_tables import mcnemar

print(mcnemar(data, exact=True))

# (4).2
data = np.array([
    [20, 0],
    [6, 14]
])

print(mcnemar(data, exact=True))
