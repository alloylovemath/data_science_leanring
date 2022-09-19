***Be as brief as possible, but take down everything noteworthy***

# EDA

## Estimation of Location
metrics:  
1. mean  
    * arithmetic mean
    * geometric mean
    * trimmed-mean
    * weighted-mean
2. median  
    * median
    * weighted-median
3. mode

## Estimation of Variability
metircs:
1. deviation  
    * mean absolute deviation
    * variance
    * standard deviation
    * median absolute deviation(MAD)
    * trimmed standard deviation
2. order statistics  
    * range
    * $p$ th percentile  
        median = 50th percentile  
        quantile -- 0.8 quantile = 80 th percentile
    * interquartile range -- IQR  
        75th percentile - 25th percentile
3. standard error (of mean) -- SE(M)

## Esitimation of the shape
1. skewness
2. kurtosis

# Distribution

## Representation of distribution

Methods:  
1. Probability density function (PDF)  
    for discrete distribution -- probability mass function (PMF)
2. Cumulative distribution function (CDF)
3. Survival Function (SF) -- SF = 1 - CDF
4. Percentile Point Function (PPF) -- the inverse of the CDF
5. Inverse Survival Function (ISF) -- the inverse of the SF
6. Random Variate Sample (RVS) -- random variates from a given distribution

Two-step procedure working with distribution:  
1. create a dis.
2. decide the function (above) to use
