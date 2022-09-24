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


#==============================================================================#
#==============================================================================#

# <ANOVA>

# 1. one-factor ANOVA
# (1) case 1
# > Source: Chen's book
group_1 = data.frame(
  values = c(390, 410, 372, 385),
  group = "1"
)
group_2 = data.frame(
  values = c(375, 348, 354, 364, 362),
  group = "2"
)
group_3 = data.frame(
  values = c(413, 383, 408),
  group = "3"
)
plant = rbind(group_1, group_2, group_3)

a <- aov(values ~ group, data=plant)
summary(a)

# 2. Kruskal–Wallis test
city1 <- c(68, 93, 123, 83, 108, 122)
city2 <- c(119, 116, 101, 103, 113, 84)
city3 <- c(70, 68, 54, 73, 81, 68)
city4 <- c(61, 54, 59, 67, 59, 70)

cities <- c(city1, city2, city3, city4)
g <- factor(rep(1:4, c(6, 6, 6, 6)),
            labels = c("city1", "city2",
                       "city3", "city4"))
kruskal.test(cities, g)
# > Or, we could do it like above

# 3. two-factor ANOVA

# (1) case 1
# > source: Chen's book (no interaction)
group_1 = data.frame(
  values = c(292, 316, 325),
  species = "1",
  breed = c('1', '2', '3')
)
group_2 = data.frame(
  values = c(310, 318, 317),
  species = "2",
  breed = c('1', '2', '3')
)
group_3 = data.frame(
  values = c(320, 318, 310),
  species = "3",
  breed = c('1', '2', '3')
)
group_4 = data.frame(
  values = c(370, 365, 330),
  species = "4",
  breed = c('1', '2', '3')
)
plant_2 = rbind(group_1, group_2, group_3, group_4)

a <- aov(values ~ species + breed, data=plant_2)
summary(a)

# (2) case 2 (interaction)
# > book1
df <- read.csv("D:/daily_learning/altman666.csv",
               stringsAsFactors = TRUE)
# convert integer to factor
df$fetus <- as.factor(df$fetus)
df$observer <- as.factor(df$observer)
# * for interaction
a <- aov(hs ~ fetus * observer, data=df)
summary(a)


#==============================================================================#
#==============================================================================#

# <Chi-square test>

# 1. one-way test

# (1) case 1
# > source: Chen's book
# > by default, the expect situation is equally likely
data_1 <- c(6, 3, 6)
chisq.test(data_1)

# (2) case 2
# > source: book1
data_2 <- c(10, 6, 5, 4, 5, 3)
chisq.test(data_2)

# 2. contingency table
# create a contingency table
data_3 <- data.frame(
  one = c(63, 16),
  two = c(37, 17),
  Three = c(60, 8)
)

data_3 <- as.table(as.matrix(data_3))

chisq.test(data_3)

# <Fisher’s Exact Test>
data_4 <- data.frame(
  one = c(4, 0),
  two = c(0, 4)
)

# library(tidyverse)
data_4 <- data_4 %>%
  as.matrix() %>%
  as.table()

fisher.test(data_4, alternative="greater")
