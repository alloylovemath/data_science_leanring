# -*- coding: utf-8 -*-

import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# <ANOVA>

# 1. one-factor ANOVA
# (1) case 1
# > Source: Chen's book
group_1 = np.array([390, 410, 372, 385])
group_2 = np.array([375, 348, 354, 364, 362])
group_3 = np.array([413, 383, 408])

F_statistic, pVal = stats.f_oneway(group_1, group_2, group_3)

# more detialed version
df_group_1 = pd.DataFrame(
    {"Value": group_1, "Treatment": "1"}
)
df_group_2 = pd.DataFrame(
    {"Value": group_2, "Treatment": "2"}
)
df_group_3 = pd.DataFrame(
    {"Value": group_3, "Treatment": "3"}
)

df = pd.concat([df_group_1, df_group_2, df_group_3], ignore_index=True)

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
model = ols('Value ~ C(Treatment)', df).fit()
anovaResults = anova_lm(model)
print(anovaResults)

# (2) case 2
# > source: book1
data_path = "D:/daily_learning/data_science/\
statistics/material/ISP/Code_Quantlets/\
08_TestsMeanValues/anovaOneway/altman_910.txt"

data = np.genfromtxt(data_path, delimiter=',')

df = pd.DataFrame(data, columns=['value', 'treatment'])    
model = ols('value ~ C(treatment)', df).fit()
anovaResults = anova_lm(model)
print(anovaResults)

#==============================================================================#

# 2. Kruskal–Wallis test
from scipy.stats.mstats import kruskalwallis

city1 = np.array([68, 93, 123, 83, 108, 122])
city2 = np.array([119, 116, 101, 103, 113, 84])
city3 = np.array([70, 68, 54, 73, 81, 68])
city4 = np.array([61, 54, 59, 67, 59, 70])

kruskalwallis(city1, city2, city3, city4)

#==============================================================================#

# 3. two-factor ANOVA

# (1) case 1
# > source: Chen's book (no interaction)
data = np.array([
    [292, 1, 1],
    [316, 1, 2],
    [325, 1, 3],
    [310, 2, 1],
    [318, 2, 2],
    [317, 2, 3],
    [320, 3, 1],
    [318, 3, 2],
    [310, 3, 3],
    [370, 4, 1],
    [365, 4, 2],
    [330, 4, 3]
])

df = pd.DataFrame(data, columns=['value', 'species', 'breed'])

formula = "value ~ C(species) + C(breed)"

lm = ols(formula, df).fit()
anovaResults = anova_lm(lm)

anovaResults

# (2) case 2 (interaction)
# > book1
data_path = "D:/daily_learning/data_science/statistics/\
material/ISP/Code_Quantlets/8_TestsMeanValues/anovaTwoway/altman_12_6.txt"

data = np.genfromtxt(data_path, delimiter=',')
df = pd.DataFrame(data, columns=['hs', 'fetus', 'observer'])

# interaction
formula = 'hs ~ C(fetus) + C(observer) + C(fetus):C(observer)'
lm = ols(formula, df).fit()
anovaResults = anova_lm(lm)

anovaResults
