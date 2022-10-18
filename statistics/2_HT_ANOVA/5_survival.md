# Survival Analysis
reference books:  
* *An introduction to Statistics with Python with Applications in the Life Science*, Thomas Haslwante
* *Python for Probability, Statistics, and Machine Learning*(second edition), José Unpingco
* 《概率论与数理统计》，陈希孺

I will call them book1, book2, book3 for short.

## What is Survival Analysis
Maybe we can see this in the application of survival analysis:  
* Test on drugs
* How long a machine lasts before it breaks
* how long people subscribe to a YouTube channel

So the survival analysis can be use to solve these problems.

Can it be used in finance? I haven't see real examples. But I have some guess.
Maybe it can be used to analysis how long the price of stocks be affected by a
specific event. Why not?

## Math Foundation of Survival Analysis
I don't get a thorough tutorial on it. But there are two things I learned by
reading the reference books. One is **hazard function**, another is **Weibull
distribution**.

### Hazard Function
Hazard function, also named **force of mortality**, **intensity rate**, or the
**instantaneous risk**, **失效率** in book3, is the instantaneous rate of failure at time $t$(
which you may can get directlly from the limitation form). The formula is:  

$$
\text{hazard function:}h(t)=
\frac{\frac{d}{dt}F(t)}{S(t)}=
\lim_{\Delta t\to 0}\frac{\text{Pr}(t< X\le t+\Delta t|X\ge t)}{\Delta t}
$$

Here, $F(t), S(t)$ is the CDF and survival function of $r.v. X$.

Why we "invent" such a indicator? Well, in survival analysis, what we are most
interested is the failure\death rate and the population at the specific time. 
So  
* $F^{\prime}(t)$, actually is the pdf, shows the failure rate;
* $S(t)$ shows the population at the specific time $t$.

There is a alternative form of the hazard function:  

$$
h(t)=-\frac{d}{dt}\ln S(t)\quad (\text{Notice that: } (\ln S(t))^{\prime}=
-[\ln (1-F(t))]^{\prime})
$$

## Weibull Distribution
The weibull distribution can be deducted from the hazard function. But why not
starts with a simple example.

Let's assume that $h(t)=\lambda$--the hazard 
function, the failure rate, is a constant $\lambda$. By the defination of
conditional probability:

$$
\begin{align*}
\text{Pr}(t< X\le t + \Delta t| X \ge t) & =
\frac{\text{Pr}(t < X \le t + \Delta t, X \ge t)}{\text{Pr}(X \ge t)}\\
&=\frac{\text{Pr}(t <X \le t + \Delta t)}{\text{Pr}(X \ge t)}\\
&=\frac{F(t + \Delta t) - F(t)}{1-F(t)}
\end{align*}
$$

So, according to the formula of hazard function in limitation form:

$$
\begin{align*}
h(t) = \lambda & =
\lim_{\Delta t \to 0}\frac{\text{Pr}(t < X \le t + \Delta t|X \ge t)}{\Delta t}\\
&=\lim_{\Delta t \to 0}\frac{\frac{F(t + \Delta t) - F(t)}{1 - F(t)}}{\Delta t}\\
&=\lim_{\Delta t \to 0}\frac{\frac{F(t + \Delta t) - F(t)}{\Delta t}}{1 - F(t)}\\
&=\frac{F^{\prime}(t)}{1 - F(t)}
\end{align*}\\
\Rightarrow F^{\prime}(t)+ \lambda F(t) = \lambda
$$

(Ah... I know this deduction before I know hazard function can be defined by
CDF and survival function directlly.) Here, we have a linear first-order ODE.
Solve this equation, we get $F(t)=1+Ce^{-\lambda t}$. Since $F(t)$ is CDF and 
$t>0$(time), we know that $F(0)=0$, so we get the specific solution:  

$$
F(t)=1-e^{-\lambda t}, \quad t>0,\\

\Rightarrow F^{\prime}(t)=f(t)=
\begin{cases}
\lambda e^{-\lambda t}, & t>0;\\
0, & \text{otherwise.}
\end{cases}
$$

Familiar? We get the exponential distribution. I don't know what is the
situation for the students in western counties. But, if you are a Chinese 
student, you must heard from your professor that the $\lambda$ in exponential 
distribution is the "failure rate" and there is a property called "无后效性" in 
it. Now, maybe you are more clear what your tutor was talking about.

