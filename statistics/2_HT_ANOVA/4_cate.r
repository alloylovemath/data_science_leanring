library(tidyverse)
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

#==============================================================================#

# <Fisher’s Exact Test>
# 1. case 1
# source: José Unpingco's book
data_4 <- data.frame(
  one = c(13, 12),
  two = c(11, 1)
)

r1 <- sum(data_4[1, 1:2])
r2 <- sum(data_4[2, 1:2])

c1 <- sum(data_4[1:2, 1])
c2 <- sum(data_4[1:2, 2])

# library(tidyverse)
data_4 <- data_4 %>%
  as.matrix() %>%
  as.table()

# p -- cdf
# r1, r1 specify the total number
# c1 -- numer of drawn
phyper(13, r1, r2, c1)

fisher.test(data_4, alternative='less')

# 2. case 2
# source: book1
data_5 <- data.frame(
  one = c(3, 1),
  two = c(1, 3)
)

r1 <- sum(data_5[1, 1:2])
r2 <- sum(data_5[2, 1:2])

c1 <- sum(data_5[1:2, 1])
c2 <- sum(data_5[1:2, 2])

# use 1 - cdf(sf) when alternative is larger
# 2 not 3, because we want the prob. of 3 involved
1 - phyper(2, r1, r2, c1)

data_5 <- data_5 %>%
  as.matrix() %>%
  as.table()

fisher.test(data_5, alternative='greater')

#==============================================================================#

# <McNemar’s Test>
# Source: book1(I noticed that there is a same example in Wikipedia)
data_6 <- data.frame(
  one = c(101, 59),
  two = c(121, 33)
)

data_6 <- as.matrix(data_6)

mcnemar.test(data_6, correct=FALSE)

#==============================================================================#

# <Cochran’s Q Test>
# Source: book1
# use package RVAideMemoire
install.packages("RVAideMemoire")
library(RVAideMemoire)
response <- c(0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0,
              1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
              0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0)
people <- gl(12,3,labels=letters[1:12])
treatment <- gl(3,1,36,labels=LETTERS[1:3])

cochran.qtest(response~treatment|people)
