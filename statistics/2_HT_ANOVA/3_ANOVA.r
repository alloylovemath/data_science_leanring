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

#==============================================================================#

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

#==============================================================================#

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
