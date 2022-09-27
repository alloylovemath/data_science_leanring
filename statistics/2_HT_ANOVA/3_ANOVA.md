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

## Tukey's HSD
*pass*

## two-factor ANOVA
The idea is much the same as the one-way factor ANOVA if we don't consider the
interaction of factors.

With more than two factors, it is recommendable to use statistical modeling
for the data analysis.
