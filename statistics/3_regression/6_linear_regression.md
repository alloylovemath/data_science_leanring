# Linear Regression Models
reference books:  
* *An introduction to Statistics with Python with Applications in the Life Science*, Thomas Haslwante
* *Probability and Statistics*, Morris H. DeGroot and Mark J. Schervish.

I will call them book1, book2, book3... for short.

> Well, I have to admit that I write this part very simply.
There are reasons. One is that it is hard to tape latex intensively in markdown.
The other is that I'm quilt familiar with this part. If you need more detail
material on the math foundation of this part, you may refer to some good
textbooks.

## 1. The process of statistical modeling
1. visual inspection of the data
2. Looking for the correlation and/or relationships
3. select statistical model to describe the data
4. determine the parameters of the model
5. assess the quality of the model and inspect the residuals  
    if the residuals are too large or other things go wrong -- back to step 3  
    if not, we may find the appropriatemodel


## 2. Linear Correlation
Since the visual inspecting has been discussed in the previous parts, we shall
starts with the correlation parts.

### 2.1 Pearson's correlation coefficient

$$r=\frac{s_{xy}}{s_{x}s_{y}}$$  

Here the $s_{xy}$ is the sample covariance; $s_{x}, s_{y}$ are both sample
standard deviations.

### 2.2 rank correlation

when data are not norm. distributed, different approaches are needed. Book1
introduces two metrics, but the introduction are simple. Besides, I don't see
them a lot.

* Spearman's $\rho$  
    the same as the Pearson correlation coefficient, but calculated on 
    the ranks of the observations and not on the original numbers.
* Kendall's $\tau$  
    measures the association between two measured quantities.

## 3. General Linear Regression Model

**model**:  
$$
y_{i} = \beta_{0} + \beta_{1} x_{i} + \varepsilon_{i}.
$$

**terms**: intercept, residuals, OLS

**general model**:(for example)  

$$
y_{i} = \beta_{0} + \beta_{1} x_{i} + \beta_{2} x_{i}^{2} + \varepsilon_{i}.
$$

**terms of the model**  
* regressand, endogenous variable, response variable, measured 
variable, or dependent variable.
* regressors, exogenous variables, explanatory variables, covariates,
input variables, predictor variables, or independent variables
* effects, or regression coefficients
* residuals, error term, disturbance term, or noise
* Design Matrix

## 4. Determine the parameters

OK, how to determine the parameter? I won't write the full math deduction here.
You can refer to any statistic book or wikipedia.

## 5. The interpretation of the regression result

Aha, many people have used some statistical softwares or programming languages
to do the regression, me too. Let's be honest, What we care about most is the
p-value, if it is smaller than 0.05, then we can sleep well in the bed. But,
there are many numbers in the regression outcome, what do they mean?
Just be patient, my friend. I will explain them all later. However, the details
will not be covered. But again, you can refer to any statistical textbook or
wikipedia.

### 5.1 Model coefficients and their interpretation

**Coefficients**:

The coefficients actually are calculated from the design matrix, there are
examples in the code part, which you can refer to.

**Standard errors of coefficients**:

The calculation of standard erros of coefficients involves design matrix and
the mean squared error of the residual. Also, examples in the code.

**t-Statistic**:

The t-Statistic is the indicator for us to get the p-value. We use it to do the
hypothesis testing for the parameters. If the p-value we get by referring the
t-statistic is small(usually 0.05 or 0.001), the we say the parameter is
significant -- the predictor does contribute to the response.

**CI**:

CI has already been introduced in previous post, you can refer to them. Maybe
one thing need to mentioned here -- if the CI of a parameter do not cover 0,
then the parameter is significant.

**Df**:  
* Df Model: (Corrected) Model Degrees of Freedom -- $k-1$;
* Df Residuals: Residuals Degrees of Freedom -- $n-k$;
* Df Total: (Corrected) Total Degrees of Freedom -- $n-1$;

Here, $n$ is the number of observations; $k$ is the number of regression
parameters, including the intercept. There is a relation of the 3 numbers:

$$
DF_{\text{mod}} + DF_{\text{res}} = DF_{\text{tot}}
$$

From Df's, we can get another 3 numbers:  
* $MS_{\text{mod}} = SS_{\text{mod}} / DF_{\text{mod}}$:
Model Mean of Squares;
* $MS_{\text{res}} = SS_{\text{res}} / DF_{\text{res}}$:
Residuals Mean of Squares. It is the unbiased estimate for $\sigma^{2}$ for
multiple regression models;
* $MS_{\text{tot}} = SS_{\text{tot}} / DF_{\text{tot}}$:
Total Mean of Squares.

---

### 5.2 Assessment of the Regression

Above is some figures we can get by applying the statistical method. Problem is
how to assess these figure? A bunch of numbers showed in the regression outcome
can be used, let's take a look.

