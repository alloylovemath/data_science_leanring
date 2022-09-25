state <- read.csv('D:/cs/data_ml_f/1/1/1cs/data/0/data/state.csv')
# <Estimation of Location>

# 1. mean group

# (1)arithmetic mean
mean(state$Population)

# (2)geometric mean
# >positive number

# use package psych
install.packages("psych")
library(psych)

geometric.mean(state$Population)

# (3) trimmed-mean
# >trim=0.1 for each end
mean(state$Population, trim=0.1)

# weighted-mean
weighted.mean(state$Murder.Rate, w=state$Population)

# 2. median group

# (1) median
median(state$Population)

# (2) weighted-median

# use matrixStats package
install.packages("matrixStats")
library(matrixStats)
weightedMedian(state$Murder.Rate, w=state$Population)

# 3. mode
# there are no built-in function for mode in R

#==============================================================================#
#==============================================================================#

# <Estimation of Variability>

# 1. deviation group

# (1) mean absolute deviation
# use package ie2misc
# > https://search.r-project.org/CRAN/refmans/ie2misc/html/madstat.html
install.packages("ie2misc")
library(ie2misc)

madstat(state$Population)

# (2) variance
# > the denominator is n-1
var(state$Population)

# (3) std
# > the denominator is n-1
# > in Python, it is std, here it is sd
sd(state$Population)

# (4) MAD -- median absolute deviation
mad(state$Population)

# 2. order statistics

# (1) range
range(state$Population)
# if you want the length of the data set
# there are way ways
range(state$Population)[2] - range(state$Population)[1]
max(state$Population) - min(state$Population)

# (2) percentile or quantile
quantile(state$Population, .5)
# multiple quantile
quantile(state$Population, p=c(.75, .25))

# (3) IQR .75 quantile - .25 quantile
IQR(state$Population)

# 3. SE, SEM
# define function
se <- function(x, na.rm = FALSE) {
  if (na.rm) x <- na.omit(x)
  sqrt(var(x) / length(x))
}

se(state$Population)

# or use the package plotrix
install.packages("plotrix")
plotrix::std.error(state$Population)


#==============================================================================#
#==============================================================================#

# <Estimation of Shape>

# 1. Skewness
# use package moments
install.packages("moments")
# > it is the same as  "biased version" in Python
moments::skewness(state$Population)

# 2. Kurtosis
# use package moments
# > it is the same as  "biased version" plus 3 in Python
moments::kurtosis(state$Population)


#==============================================================================#
#==============================================================================#

# Distribution
# there are so many dis. we just can't show them all
# So, we use binomial dis., poisson dis. and normal dis. to do the presentation

# 1. Binomial
# (1) PMF -- x for success num.
dbinom(x=2, size=5, p=0.1)

# (2) CDF
pbinom(2, 5, 0.1)

# (3) generate random numbers from binomial dis.
# > n -- the size you want
# > the returned values are the nums of successes
rbinom(n=10, size=100, p=0.1)

# 2. Poisson
# (1) PMF
dpois(x=3, lambda=2)

# (2) CDF
ppois(6, 6)

# (3) random variates
rpois(n=5, 10)

# 3. Normal
# (1) ISF
qnorm(0.975, 0, 1)

#==============================================================================#

# <functions>
# 1. Normal

# (1) density
dnorm(5 ,mean=5, sd=1)

# (2) CDF
pnorm(1, mean=2, sd=3)

# (3) sf = 1 - CDF
1 - pnorm(1, mean=2, sd=1)

# (4) ppf - inverse of CDF
qnorm(pnorm(1, mean=2, sd=3), mean=2, sd=3)

# (5) ISF - inverse of SF
# > get the 1 - probability, use ppf to get the value
qnorm(1-0.95, mean=0, sd=1)

# (6) RVS
rnorm(5, mean=2, sd=3)

# 2. t-dis.

# (1) density
dt(qt(0.95, 5), 5)

# (2) CDF
pt(qt(0.95, 5), 5)

# (3) sf = 1 - CDF
1 - pt(qt(0.95, 5), 5)

# (4) ppf - inverse of CDF
qt(0.95, 5)

# (5) ISF - inverse of SF
# > get the 1 - probability, use ppf to get the value
qt(1-0.05, 5)

# (6) RVS
rt(5, 5)
