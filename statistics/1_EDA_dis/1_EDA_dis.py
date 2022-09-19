# -*- coding: utf-8 -*-

import os
os.chdir(r'D:\cs\data_ml_f\1\1\1cs\data\0\data')

import numpy as np
import pandas as pd


state = pd.read_csv('state.csv')

# <Estimation of Location>

# 1. mean group

# (1)arithmetic mean
# > two ways
state['Population'].mean()

np.mean(state['Population'])
# > handling missing values
np.nanmean(state['Population'])

# (2)geometric mean
# >positive number

# use package scipy.stats
import scipy.stats as stats
stats.gmean(state['Population'])

# (3) trimmed-mean
# >trim=0.1 for each end
stats.trim_mean(state['Population'], 0.1)

# weighted-mean
np.average(state['Murder.Rate'], weights=state['Population'])

# 2. median group

# (1) median
# > two ways
state['Population'].median()

np.median(state['Population'])

# (2) weighted-median

# use package wquantiles
import wquantiles
wquantiles.median(state['Murder.Rate'], weights=state['Population'])

# 3. mode
# > generally not used for numeric data
stats.mode(state['Population'])

#==============================================================================#
#==============================================================================#

# <Estimation of Variability>

# 1. deviation group

# (1) mean absolute deviation
state["Population"].mad()

# (2) variance
# > two ways
# > in pandas, the denominator is n-1
state['Population'].var()

# > in np, the default denominator is n
# > but we can change it
np.var(state['Population'], ddof=1)

# (3) std
# > in Python, it is std,;in R it is sd
# > two ways
# > in pandas, the denominator is n-1
state['Population'].std()

# > in np, the default denominator is n
# > but we can change it
np.std(state['Population'], ddof=1)

# (4) MAD -- median absolute deviation
# > use package statsmodels.robust.scale
from statsmodels.robust.scale import mad
mad(state['Population'])

# 2. order statistics

# (1) range
# > two ways
np.ptp(state['Population'])

state['Population'].max() - state['Population'].min()


# (2) percentile or quantile
state['Population'].quantile(0.5)
# multiple quantile
state['Population'].quantile([0.75, 0.25])

# > np way
np.quantile(state['Population'], q=[0.75, 0.25])

# (3) IQR .75 quantile - .25 quantile
# > two ways
stats.iqr(state['Population'])

state['Population'].quantile(0.75) - state['Population'].quantile(0.25)

# 3. SE, SEM
# define function
def se(df, na=False):
    if na:
        df = df[df.notnull()]
    from math import sqrt
    return sqrt(df.var() / len(df))

se(state['Population'])

# or use the package stats
stats.sem(state['Population'])

#==============================================================================#
#==============================================================================#

# <Estimation of Shape>

# 1. Skewness
# > two ways
state['Population'].skew()

# bias=False --  the calculations are corrected for statistical bias
stats.skew(state['Population'], bias=False)

# 2. Kurtosis
# > two ways
state['Population'].kurtosis()

stats.kurtosis(state['Population'], bias=False)


#==============================================================================#
#==============================================================================#

# Distribution
# there are so many dis. we just can't show them all
# So, we use binomial dis., poisson dis. and normal dis. to do the presentation

# 1. Binomial
# (1) PMF -- x for success num.
stats.binom.pmf(2, 5, 0.1)

# (2) CDF
stats.binom.cdf(2, 5, 0.1)

# (3) generate random numbers from binomial dis.
# > n -- the size you want
# > the returned values are the nums of successes
stats.binom.rvs(size=5, n=10, p=0.1)

# 2. Poisson
# (1) PMF
stats.poisson.pmf(3, 2)

# (2) CDF
stats.poisson.cdf(6, 6)

# (3) random variates
stats.poisson.rvs(size=5, mu=3)

# 3. Normal
# (1) ISF -- quantile?
my_norm_dis = stats.norm(0, 1)
my_norm_dis.isf(0.025)
