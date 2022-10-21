library(tidyverse)

# (1)

# load the data
# > source:https://www.r-bloggers.com/2021/06/reading-data-from-excel-files-xlsxlsxcsv-into-r-quick-guide/
# use package readxl
install.packages("readxl")
library(readxl)
AvgTemp <- read_excel('data/AvgTemp.xls')

Year <- AvgTemp$year
AvgTmp <- AvgTemp$AvgTmp

# get the Pearson's correlation
cor.test(Year, AvgTmp, method="pearson")

# get the Spearman's rho
cor.test(Year, AvgTmp, method="spearman")

# get the Kendall's tau
cor.test(Year, AvgTmp, method="kendall")


# (2)
resTMP <- lm(AvgTmp ~ year, data=AvgTemp)
summary(resTMP)

# (3)
ks.test(resTMP$residuals, 'pnorm')
