library(tidyverse)

# <case 1>

# Our first example comes from book2
# it actually is the example of Ch.11
# for detail of the data, you can refer to the book.

# load the data
deny <- readr::read_csv('data/logit_11.csv')

resCase1_logit <- glm(deny ~ black + pi_rat, data=deny, family='binomial')

# > If we want clustered standard errors
#source: https://stackoverflow.com/questions/16498849/logistic-regression-with-robust-clustered-standard-errors-in-r

# use package sandwich
install.packages("sandwich")
install.packages("lmtest")

library(sandwich)
library(lmtest)

coeftest(resCase1_logit, vcov. = vcovCL(
  resCase1_logit, cluster = deny$id, type = "HC0")
)

# Ah, other examples in Python code are just 'experiments' for different methods
# performing logit regression. So, in R, it seems that this example is enough.
# (I'm a lazy boy, forgive me.)
