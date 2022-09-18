# read a csv file

# there will be a object on the rigt side

# R will first find files in the working directory
# when using R projects, the working directory is where you have
# the *.Rproj file

# <- the same as =, <- is better
diamonds <- read.csv("ch02-r4py/data/diamonds.csv")

# click on it will show a Excel-like sheet
# View(diamond)

# install tidyverse package
install.packages("tidyverse")

# check the directory of the package
.libPaths()

# load the package
# we can load the whole package
# but maybe it's better to load the part you really want
library(readr)

# another way of loading packages is
# require(reader)

# function read_csv in readr
# much the same as read.csv in the base R
diamonds_2 <- read_csv("ch02-r4py/data/diamonds.csv")

# compare the output
diamonds
diamonds_2

# another way to use function in a package
# diamonds_2 <- reader::read_csv("ch02-r4py/data/diamonds.csv")
# when to use this method?
# 1. when you only need one specific function in a package
# 2. name collision

# round brackets around an expression means excute the expression
# and print the result
(aa <- 8)

# but try to avoid this, instead using code below
aa <- 8
aa

# use use Ctrl + Shift + C can comment out the print line easily in RStudio
# review: in Spyder the same operation can be done by Ctrl + 1

# the class of diamonds and diamonds_2 are different
class(diamonds)
class(diamonds_2)

#==============================================================================#
#==============================================================================#

# Types in R
# Page 24

#==============================================================================#

# Vector
# vectors are homogeneous
# bool's in R use capital letters(all capital)
a <- c(TRUE, FALSE)
class(a)

# R, by default, interprets numbers as double
b <- c(1, 2)
typeof(b)

# When you want to use integer, two methods can be used
# way 1
b <- as.integer(c(1, 2))
typeof(b)

# way 2
b <- c(1L, 2L)
typeof(b)

# construct a data.frame
my_data_frame <- data.frame(
  a = c(TRUE, FALSE),
  b = c(1L, 2L),
  c = c(3.14, 6.8),
  d = c("a", "b")
)
my_data_frame

# or, construct a tibble
library(tidyverse)
my_tibble <- tibble(
  a = c(T, F),
  b = c(1L, 2L),
  c = c(3.14, 6.8),
  d = c("a", "b")
)
my_tibble

# str() in Python in a function for type conversion
# However in R, it's for showing the structure of a object
str(my_tibble)

# Another way(need load the tidyverse package)
glimpse(my_tibble)


# Importing a file with no header
diamonds_base_nohead <- read.csv("ch02-r4py/data/diamonds_noheader.csv",
                                 header = F)
diamonds_tidy_nohead <- read_csv("ch02-r4py/data/diamonds_noheader.csv",
                                 col_names = F)

# see the column names
# If no header provided -- default is V1 or X1
names(diamonds_base_nohead)
names(diamonds_tidy_nohead)

names(diamonds)

#==============================================================================#

# List
# the list of R is different from list in Python
# Actually, data.frame or tbl is a specific list

# In the case that each element is a vector of the same length
class(my_tibble)

glimpse(PlantGrowth)
str(PlantGrowth)
view(PlantGrowth)

# define a linear model -- lm()
pg_lm <- lm(weight ~ group, data=PlantGrowth)
# We will get "a type list of class lm"
typeof(pg_lm)
class(pg_lm)

# access a named element within a list using the $ notation
names(PlantGrowth)

# Ah, in R, the index begins at 1!!!
PlantGrowth$weight

# now, look at the lm
names(pg_lm)
pg_lm$coefficients

# if there are a lot of independent variables, we may use . to simplify
lm(len ~ ., data = ToothGrowth)
# the same as
lm(len ~ supp + dose, data = ToothGrowth)
# but if you want different types of model, . may can't help
lm(len ~ supp * dose, data = ToothGrowth)


#==============================================================================#
#==============================================================================#

# Factors
# factor, in R, is a class to type integer
typeof(PlantGrowth$group)
class(PlantGrowth$group)

# we can tell factors in str() or Levels in the out put of the print
str(PlantGrowth)
PlantGrowth$group

# using dput() to see the internal structure of an obj.
dput(PlantGrowth$group)

# categorical variable with order
# the output is different from the result on the book?
diamonds$color


#==============================================================================#
#==============================================================================#


# the output is a logical vector
diamonds$price > 18000
diamonds$price > 18000 & diamonds$carat < 1.5

# in R, logical is also defined by 1 and 0
# so, we can do math on them
sum(diamonds$price > 18000 & diamonds$carat < 1.5)
sum(diamonds$price > 18000 & diamonds$carat < 1.5)/nrow(diamonds)


# index
# page 33, table 2-3

# letters -- a built-in vector
letters

# remember, in R, index starts at 1!
letters[1]
letters[23:26]
letters[23:length(letters)]

# different from Python, [-4] is not the 4th element
# counting backward
# it's Everything except the 4th element
letters[-4]

# Exclude elements 1 through 20
letters[-(1:20)]

# using logical expression to index
diamonds$color[diamonds$price > 18000 & diamonds$carat < 1.5]

# the same as
str(diamonds[diamonds$price > 18000 & diamonds$carat < 1.5, "color"])
# you can think that
# i -- for rows
# j -- for columns

str(diamonds_2[diamonds_2$price > 18000 & diamonds_2$carat < 1.5, "color"])

# the + operator in the book will automatically get in the console
diamonds %>%
  filter(price > 18000, carat < 1.5) %>%
  select(color)

# in the code above, we used %>% to unnest objects and functions
# it is the same as
select(filter(diamonds, price > 18000, carat < 1.5), color)

# function summarise()
# it often used with group_by()
# the functions applied in summarise are thus group-specific
PlantGrowth %>%
  group_by(group) %>%
  summarise(avg=mean(weight), stdev=sd(weight))

# mutate()
# used to apply a transformation function, which returns as many outputs
# as inputs
irrigation <- read_csv("ch02-r4py/data/irrigation.csv")
irrigation

irrigation %>%
  group_by(region) %>%
  mutate(area_std_1980 = area/area[year == 1980])

irrigation <- irrigation %>%
  group_by(region) %>%
  mutate(area_std_1980 = area/area[year == 1980],
         area_per_change = c(0, diff(area)/area[-length(area)] * 100))

irrigation

#==============================================================================#
#==============================================================================#

# Iteration?

# tapply is in the apply family(on page 39)
# the code below is
# take the weight column from the PlantGrowth dataset,
# split the values according to the label in the group column
# in the PlantGrowth dataset, apply the mean function to each
# group of values, and then return a named vector
tapply(PlantGrowth$weight, PlantGrowth$group, mean)

# modern method
library(dplyr)
PlantGrowth %>%
  group_by(group) %>%
  summarize(avg = mean(weight))

# very old way
aggregate(weight ~ group, PlantGrowth, mean)
