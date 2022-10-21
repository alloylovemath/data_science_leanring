# -*- coding: utf-8 -*-

from unittest import result
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

import scipy.stats as stats

# (1)

# read the data
AvgTemp = pd.read_excel('data/AvgTemp.xls')

Year = AvgTemp['year'].values
AvgTmp = AvgTemp['AvgTmp'].values

# get the Pearson's correlation
stats.pearsonr(Year, AvgTmp)

# get the Spearman's rho
stats.spearmanr(Year, AvgTmp)

# get the Kendall's tau
stats.kendalltau(Year, AvgTmp)


# (2)
import statsmodels.formula.api as smf

resTMP = smf.ols('AvgTmp ~ year', data=AvgTemp).fit()

print(resTMP.summary())

# (3)
stats.kstest(resTMP.resid, 'norm')
