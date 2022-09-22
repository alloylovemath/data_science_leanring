# <Normality check>

# 1. graph
# (1) QQ-Plot
norm_samp <- rnorm(100)

# > draw a QQ-plot
# > main-title, xlab, ylab-label, col-color of the points
qqnorm(norm_samp, main='QQ-Plot for Normality', xlab='Normal dis.',
       ylab='Sample dis.', col='blue')
# > add a reference line
# > lwd-line width lty-line style
qqline(norm_samp, col='red', lwd=2, lty=1)

# (2) PP-plot
# >Source:https://drjamesready.com/2020/10/19/__trashed-2/
# >Source:https://cran.r-project.org/web/packages/qqplotr/vignettes/introduction
# .html
# use ggplot2 and qqplotr package
library(ggplot2)
library(qqplotr)
ggplot(mapping=aes(sample=norm_samp)) +
  stat_qq_point(col="red") +
  stat_qq_line(col="blue") +
  labs(x = "Normal dis.", y = "Sample dis.")

# (3) Probability plot
# > QQ-plot -- quantile vs. quantile
# > probability plot-- quantile(x-axis) vs. prob.
install.packages("e1071")
library(e1071)
probplot(norm_samp)

# 2. statistic test

# (1) Shapiro-Wilk test
# > The p-value is greater than 0.05. Hence, the distribution of the given data
# is not different from normal distribution significantly.
shapiro.test(norm_samp)

# (2) Lilliefors-test
# use package nortest
install.packages("nortest")
library(nortest)
lillie.test(norm_samp)

# (3) Kolmogorov-Smirnov test
# > "pnorm" -- CDF of normal dis.
ks.test(norm_samp, "pnorm")

# (4) D'Agostino–Pearson omnibus test
# > use package fBasics
install.packages("fBasics")
library(fBasics)
dagoTest(norm_samp)

# > it seems that KS test, SW test, Lilliefors test can also be down with it
shapiroTest(norm_samp)
lillieTest(norm_samp)
ksnormTest(norm_samp)


#==============================================================================#
#==============================================================================#

# # <Hypothesis Tests>

# 1. Cases

# book1 page 126, H0 -- mean = 110
scores <- c(109.4, 76.2, 128.7, 93.7, 85.6,
            117.7, 117.2, 87.3, 100.3, 55.1)

# --step 1: check normality
qqnorm(scores, main='QQ-Plot for Normality', xlab='Normal dis.',
       ylab='Sample dis.', col='blue')
# > add a reference line
# > lwd-line width lty-line style
qqline(scores, col='red', lwd=2, lty=1)

library(fBasics)
dagoTest(scores) # in R sample size must be larger than 20, so we failed here

# --step 2: do t test
# > the way I learned in the math lecture is a little different from the book1
# > (not so different...). so I display two ways here
# --- way 1: set significant level(0.05), define the critical region
# finally, check the mean falls into which region

# accept region
right_side <- (sqrt(1 / length(scores)) *
                 sd(scores) * qt(.975, length(scores) - 1)) + 110
# here, (sqrt(1 / length(scores)) * sd(scores) = plotrix::std.error(scores)

left_side <- -(sqrt(1 / length(scores)) *
                 sd(scores) * qt(.975, length(scores) - 1)) + 110

accept_region <- c(left_side, right_side)
accept_region

# check the mean
mean(scores) # the result is 97.11999999999999, so wo accept H0

# ---way 2: book1's way
# > t statistic
tval <- (110 - mean(scores)) / plotrix::std.error(scores) # here, tval > 0

# pt -- cdf
p <- 2 * (1 - pt(tval, length(scores)-1)) # if tval < 0, we don't need "1 - "
p # 0.09953844 greater than 0.05, so we accept H0

# Actually, there is a more convenient way
t.test(scores, mu=110)


# 2. Power
# use package pwr
install.packages("pwr")
library(pwr)

# d = mu-m0
# > here the d must be negative number
# > H0 -- >, means that H1 -- <
# > to detect, mu here must be more less than mu0
pwr.norm.test(d=-0.5, power=0.95, sig.level=0.05, alternative='less')
