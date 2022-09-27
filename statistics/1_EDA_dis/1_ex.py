# -*- coding: utf-8 -*-

'''
This is my solution for the exercise of book1 in Chapter 6
'''

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('seaborn')

import math

# (1)
a = np.arange(1, 11)

np.mean(a)
np.std(a, ddof=1)

# (2)
norm_dis = stats.norm(loc=5, scale=3)

# plot the pdf
fig, ax = plt.subplots(1, 1)

x = np.linspace(norm_dis.ppf(0.01),
                norm_dis.ppf(0.99), 100)
ax.plot(x, norm_dis.pdf(x), '-')

# generate 1000 random data
data = norm_dis.rvs(1000)

# plot the histogram of data
fig, ax = plt.subplots(1, 1)

ax.hist(data, bins=40)

# 95% interval (not CI)
np.array([norm_dis.ppf(0.025), norm_dis.isf(0.025)])

# practical problem
# > mu - 1 <= X <= mu + 1 -->
# > -1 / sigma <= (X-mu) / sigma ~ N(0, 1) <= 1 / sigma
# > So, we get 1 / sigma >= u(0.0005)(上分位数)
norm_dis_1 = stats.norm(loc=0, scale=1)
1 / norm_dis_1.isf(0.0005) # 0.304

# (3)
weights = np.array([52, 70, 65, 85, 62, 83, 59])

# mean
np.mean(weights)

# 95% CI
# > Suppose weight ~ N(mu, var)
left_side = (np.mean(weights) - (math.sqrt(1 / len(weights))
            * np.std(weights, ddof=1) * stats.t.isf(0.005, (len(weights) - 1))))
right_side = (np.mean(weights) + (math.sqrt(1 / len(weights))
            * np.std(weights, ddof=1) * stats.t.isf(0.005, (len(weights) - 1))))

np.array([left_side, right_side])

# use sem may make the code more clean
left_side_1 = (np.mean(weights) -
            (stats.sem(weights) * stats.t.isf(0.005, len(weights) - 1)))
right_side_1 = (np.mean(weights) +
            (stats.sem(weights) * stats.t.isf(0.005, len(weights) - 1)))
np.array([left_side_1, right_side_1])

# or stats just have the function
# > notice that the scale is sem
stats.t.interval(alpha=0.99, df=len(weights)-1,
                loc=np.mean(weights), scale=stats.sem(weights))

# (4)
norm_sample_1 = stats.norm().rvs(1000)
norm_sample_2 = stats.norm().rvs(1000)
norm_sample_3 = stats.norm().rvs(1000)

chi2_sample = ((norm_sample_1 ** 2) +
               (norm_sample_2 ** 2) + (norm_sample_3 ** 2))

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# > density = True -- frequency plot, False -- counts
ax1.hist(chi2_sample, bins=100, density=True)

chi2_dis = stats.chi2(df=3)
x = np.linspace(chi2_dis.ppf(0.01),
                chi2_dis.ppf(0.99), 100)
ax2.plot(x, chi2_dis.pdf(x), '-')
plt.show()

# (5)
# > Compare two samples variance, reference -- Chen's book page 212-213
weights_1 = np.array([110, 121, 143])
weights_2 = np.array([88, 93, 105, 124])

fval = np.var(weights_1, ddof=1) / np.var(weights_2, ddof=1)
f_dis = stats.f(len(weights_1), len(weights_2))
f_dis.cdf(fval)

# (6)
binom_dis = stats.binom(n=15, p=0.37)

binom_dis.pmf(3)
binom_dis.pmf(6)
binom_dis.pmf(10)

# (7)
poisson_dis = stats.poisson(1.19)

poisson_dis.pmf(0)
poisson_dis.pmf(2)
poisson_dis.pmf(5)
