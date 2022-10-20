library(tidyverse)
library(ggplot2)

# <linear correlation>

# 1. Pearson's correlation

# (1) for two variables
x <- c(23., 23., 27., 27., 39., 41., 45., 49., 50., 53., 53., 54., 56.,
       57., 58., 58., 60., 61.)
y <- c(9.5, 27.9,  7.8, 17.8, 31.4, 25.9, 27.4, 25.2, 31.1, 34.7, 42. ,
       29.1, 32.5, 30.3, 33. , 33.8, 41.1, 34.5)

cor.test(x, y, method="pearson")
# In R, the CI can be directly seen in the results

# (2) correlation matrix
library(readr)
etfs <- read_csv('data/etfs.csv')

# use round() to control the digits
round(cor(etfs), 3)

# 2. robust "correlation"'s

# (1) Spearman's rho
cor.test(x, y, method='spearman')

# (2) Kendall's tau
cor.test(x, y, method='kendall')

#==============================================================================#
#==============================================================================#

# 1. regression
# (1) Noisy Quadratic Polynomial
# This example shows how to use the I() function(Wow, the same as python)
# source: https://www.datacamp.com/tutorial/linear-regression-R
x_1 <- 1:100
y_1 <- 150 + 3 * x_1 + 0.03 * (x_1 ** 2) + 5 * rnorm(100)

df <- data.frame(x_1, y_1)

res2F <- lm(y_1 ~ x_1 + I(x_1^2), data=df)
summary(res2F, digits=2)

# (2) example for further discussion
AT <- read_csv('data/AT.csv')

resAT <- lm(Alcohol ~ Tobacco, data=AT)
summary(resAT)

#==============================================================================#
#==============================================================================#

# <Model coefficients and their interpretation>

# 1. Coefficients
# Only for simple linear regression

tobacco <- AT$Tobacco
alcohol <- AT$Alcohol

params <- lsfit(tobacco, alcohol)

params[1]

# 2. Standard errors of coefficients
design_matrix_AT <- matrix(tobacco, ncol=1)
ONE <- matrix(rep(c(1), each=length(design_matrix_AT)), ncol=1)

# 'cbind()' - bind two matrix row-wise
X <- t(cbind(ONE, design_matrix_AT))

# 'solve()' - inverse the matrix
C <- solve(X %*% t(X))

SE <- sqrt(C * (sum(resAT$residuals ^ 2) / resAT$df.residual))

# 3. t-Statistic and its p-value
param_tobacco <- resAT$coefficients[2]
se_tobacco <- SE[2, 2]
t_tobacco <- param_tobacco / se_tobacco
t_tobacco

# p-value
# get the Dof of the residuals
dof_resid_AT <- resAT$df.residual

# the t-statistic is positive here, we shall use CDF.
# if it is negative, we shall use survival function.
p_tobacco_oneside <- 1 - pt(t_tobacco, dof_resid_AT)
p_tabacco_twoside <- p_tobacco_oneside * 2

# 4. CI
# qt - ppf of t-distribution
z_tabacco <- qt(0.975, dof_resid_AT)

CI_AT_tobacco <- c(param_tobacco - z_tabacco * se_tobacco,
                   param_tobacco + z_tabacco * se_tobacco)
CI_AT_tobacco

#==============================================================================#
#==============================================================================#

# <Assessment of the Regression>

# 1. R square
ssr_AT <- sum(resAT$residuals ^ 2)
tss_AT <- sum((alcohol - mean(alcohol)) ^ 2)

R_2_AT <- 1 - (ssr_AT / tss_AT)
R_2_AT

# 2. adjusted R square
mse_res_AT <- sum(resAT$residuals ^ 2) / resAT$df.residual

# get the Dof of the tot
dof_tot_AT <- length(tobacco) - (length(resAT$coefficients) - 1)
mse_tot_AT <- sum((alcohol - mean(alcohol)) ^ 2) / dof_tot_AT

adjust_R2_AT <- 1 - (mse_res_AT / mse_tot_AT)
adjust_R2_AT

# 3. F-test
mes_mod_AT <- (sum((resAT$fitted.values - mean(alcohol)) ^ 2) /
                (length(resAT$coefficients) - 1))

F_AT <- mes_mod_AT / mse_res_AT
F_AT

# p-value
p_F_AT = 1.0 - pf(F_AT, (length(resAT$coefficients) - 1), resAT$df.residual)
p_F_AT

# 4. Log-Likelihood
# 5. AIC and BIC
# Sorry, but I think the necessity of calculte this is small...
# And in R, I have more things to learn...

#==============================================================================#
#==============================================================================#

# <Analysis of Residuals>

# 1. Skewness and Kurtosis:
# use package moments
library(moments)
skew_AT <- skewness(resAT$residuals)
kurt_AT <- kurtosis(resAT$residuals)

c(skew_AT, kurt_AT)

# 2. Omnibus Test
# use package fBasics
library(fBasics)
# the function is indeed for the Omnibus test
# but the test needs the sample size bigger that 20
dagoTest(resAT$residuals)

# 3. Durbin–Watson test
# use package car
library(car)
durbinWatsonTest(resAT)

# 4. Jarque–Bera test
# use package tseries
install.packages("tseries")
library(tseries)
jarque.bera.test(resAT$residuals)

# 5. Condition Number
CN_AT <- sqrt(max(eigen(X %*% t(X))$values) / min(eigen(X %*% t(X))$values))
CN_AT
