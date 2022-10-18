library(tidyverse)

# <Weibull Dis.>

# Unlike Python, the Weibull distribution in R is the same as we introduced
# remember k is the **scale parameter**; lambda is the **scale parameter**

# (1) draw the graph of Weibull dis.

# Use ggplot2 library
library(ggplot2)

ggplot(data.frame(x = c(0, 6)), aes(x = x)) +
  stat_function(fun = dweibull, args=list(shape=1.5, scale=2))

# (2) fit the Weibull dis.
# source: https://www.r-bloggers.com/2020/01/survival-analysis-fitting-weibull-models-for-improving-device-reliability-in-r/
sample_weibull <- read_csv('data/weibull_fit.csv')

# use package fitdistrplus
install.packages("fitdistrplus")
library(fitdistrplus)
weibull_fit_results <- fitdist(sample_weibull$data, "weibull")

summary(weibull_fit_results)
# We still get a shape parameter around 1.5, but the result is slightly
# different from the Python's version
# I don't know why since I don't know the underneath process

# <Kaplan–Meier survival curve>

# (1) draw the curve
# source: https://rviews.rstudio.com/2017/09/25/survival-analysis-with-r/


# load the data
waltons_data <- read_csv('data/waltons_data.csv')

# use package survival
library(survival)

# fit the KM curve
# > use Surv to constuct a survival object
# > T - time, E - consored or not
# > ~ group: for divide into different groups
km_fit <- survfit(Surv(T, E) ~ group, data=waltons_data)

# plot the KM curve
autoplot(km_fit)


# (2) Compare two curves using logrank test
# source: https://www.r-bloggers.com/2021/08/log-rank-test-in-r-survival-curve-comparison/
logrank_results <- survdiff(Surv(T, E) ~ group, data=waltons_data)
logrank_results

# <Cox Proportional Hazards Model>

# you can see the detail of this case in book 2

# load the data
rossi_data <- read_csv('data/rossi_data.csv')

# fit the model
# source: https://socialsciences.mcmaster.ca/jfox/Books/Companion/appendices/Appendix-Cox-Regression.pdf
rossi_result <- coxph(formula = Surv(week, arrest) ~ fin + age + race + wexp +
        mar + paro + prio, data = rossi_data)
rossi_result

# plot the CI of params.
# source: https://www.themillerlab.io/post/survival_analysis/

# > use package survminer
install.packages("survminer")
library(survminer)
ggforest(rossi_result)
