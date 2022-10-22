# -*- coding: utf-8 -*-

from unittest import result
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# <case 1>

'''
Our first example comes from book2
it actually is the example of Ch.11
for detail of the data, you can refer to the book.
'''

# load the data
deny = pd.read_csv('data/logit_1.csv')
deny.head()

# (1) try OLS first on deny and pi_rat
# the effect of parameters in fit is the same as 'r' in stata
# use the robust standard error -- clustered standard error
# it's hard to find this method, so, thanks to

'''
source:
https://stackoverflow.com/questions/59831733/
regression-standard-error-clustering-and-robust-to-heteroskedascity-serial-aut
'''

import statsmodels.formula.api as smf

resCase1_linear = smf.ols("deny ~ pi_rat", data=deny).fit()
print(resCase1_linear.summary())

# (2) try logit model on deny and pi_rat and black
resCase1_logit = smf.logit("deny ~ pi_rat + C(black)",
                            data=deny).fit(cov_type='cluster',
                            cov_kwds={'groups': deny.index})
print(resCase1_logit.summary())

# (3) try to replace the outcome in book2(on page 410, col (2))
formula_logit_case1 = "deny ~ black + pi_rat + hse_inc + ltv_med + ltv_high \
                        + ccred + mcred + pubrec + denpmi + selfemp"

Case1_logit_m = smf.logit(formula_logit_case1, data=deny)
resCase1_logit_m = Case1_logit_m.fit(
    cov_type='cluster', cov_kwds={'groups': deny.index}
)
print(resCase1_logit_m.summary())
'''
well, I have to admit that the result is slightly different from the books
but... yes, very slightly.
'''

#==============================================================================#

# (4) try logit model on deny and pi_rat
resCase1_logit_2 = smf.logit("deny ~ pi_rat", data=deny).fit(
    cov_type='cluster', cov_kwds={'groups': deny.index}
)
print(resCase1_logit_2.summary())

# (5) let's try the way on book1
from statsmodels.genmod.families import Binomial

resCase1_logit_3 = smf.glm("deny ~ pi_rat", data=deny, family=Binomial()).fit(
    cov_type='cluster', cov_kwds={'groups': deny.index}
)
print(resCase1_logit_3.summary())

# now let's try the challenger's data
challenger_data = pd.read_csv('data/challenger_data.csv')

resCase_cha = smf.logit("fail ~ Tmp", data=challenger_data).fit()
print(resCase_cha.summary())

#==============================================================================#

'''
Ah, there is a solution from book1, which gives the same result.
But I don't know exactly what it is doing.
I may write an e-mail to the author for some help?
And if you know, please tell me.

What I don't understand is the 'glm' part.
And, anyway, repect to those brave astronauts.
'''

challenger_data = np.genfromtxt('data/challenger_data2.csv',
    skip_header=1,usecols=[1, 2], missing_values='NA',delimiter=',')

# Eliminate NaNs
challenger_data = challenger_data[~np.isnan(challenger_data[:, 1])]

# Create a dataframe, with suitable columns for the fit
df = pd.DataFrame()
df['temp'] = np.unique(challenger_data[:,0])
df['failed'] = 0
df['ok'] = 0
df['total'] = 0
df.index = df.temp.values
# Count the number of starts and failures
for ii in range(challenger_data.shape[0]):
    curTemp = challenger_data[ii,0]
    curVal = challenger_data[ii,1]
    df.loc[curTemp,'total'] += 1
    if curVal == 1:
        df.loc[curTemp, 'failed'] += 1
    else:
        df.loc[curTemp, 'ok'] += 1
# fit the model
# --- >>> START stats <<< ---
model = smf.glm('ok + failed ~ temp', data=df, family=Binomial()).fit()
# --- >>> STOP stats <<< ---
print(model.summary())

#==============================================================================#
