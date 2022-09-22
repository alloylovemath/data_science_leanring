***Be as brief as possible, but take down everything noteworthy***

# Hypothesis Tests

## Typical Analysis Procedure
"The old days" -- hypothesis tests' procedure  
1. formulate hypothesis
2. collect data
3. determine

Modern way:  
1. looking at the data (visualization)
2. generate models
3. determine the best fit parameters
4. check the model (residuals)
5. ? modify

**Start off steps**:  
1. Visually inspect the data
2. Find extreme samples, and check them carefully
3. Determine the data-type of the values
4. If the data are continuous, check whether or not they are normally distributed
5. Select and apply the appropriate test, or start with the model-based analysis of the data

## Normality Check
Often, we conduct our test based on that the paramaters we estimated can approximatelly described by a specific dis.(especially, normal). This means, if not, our estimation might be wrong $\Rightarrow$ test is necessary.

**Tools**:  
1. graph  
    * QQ-Plots Q -- quantile
    * PP-Plots use CDF
    * Probability Plots

    In all three cases the results are similar: if the two distributions being compared are similar, the points will approximately lie on the line $y=x$.
2. statistic test  
    * Shapiro-Wilk -- for samll data set ($\le$ 50)
    * Lilliefors-test -- for intermediate data set
    * Kolmogorov-Smirnov -- large data set (>300)
    * D'Agostino–Pearson omnibus test -- combines a skewness and kurtosis test to produce a single, global “omnibus” statistic.
3. transformation  
    sometimes, samples are not apply to a normal dis.. but we can transform them to approximatelly apply to normal dis.  
    Say, a data set covers only positive number -- try take the $\log$ value.

## Hypothesis Test

The basic idea of hypothesis test will not be covered here. If you are not familiar with it, and you can read Chinese, I recommend you the book *Probability theory and statistics* written by Chen Xiru, the founder of Chinese statistics subject.

exploratory research - produce p-value
confirmatory research - check if the p-value showed again
calibrated p-value(page 129, use seldom)

## power (sensitive) and sample size
There are detailed explaination on the book written by Mr.Chen Xiru (from page
196 to page 203, one sample one side). In short, four factors are involved here:  
1. $\alpha$
2. $\beta$ -- power
3. $d$ -- the effect size, i.e., the magnitude of the investigated effect relative to $\sigma$, the standard deviation of the sample
4. $n$ -- sample size

## Sensitivity and Specificity
Bayes Formula? pretty similar, at least.

**Four numbers**:  
1. ill -- test pos. (True pos) -- **Sensitivity**
2. healthy -- test neg. (Ture neg) -- **Specificity**
4. test pos. -- ill -- **Positive Predictive Value (PPV)**
4. test neg. -- healthy -- **Negative Predictive Value (NPV)**

Sensitivity and Specificity -- are independent of prevalence, more important, **they do not indicate what portion of patients with abnormal test results are truly abnormal**

For a doctor, what's more important is PPV and NPV -- **ther show the importance of the test result**. But they are affected by the prevalence of the disease.

**a high prevalence of the disease increases the PPV of the test, but decreases the NPV; and a low prevalence does exactly the opposite**

## Related Calculation in Evidence-Based medicine(循证医学)
Some indicators(see healthy as H0):  
1. False positive rate(like type 1 error -- $alpha$)  
    1-specificity
2. False negative rate(like type 2 error -- $\beta$)  
    1-sensitivity
3. Power  
    1 - type 2 error = 1 - $\beta$ = sensitivity
4. positive likelihood ratio  
    sensitivity / (false positive rate)
5. negative likelihood ratio  
    type 2 error / (specificity)

## ROC curve
There is a trade-off between sensitivity and specificity. Considering a extrem case: we classify all the people positive. It will make the sensitivity be 1 while the specificity be 0.

The ROC curve just show the trade-off. It plot sensitivity on the y-axis, specificity on the x-axis(more acurate, 1-specificity on the x-axis). If we plot a diagnal line in the plot, it means a test no better than random classification. A extremely effective diagnostic test will be at the upper-left corner.

***Be as brief as possible, but take down everything noteworthy***

**Reference Book**:  
1. 《概率论与数理统计》（陈希孺，2009年2月第一版） -- Chen's book
2. *An Introduction to Statistics with Python* (Thomas Haslwanter) -- book1

# Analysis of Variance (ANOVA)

## one-factor ANOVA
**Basic idea**:  
$$SS_{\text{Total}} = SS_{\text{Treatment}} + SS_{\text{Resid}}$$
Assumption: the data are normal distributed.

The results of ANOVA can only show us if there is a difference. But we still don't know which pair has difference. We can then perform a bunch of two-sample
t-test(slitely different, reference on page 312-313 Chen's book). However, there
will be some problems here. To solve this, methods names multiple comparision
have been developed.

Three methods:  
1. Tukey Honest Significant Difference test (HSD) method  
    studentized range
2. Bonferroni Correction  
    p-value * nums of comparisions
3. Holm Correction

For non-normal distributied data, we conduct **Kruskal–Wallis test**.

## two-factor ANOVA
The idea is much the same as the one-way factor ANOVA if we don't consider the
interaction of factors.

With more than two factors, it is recommendable to use statistical modeling
for the data analysis.