You see, the hazard function leads to exponential distribution is a constant.
For the Weibull distribution, the hazard function is a increasing function
$\lambda x^{m}(\lambda >0, m>0)$. As the time pass, the failure\death rate increase. More realistic? Maybe.

Similar process, we can get the CDF of Weibull distribution:  

$$
F(t)=1-\exp [-(\lambda / m+1) t^{m+1}].\\

F^{\prime}(t)=f(t)=
\begin{cases}
\lambda t^{m} \exp [-(\lambda / m+1) t^{m+1}], & t>0;\\
0, & \text{otherwise.}
\end{cases}
$$

Ah, what about a little "amendment"? Let $k=m+1$, we get:

$$
f(t)=\lambda t^{k-1} \exp [-(\lambda/k) t^{k}].\quad (t>0)
$$

Let $(\lambda / k)^{1/k}=1/m$, we can get:  

$$
f(t)=\frac{k}{m}(\frac{t}{m})^{k-1}\exp [-(t/m)^{k}].\quad (t>0)
$$

If we want a "better" from, just let $m=\lambda$:  

$$
f(t)=
\begin{cases}
f(t)=\frac{k}{\lambda}(\frac{t}{\lambda})^{k-1}\exp [-(t/\lambda)^{k}], & t>0;\\
0, & \text{otherwise.}
\end{cases}
$$

