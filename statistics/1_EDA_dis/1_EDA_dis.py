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
# So, we use normal dis. and t dis. to do the presentation

# 1. Normal
norm_dis = stats.norm()
# > loc -- mean, scale -- std
norm_dis_1 = stats.norm(loc=2, scale=3)

# (1) density
norm_dis_1.pdf(5)

# (2) CDF
norm_dis_1.cdf(1)

# (3) sf = 1 - CDF
norm_dis_1.sf(1)

# (4) ppf - inverse of CDF
norm_dis.ppf(0.975)
norm_dis_1.ppf(norm_dis_1.cdf(1))

# (5) ISF - inverse of SF
# > get the 1 - probability, use ppf to get the value
norm_dis.isf(0.025)

# (6) RVS
norm_dis.rvs(10)

# 2. t-dis.
t_dis = stats.t(df=5)

# (1) density
t_dis.pdf(t_dis.ppf(0.95))

# (2) CDF
t_dis.cdf(t_dis.ppf(0.95))

# (3) sf = 1 - CDF
t_dis.sf(t_dis.ppf(0.95))

# (4) ppf - inverse of CDF
t_dis.ppf(0.95)

# (5) ISF - inverse of SF
# > get the 1 - probability, use ppf to get the value
t_dis.isf(0.05)

# (6) RVS
t_dis.rvs(10)
