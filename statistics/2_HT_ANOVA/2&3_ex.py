# -*- coding: utf-8 -*-

'''
This is my solution for the exercise of book1 in Chapter 8
'''

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.style.use('seaborn')

import math

# (1)
energy_intake = np.array([5260., 5470., 5640., 6180., 6390.,
                          6515., 6805., 7515., 7515., 8230., 8770.])

# > way 1: calculate directly
# > we use the absolute value, if not, we may need to judge the value first
tval = abs(math.sqrt(len(energy_intake))
        * (np.mean(energy_intake) - 7725) / np.std(energy_intake, ddof=1))
t_dis = stats.t(df=len(energy_intake) - 1)
# > two side
pval = 2 * t_dis.sf(tval)
pval

# > way 2
stats.ttest_1samp(energy_intake, 7725)

# andWilcoxon signed rank sum test
# Page 678
stats.wilcoxon(energy_intake-7725)

# another way?
stats.wilcoxon(energy_intake, np.ones_like(energy_intake) * 7725)

# (2)
lazy_weights = np.array([76, 101, 66, 72, 88,
                         82, 79, 73, 76, 85,
                         75, 64, 76, 81, 86.])

sport_weights = np.array([64, 65, 56, 62, 59,
                          76, 66, 82, 91, 57,
                          92, 80, 82, 67, 54])

stats.ttest_ind(lazy_weights, sport_weights)

# (3)
# We use normaltest to do the job
stats.normaltest(lazy_weights)
stats.normaltest(sport_weights)

# (4)
stats.mannwhitneyu(lazy_weights, sport_weights)

# (5)
data = pd.read_excel('D:/daily_learning/1.xls',
                     skiprows=[0, 1]).iloc[:, [4,5]]
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

model = ols('weight ~ C(group)', data).fit()
anova_lm(model)

# (6)
from statsmodels.stats import multicomp

mc = multicomp.MultiComparison(data['weight'], data['group'])
mc.tukeyhsd().summary()
mc.groupsunique

# (7)
g_a = data['weight'][data['group']=='TreatmentA']
g_b = data['weight'][data['group']=='TreatmentB']
g_c = data['weight'][data['group']=='Control']

stats.kruskal(g_c, g_a, g_b)