Now, check [the page of the Weibull distribution on Wikipedia](https://en.wikipedia.org/wiki/Weibull_distribution), you can see the same formula.

## Censoring and Truncation
OK, how do we perform survival analysis then? In the simplest scenario, you can
get the data and then "fit" it to the Weibull distribution(scipy module actually
do have a function `fit()` for the Weibull distribution). But there may be some
problems remain.

Consider you are carring a test on a drug. You want to know how it affet the
survival time of the patients. Two possible scenario is:  
* Patients leave the test ahead the test(maybe they don't believe the drug);
* Patients stay safe until the end of the test. We can't hope that when the test
ends, all the patient died, right? It's so inhuman.

In both situation, we don't get the correct answer of the survival time. To
solve this, we calculate the probabilty of survival recursivelly:

$$
p_{k}=p_{k-1}\times \frac{r_{k}-f_{k}}{r_{k}}.
$$

Here, $p_{k}$ stands for the surviavl probabilty of the $k$ th period; $r_{k}$
stands for the subjects(patients) still "alive" and in the test before the $k$
th period; $f_{k}$ stands for the "failure" in period $k$.

Example comes! Suppose after the test ends, we get the data:

$$
\{1,2,3^{+},4,5,6^{+},7,8\}.
$$

Numbers without $+$ shows the time of failure for a subject. For example, $2$
means that a subject fail in period 2. Numbers with $+$ shows that the period
which subject droped out of the test. For example, $3^{+}$ means that a subject
droped out of the test in period 3. Look at the table below:

|Period | Survival Prob.| Remaining subjects|
|---|---|---|
|0 | 1| 8|
|1|$\frac{7}{8}\cdot 1$| 7|
|2|$\frac{6}{7}\cdot\frac{7}{8}\cdot 1$|6|
|3|$\frac{5}{5}\cdot\frac{6}{7}\cdot\frac{7}{8}\cdot 1$|5|
|$\cdots$|
|6|$\frac{2}{2}\cdot\frac{3}{4}\cdot\frac{4}{5}\cdot\frac{5}{5}\cdot\frac{6}{7}\cdot\frac{7}{8}\cdot 1$|2|

Pay attention to period 3 and 6, where we have subjects droped out of the test.

Using the table, we could construct a so called Kaplan–Meier survival curve,
a tool for visualize the survival analysis(detail in code).

## Comparing Survival Curves in Two Groups
I only learned the **Cox Regression model**, also called **Cox Proportional 
Hazards model**. It can be used to investigate several variables at the same time.

### Parametric Regression Models
We should first start with parametric regression models.

Suppose we want to analyze the survival time of some objects. One thing we
should consider is that there might be some other factors involved. We can model
the survival time or the hazard function by two parts:  
* baseline instantaneous hazard function -- $h_{0}(t)$;
* other independent variables(also called covariates).  
    to model it, consider that hazard function is always non-negative  
    so we can multiply $h_{0}(t)$ by a factor to adjust it  
    it turns out that the factor is $\exp (\mathbf{x}^{T}\mathbf{\beta})$

Finally, we get:  

$$h(t|\mathbf{x})=h_{0}(t) \exp (\mathbf{x}^{T}\mathbf{\beta}).$$

It's called **proportional hazard rate model**.

### Cox Proportional Hazards Model

> **!!! I don't know if I get this part right!!! The material in book1 and book2 
are not sufficient. I tried to refer the [origin paper written by Cox in 1972](http://www.medicine.mcgill.ca/epidemiology/hanley/c626/cox_jrssB_1972_hi_res.pdf),
but I can't fully understand it by the time I wrote this essay.**

Proportional hazard rate model is good. But, wait a minute, how to define the
baseline hazard function? Actually, in many cases, we don't need to define it.
Let's say we are performing a drug test. The usual way is to divide patients
into several groups.
To make it simple, let's assume that there are only one independent variable--group, for example.

So, we have:  

$$
h_{i}(t_{j})=h_{0}(t_{j}) \exp(z_{i}\beta).
$$

Here, $i$ denotes subject $i$; $z_{i}$ denotes the groups. If $z_{i}=1$,
subject $i$ is in the experimental group, else it's in the control group.
For writing simplicity, let us simplify the formula to:  

$$
h_{i}(t_{j})=h_{0}(t_{j}) \exp(z_{i}\beta)=h_{0}(t_{j}) \psi_{i}.
$$

Now, let's consider the probabilty for subject $i$ actually failed in the period
$t_{1}$, we use $p_{i1}$ to denote the figure.

But, before we move forward, we shall consider one question--what's the 
defination of hazard function for discrete $r.v.$? Review:  

$$
h(t)=\frac{\frac{d}{dt}F(t)}{S(t)}=\frac{f(t)}{S(t)}.
$$

For continuous $r.v.$, $f(t)$ is pdf. So, for discrete $r.v.$, $f(t)$ should be
pmf, analagously. So, we can re-write the formula to:  

$$
h(t)=\frac{\text{Pr}(X=t)}{1-F(t-1)}=
\frac{\text{Pr}(X=t)}{\text{Pr}(X\ge t)}=\text{Pr}(X=t|X\ge t).
$$

(I replace $S(t)$ to $S(t-1)$, because we are considering the discrete $r.v.$.)
Now, back to $p_{i1}$. We say $p_{i1}$ is the probabilty of subject $i$ fail in
period $1$. This can be state in another way: the probability for subject $i$
fail in period $1$, given that there is(are) fail(s) in period $1$. First, we
have:  

$$
A=\{i \text{ fail in period }1\}, 
B=\{\text{there is(are) fail(s) in period $1$}\}\\
A \subset B \Rightarrow A \cap B= A.
$$

Second, is what we want:  

$$
\begin{align*}
p_{i1}=\text{Pr}(A|B)&=\frac{\text{Pr}(A\cap B)}{\text{Pr(B)}}\\
&=\frac{\text{Pr}(A)}{\text{Pr(B)}}\\
&=\frac{\text{Pr}(X_{i}=t_{1}|X_{i}\ge t_{1})}
{\sum_{j:X_{j}\ge t_{1}} \text{Pr}(X_{j}=t_{1}|X_{j}\ge t_{1})}\\
&=\frac{h_{i}(t_{1})}{\sum_{j:X_{j}\ge t_{1}} h_{j}(t_{1})}\\
&=\frac{h_{0}(t_{1})\psi_{i}}{\sum_{j:X_{j}\ge t_{1}} h_{0}(t_{1})\psi_{j}}\\
&=\frac{\psi_{i}}{\sum_{j:X_{j}\ge t_{1}}\psi_{j}}.
\end{align*}
$$

In the end, the baseline hazard functions all have been canceled out.
(I have to say that I refered to [the essay written by Ravi Charan](https://towardsdatascience.com/the-cox-proportional-hazards-model-35e60e554d8f) a lot.
So much thanks I shall give to him. Besides, The calculation here actually is
based on that there will not be two or more subjects fail at the same period.
So that we can use the third axiom of probability in the denominator.)

$p_{i2}, p_{i3}, \cdots$ can be calculate similarly. Based on the actual order
of the failure, a partial log likelihood function can be construct, then we can
estimate the parameter of the independent variable, here is the group.
