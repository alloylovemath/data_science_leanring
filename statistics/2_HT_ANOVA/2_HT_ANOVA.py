# -*- coding: utf-8 -*-

# <Normality check>

import scipy.stats as stats
import numpy as np

norm_dis = stats.norm(0, 3)
norm_sample = norm_dis.rvs(1000)

erlang_sample = stats.erlang(3).rvs(1000)

# 1. graph
# (1) QQ-Plot
# > use package statsmodels.api
import statsmodels.api as sm
from matplotlib import pyplot as plt

# line="s" -- standardized line
fig = sm.qqplot(norm_sample, line="s")
plt.show()

# (2) PP-plot
# > Ah, I don't see a solution...
# > a "may be" useful way is
# calculate the mean and std of the sample
mean_s = norm_sample.mean()
std_s = norm_sample.std(ddof=1) # ddof=0

pp_plot = sm.ProbPlot(norm_sample, stats.norm(mean_s, std_s)).ppplot(line='45')
plt.show()

# (3) Probability plot
# > QQ-plot -- quantile vs. quantile
# > probability plot-- quantile(x-axis) vs. prob.
prob_plot = stats.probplot(norm_sample, plot=plt)
plt.show()

# 2. statistic test

# (1) Shapiro-Wilk test
# > The p-value is greater than 0.05. Hence, the distribution of the given data
# is not different from normal distribution significantly.
stats.shapiro(norm_sample)

# (2) Lilliefors-test
from statsmodels.stats.diagnostic import lilliefors
lilliefors(norm_sample)

# (3) Kolmogorov-Smirnov test
stats.kstest((norm_sample-np.mean(norm_sample))/np.std(norm_sample,ddof=1),
            'norm')

# (4) D'Agostino–Pearson omnibus test
stats.normaltest(norm_sample)


#==============================================================================#
#==============================================================================#

# <Hypothesis Tests>

# 1. Cases

# book1 page 126, H0 -- mean = 110
scores = np.array([109.4, 76.2, 128.7, 93.7, 85.6,
                   117.7, 117.2, 87.3, 100.3, 55.1])

# --step 1: check normality
fig = sm.qqplot(scores, line="s")
plt.show()

stats.normaltest(scores)
# so, we can assume scores comes from a norm population
# and we don't know the std

# --step 2: do t test
# > the way I learned in the math lecture is a little different from the book1
# > (not so different...). so I display two ways here
# --- way 1: set significant level(0.05), define the critical region
# finally, check the mean falls into which region

# accept region
from math import sqrt

right_side = (sqrt(1 / len(scores)) *
                scores.std(ddof=1) * stats.t(len(scores) - 1).ppf(0.975)) + 110
# here, sqrt(1 / len(scores)) * scores.std(ddof=1) = stats.sem(scores)

left_side = -(sqrt(1 / len(scores)) *
                scores.std(ddof=1) * stats.t(len(scores) - 1).ppf(0.975)) + 110

critical_region = [left_side, right_side]
critical_region # the outcome is [94.1306168164536, 125.8693831835464]

# check the mean
scores.mean() # the result is 97.11999999999999, so wo accept H0

# ---way 2: book1's way
# > t statistic
tval = (110-np.mean(scores)) / stats.sem(scores)

# > calculate the p value
t_dis = stats.t(len(scores)-1)

p = 2 * t_dis.sf(tval) # sf -- 1 - CDF, tval > 0 -- sf, tval < 0 -- cdf
p # 0.09953843652790623 greater than 0.05, so we accept H0

# Actually, there is a more convenient way
stats.ttest_1samp(scores, 110)

# 2. Power
from statsmodels.stats import power

# > case on the book of mr.Chen
from statsmodels.stats import power

nobs = power.normal_sample_size_one_tail(
            alpha=0.05, power=0.95, diff=0.5, std_null=1, std_alternative=1)
nobs

# > for t-test (two sample)
nobs = power.tt_ind_solve_power(effect_size = 0.5, alpha =0.05, power=0.8)
nobs


#==============================================================================#
#==============================================================================#

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

# 2. Kruskal–Wallis test
from scipy.stats.mstats import kruskalwallis

city1 = np.array([68, 93, 123, 83, 108, 122])
city2 = np.array([119, 116, 101, 103, 113, 84])
city3 = np.array([70, 68, 54, 73, 81, 68])
city4 = np.array([61, 54, 59, 67, 59, 70])

kruskalwallis(city1, city2, city3, city4)

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
