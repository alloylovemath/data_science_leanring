# Tests on Categorical Data

**Reference Book**:  
1. 《概率论与数理统计》（陈希孺，2009年2月第一版） -- Chen's book
2. *An Introduction to Statistics with Python* (Thomas Haslwanter) -- book1

## $\chi^{2}$ Test
The definition of the test is different in Chen's book and book1, I will follow 
the definition in Chen's book.

The $\chi^{2}$ test is a kind of goodness of fit test. By definition, it tests
whether the data of the sample shows it comes from some specific dis. 

The idea is, in short, we calculate a $\chi^{2}$ statistic which shows the
deviation between the real number in the data and the expect value.

There are two basic cases here:  
1. only one factor (but multiple levels or classes)
2. contingency table(列联表)

Math in different situations differ, but I won't cover it here. You can look
them up in Chen's book(page 233-243)

## Fisher’s Exact Test
**Example: A Lady Tasting Tea(R.A.Fisher)**  
I do believe the example above has significant meaning. However, book1 didn't
show me that...(In my opinion)
So, I use another book: ***Python for Probability, Statistics, and Machine
Learning*** (José Unpingco, page 163)

The question is whether or not the observed table corresponds to a random
partition of the sample population, constrained by the marginal sums. Note that 
because this is a two-by-two table, **a change in any of the table entries 
automatically affects all of the other terms** because of the row and column sum 
constraints.

In a $2\times 2$ contingency table, we get $r_{1}, r_{2}, c_{1}, c_{2}$
(row sums, column sums). Consider this question, if the number in each entry is
randomly select, what's the prob.?

Thought:  
1. The total number is $r_{1} + r_{2}$
2. we select $c_{1}$
3. what's the prob. for that the number of entry (1, 1) is $x_{1,1}$ ,
ther are of category $r_{1}$ ? ( $x_{1, 1}\le r_{1}, x_{1, 1}\le c_{1}$ ) 

Obviously, the prob. can be derived from the hypegeometric dis.  

$$
\textnormal{Pr}(x_{1, 1}=k) =
{\Large\frac{{r_{1} \choose k}{N-r_{1} \choose c_{1} - k}}{N \choose c_{1}}}
$$

Now, suppose the thing we want to proof, ie. the alternative hypothesis is
outcome tend to show up in (1, 1) less than randomlly selection, we shall 
calculate

$$ \sum_{i=0}^{k} \textnormal{Pr} (x_{1, 1}=i), $$

that is the p-value

## McNemar’s Test
I find a good explaination online that you can refer to: 
https://www.theanalysisfactor.com/difference-between-chi-square-test-and-mcnemar-test/
When the sample size is small (or $b+c$ is small, say smaller than 25),
we may use a binomial dis. to do the calculation
(similar to Fisher's exact test' idea), you can view the Wikipedia web page for
the detail

## Cochran’s Q Test
*pass*
