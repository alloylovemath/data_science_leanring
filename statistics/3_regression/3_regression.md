# Linear Regression Models
**Procedure**:  
1. visual inspection of the data
2. select statistical model to describe the data
3. determine the parameters of the model
4. assess the quality of the model
5. inspect the residuals

## Linear Correlation
metrices:  
1. Pearson's correlation coefficient  
    $$r=\frac{s_{xy}}{s_{x}s_{y}}$$
2. rank correlation  
    when data are not norm. dis.  
    * Spearman's $\rho$  
        the same as the Pearson correlation coefficient, but calculated on 
        the ranks of the observations and not on the original numbers.
    * Kendall's $\$

## Terms of General Linear Regression Model
1. basics  
    intercept, residuals, OLS
2. SS  
    * $SS_{\textnormal{mod}}$, the Model Sum of Squares  
    * $SS_{\textnormal{res}}$, the Residuals Sum of Squares
    * $SS_{\textnormal{total}}$, the Total Sum of Squares
    * $R^{2}$
3. Patsy: The Formula Language  
    ~, :, *
4. terms of the model  
    * regressand, endogenous variable, response variable, measured 
    variable, or dependent variable.
    * regressors, exogenous variables, explanatory variables, covariates,
    input variables, predictor variables, or independent variables
    * effects, or regression coefficients
    * residuals, error term, disturbance term, or noise

**Terms of the regression results**:  
1. Adjust $R^{2}$, penalized for having a large number of parameters in the
model
2. The F-Test, test the hypothesis that all the param.' is 0
3. Log-Likelihood, the value of likelihood of the maximum likelihood estimator
of residuals' $\sigma$
4. Akaike Information Criterion (AIC), Bayesian Information Criterion (BIC)  
    Both measures are only used when trying to decide between different models  
    we should choose the model with the lower AIC or BIC value
5. Analysis of Residuals  
    * Omnibus Test  
    * Durbin–Watson test, detect the presence of autocorrelation 
    (a relationship between values separated from each other by
    a given time lag)  
    * Jarque–Bera Test
    * Condition Number, measures the sensitivity of a function’s output
    to its input  
    If the condition number is greater than 30, then the regression may have
    multicollinearity.
