# -*- coding: utf-8 -*-

from unittest import result
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# <linear correlation>

# 1. Pearson's correlation

# (1) for two variables
from scipy import stats

correlation_sample_1 = np.genfromtxt('data/altman_11_1.txt', delimiter=',')
x = correlation_sample_1[:, 0]
y = correlation_sample_1[:, 1]

# the results are (pearson, p-value)
res_pearson = stats.pearsonr(x,y)
res_pearson

# CI of the pearson
res_pearson.confidence_interval()

# (2) correlation matrix
etfs = pd.read_csv('data/etfs.csv')

etfs.corr(method='pearson')

# 2. robust "correlation"'s

# (1) Spearman's rho
stats.spearmanr(x, y)

# (2) Kendall's tau
stats.kendalltau(x, y)

#==============================================================================#
#==============================================================================#

# <general linear models>

# 1. regression
# (1) Noisy Quadratic Polynomial
# This example shows how to use the I() function

# get the data
x_1 = np.arange(100)
y_1 = 150 + 3 * x_1 + 0.03 * (x_1 ** 2) + 5 * np.random.randn(len(x_1))

df = pd.DataFrame({'x': x_1, 'y': y_1})

import statsmodels.formula.api as smf

# pay attention to 'I()' here
# In pasty, '**' already has a meaning -- produce interaction effects.
# But what we want is power - the python default meaning.
# So, we use 'I()' to get what we want - back to the default python meaning.
res2F = smf.ols('y_1 ~ x_1 + I(x_1 ** 2)', data=df).fit()

res2F.summary()

# (2) example for further discussion
AT = pd.read_csv('data/AT.csv')
resAT = smf.ols('Alcohol ~ Tobacco', AT).fit()
print(resAT.summary())

#==============================================================================#
#==============================================================================#

# <Model coefficients and their interpretation>

# 1. Coefficients
# Only for simple linear regression

tobacco = AT['Tobacco'].values
alcohol = AT['Alcohol'].values
design_matrix_AT_T = np.vstack((np.ones_like(tobacco), tobacco)).T

# np.linalg.lstsq
# Return the least-squares solution to a linear matrix equation.
params_AT = np.linalg.lstsq(design_matrix_AT_T, alcohol)

params_AT[0]

# 2. Standard errors of coefficients
design_matrix_AT = np.matrix(np.vstack((np.ones_like(tobacco), tobacco)))

C = np.linalg.inv(design_matrix_AT * design_matrix_AT.T)
C = C * resAT.mse_resid
SE = np.sqrt(C)
SE

# 3. t-Statistic and its p-value
param_tobacco = resAT.params[1]
se_tobacco = SE[1, 1]
t_tobacco = param_tobacco / se_tobacco
t_tobacco

# p-value
N = resAT.nobs
k = resAT.df_model + 1
dof_resid_AT = N - k

# the t-statistic is positive here, we shall use CDF.
# if it is negative, we shall use survival function.
p_tobacco_oneside = 1 - stats.t(dof_resid_AT).cdf(t_tobacco)

# we are doing two-side HT
p_tabacco_twoside = p_tobacco_oneside * 2
p_tabacco_twoside

# 4. CI
z_tabacco = stats.t(dof_resid_AT).ppf(0.975)

CI_AT_tobacco = np.array([param_tobacco - z_tabacco * se_tobacco,
                          param_tobacco + z_tabacco * se_tobacco])

#==============================================================================#
#==============================================================================#

# <Assessment of the Regression>

# 1. R square
ssr_AT = resAT.ssr
tss_AT = resAT.centered_tss

R_2_AT = 1 - (ssr_AT / tss_AT)
R_2_AT

# 2. adjusted R square
mse_res_AT = resAT.mse_resid
mse_tot_AT = resAT.mse_total

adjust_R2_AT = 1 - (mse_res_AT / mse_tot_AT)
adjust_R2_AT

# 3. F-test
mes_mod_AT = resAT.mse_model

F_AT = mes_mod_AT / mse_res_AT
F_AT

# p-value

# get the Dof of the model
dof_model_AT = resAT.df_model

p_F_AT = 1.0 - stats.f.cdf(F_AT, dof_model_AT, dof_resid_AT)
p_F_AT

# 4. Log-Likelihood
# 5. AIC and BIC
'''
Sorry, but I think the necessity of calculte this is small...
'''

#==============================================================================#
#==============================================================================#

# <Analysis of Residuals>

# 1. Skewness and Kurtosis:
skew_AT = stats.skew(resAT.resid, bias=True)
kurt_AT = stats.kurtosis(resAT.reside, fisher=False, bias=True)

[skew_AT, kurt_AT]

# 2. Omnibus Test
stats.normaltest(resAT.resid)

# 3. Durbin–Watson test
from statsmodels.stats.stattools import durbin_watson
durbin_watson(resAT.resid)

# 4. Jarque–Bera test
stats.jarque_bera(resAT.resid)

# 5. Condition Number
X_conn = np.matrix(np.vstack((np.ones(tobacco.size), tobacco)))
EV_X_conn = np.linalg.eig(X_conn * X_conn.T)

CN_AT = np.sqrt(EV_X_conn[0].max() / EV_X_conn[0].min())
CN_AT
