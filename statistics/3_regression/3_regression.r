# <Simple Linear Regression>

# 1. case 1
data_1 = read.csv("D:/daily_learning/data_science/statistics/sta/al_to.csv")
model = lm(formula= Alcohol ~ Tobacco, data=data_1[1:10,])
summary(model)
