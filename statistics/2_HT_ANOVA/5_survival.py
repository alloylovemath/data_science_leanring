# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# <Weibull Dis.>

import scipy.stats as stats

'''
The Weibull dis. in scipy.stats is Weibull_min.
One thing we shall pay attention to is that
the pdf of Weibull_min is slightly different from the
pdf we introduced of the pdf in the Wikipedia
it only need to specify k, and lambda is 1
to change the lambda(scale parameter) we shall define the scale
'''

Weibull_test = stats.weibull_min(c=1.5, scale=2)

# (1) draw the graph of Weibull dis.
x = np.linspace(Weibull_test.ppf(0.01),
                Weibull_test.ppf(0.99),100)

fig, ax = plt.subplots(1, 1)

ax.plot(x, Weibull_test.pdf(x), 'r-')

# (2) fit the Weibull dis.

# get some sample data
Weibull_test1 = stats.weibull_min(1.5)
sample_weibull = Weibull_test1.rvs(500)

# fit the parameter
fitPar = stats.weibull_min.fit(sample_weibull)

# there are three params. in fitPar
# [0]-shape parameter;
# [1]-loc parameter, 
# where the x begins, maybe draw a picture will help you understand);
# [2]-scale parameter;
fitPar

# <Kaplan–Meier survival curve>

# (1) draw the curve

from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter

# get the sample data(provide by the lifelines.datasets library)
data_waltons = load_waltons()

T = data_waltons["T"]
E = data_waltons["E"]
groups = data_waltons["group"]

ix = (groups == 'miR-137')

kmf = KaplanMeierFitter()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# The ~ operator is used to invert a general condition.
# For example, here T[~ix] means data in T which are not belong to 'miR-137'
kmf.fit(T[~ix], E[~ix], label='control')
kmf.plot(ax=ax)

kmf.fit(T[ix], E[ix], label='miR-137')
kmf.plot(ax=ax)


# (2) Compare two curves using logrank_test

from lifelines.statistics import logrank_test

results = logrank_test(T[ix], T[~ix], event_observed_A=E[ix],
                       event_observed_B=E[~ix])
results
# if the p-value is less than 0.05, we shall reject the null hypothesis here
# which is that the lifetime of the two groups are the same

# <Cox Proportional Hazards Model>
'''
you can see the detail of this case in book 2
'''

# load the dataset and function we need
from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter

rossi_dataset = load_rossi()
cph = CoxPHFitter()

# fit the model
cph_result = cph.fit(rossi_dataset,
                     duration_col = 'week', event_col = 'arrest')

# see the result
cph_result.print_summary()

# plot the CI of the parameters
fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(1, 1, 1)

cph.plot(ax = ax)
