# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
from scipy import stats

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# <Simple Linear Regression>

# 1. case 1
df = pd.read_csv('D:/daily_learning/data_science/statistics/sta/al_to.csv')
result = sm.ols('Alcohol ~ Tobacco', df).fit()
print(result.summary())

# 2. case 2
# Regression Using Sklearn
data = np.matrix(df)

cln = LinearRegression()
org = LinearRegression()

X = np.array(df.iloc[:, 1]).reshape(-1, 1)
Y = np.array(df.iloc[:, 2]).reshape(-1, 1)
cln.fit(Y[:-1], X[:-1])
org.fit(Y, X)

X, Y = data[:,2], data[:,1]
cln.fit(X[:-1], Y[:-1])
org.fit(X, Y)

# adujust R square
clean_score = '{0:.3f}'.format(cln.score(Y[:-1], X[:-1]))
original_score = '{0:.3f}'.format(cln.score(Y, X))

# intercept
cln.intercept_
# coefficient
cln.coef_