**The coefficient of determination $R^{2}$**:  
Let's consider a perfect regression, that is the predict values of the model are
completely the same as the dependent values. In such a scenario, what will the
metric below be:  

$$
\frac{SS_{\text{res}}}{SS_{\text{tot}}} =
\frac{ \sum_{i=1}^{n} {(y_{i} - \hat{y}_{i}) ^ {2}} }
{ \sum_{i=1}^{n} {(y_{i} - \bar{y}) ^ {2}} }
$$

The answer would be 0 becanse the numerator is 0. OK, then what this metric is
saying? Look at the denominator first. It looks like the variance right? So,
we can say that the denominator shows the variation of the $y_{i}$'s.
Now, take a look at the nomerator. Obviously, it can only be calculated after
the regression(or where can you find the predict values). Here is the important
thing -- **the nomerator shows the variation that is still present after the
regression**. Why? Because some variation of the data has been explained by the
model. Review the scenario we just mentioned above. If our model are "perfect"
the dependent values are completely the same as the predict values, then answer
the question: why the $y_{i}$'s change? Because the $x_{i}$'s change no more
other reasons -- the residuals are 0's.

So, the metric above just shows us how much variation not be explained by the
regression model. Obviously, it won't exceed 1. So how about we subtract it from
1? We get:  

$$
R^{2} = 1 -\frac{SS_{\text{res}}}{SS_{\text{tot}}} =
\frac{SS_{\text{mod}}}{SS_{\text{tot}}}
$$

These new metirc shows the variation explained by the model. And we call it
$R^{2}$, which can be viewed as the metric to assess how good the model is.
As you can see, in the perfect scenario, this number would be 1 or 100%.

**Adjusted $R^{2}$**:  

> **With four parameters, I can fit an elephant, and with five I can make him
wiggle his trunk.** *Von Neumann*

A thing needs pay attention to is that with more parameters, the $R^{2}$ usually
will get bigger. But does it mean a better model? Well, maybe not. Because you
can add to the model a independent variable which is completely unrelated to
the dependent variable, and you still get a higher $R^{2}$.
So, we need to modify the metric $R^{2}$ so that it will not always increse
with more parameters unless the parameter do affect the dependent variable.

Here comes adjusted $R^{2}$, often writen as $\bar{R}^{2}$ or
$R^{2}_{\text{adj}}$:  

$$
\bar{R}^{2} = 1 - \frac{SS_{\text{res}} / DF_{\text{res}}}
{SS_{\text{tot}} / SS_{\text{tot}}}=
\frac{SS_{\text{res}}}{SS_{\text{tot}}}
\frac{n-1}{n-k}=
1 - (1 - R^{2}) \frac{n-1}{n-k}.
$$

As you can see, when we introduce more parameters into the model, $k$(the
number of the parameters) will get bigger. So $(n - 1) / (n - k)$ will get
smaller. So, althrough $R^{2}$ get larger, $\bar{R}^{2}$ may not get bigger.

**$F$-test**:  
The $F$-statistic in the regression outcome is for the hypothesis test which
test the null hypothesis that all the parameters are 0. And the null hypothesis
is true, our model must be a "bad" model, clearly. The figure is defined as:  

$$
F = \frac{SS_{\text{mod}} / DF_{\text{mod}}}{SS_{\text{res}} / DF_{\text{res}}}.
$$

If the null hypothesis is true, the $F$-statistic will comply a $F$ distribution
with ($DF_{\text{mod}}, DF_{\text{res}}$) DOF. So, we can perform the hypothesis
testing(Prob (F-statistic) in the regression outcome comes from here).

**Log-Likelihood**:  
Usually, we apply the OLS method to do the regression. However there is another
way -- MLE. The Log-Likelihood in the regression outcome shows value of the
log likelihood function. And the esitimator of the variance of the residuals,
is:  

$$
E(\sigma^{2}) = \frac{SS_{\text{res}}}{n}.
$$

**Information Content of StatisticalModels: AIC and BIC**:  
I don't know much about them, frankly speaking. In book1, it said that both
measures are only used when trying to decide between different models. And we
shall choose model with lower AIC or BIC value.

---

### 5.3 Analysis of Residuals

Other figures in the regression outcome mainly relate to the residuals.

**Skewness and Kurtosis**:  
Pass, since we have already discussed those metrics.

**Omnibus Test**:  
Test that if the residuals are normal distributed. Small p-value means that
the residuals may not norm. distributed.

**Durbin–Watson test**:  
The Durbin–Watson test is used to detect the presence of **autocorrelation (a
relationship between values separated from each other by a given time lag)** in
the residuals.

**Jarque–Bera test**:  
Just like the omnibus test, but not suitable for small data set.

**Condition Number**:  
Measures the sensitivity of a function’s output to its input. I don't know it
very well. According to book1, it handles the problem called
**multicollinearity**. If the result is below 30, then we get a "good" model.

Ok, see examples in the code.
