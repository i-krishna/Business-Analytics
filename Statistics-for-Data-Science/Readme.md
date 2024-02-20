# Simple Linear Regression by Krishna Damarla

## Infographic 

https://www.canva.com/design/DAF8QfkZUA8/C67-IMhT3tOYeVBH9DFSLQ/edit?utm_content=DAF8QfkZUA8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

The above infographic defines simple linear regression as a statistical method to model the linear relationship between two continuous variables (Anderson et al., 2020) and explains its principles with an example of predicting the price of used cars based on an odometer reading.

Here's the summary of the design (Jalayer Academy, 2019):

Step1: Understand Data: A scatterplot was built on the sample data to visualize the strong negative correlation between used car prices and odometer readings. The scatterplot shows that the price (dependent variable / Y-axis ) changes based on the odometer (independent variable / X-axis) reading.

Step 2: Train Model: Model was trained on the sample data from step 1 and regression statistics were computed in Excel. This step involved determining the slope, y-intercept of the regression line, as well as assessing the R-squared value to evaluate the model's reliability for prediction.

Step 3: Make Predictions: The linear regression equation derived from the model in step 2 is used for predictions of used car prices. For example, the predicted price of a used car with an odometer reading of 30,000 miles was calculated as approximately $15,855 with a margin of error of $1,482.72 (PennState Eberly College of Science, 2023). 
 
Used_car_price = 17160 + (-0.087) * odometer ± Standard_Error

Where,
Used_car_price is the value to be predicted based on given odometer reading.
17160 is the y-intercept of the estimated regression line.
-0.087 is the slope of the estimated regression line.
Standard error as depicted in the infographic is used to measure the accuracy of the estimated regression coefficients, such as the slope and the intercept. A smaller standard error suggests that the regression line is a better fit for the data and provides reliable predictions (Anderson et al., 2020).
Conclusion: As mileage increases, the price of the used car decreases. This is also supported by the negative slope / correlation between price and odometer readings seen in the scatterplot.

## References

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Jalayer Academy. (2019). Simple Linear Regression Example. YouTube. https://www.youtube.com/watch?v=apRkIy73sxg

PennState Eberly College of Science. (2023). Regression Methods. https://online.stat.psu.edu/stat501/lesson/1


# Chi-Square Fitness and Independence Test by Krishna Damarla

Chi-Square Goodness of Fit and Independence tests are designed for categorical data based on a single sample from a single population.

## Chi-Square Goodness of Fit

1. Definition: Determines whether a variable meets a specific probability distribution (Anderson et al., 2020).

2. Importance / Application: Test whether the frequency distribution of categorical data follows the assumption of hypothesized distribution. It is widely used in business research, and quality control to determine if the observed frequencies match with expected frequencies and to detect any deviations from the expected distribution.

3. Example: Research study, testing historical market shares of three companies (A, B, and C) based on new product introduction by Company C (Anderson et al., 2020).

3a. Hypotheses (The Organic Chemistry Tutor, 2019a):
• Null Hypothesis (H0): The introduction of new product will not alter shares.
• Alternative Hypothesis (Ha): The introduction of new product will alter shares.

3b. Test Statistic: Test involve comparing observed and expected frequencies using the chi-square test statistic formula as shown below (Anderson et al., 2020).

Formula <img width="181" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/75c93b85-46e4-43c7-a1f2-9062ee9435cf">


The chi-square test statistic has k−1 degrees of freedom, where k is the number of categories (3 in this case). f is the observed frequency of category i and e is the expected frequency of category i

3c. P-value: If p-value falls between 0.05 and 0.025 at a significance level (α) of 0.05, and if P < α, we reject the null hypothesis.

3c. Critical Region: Instead of P-value, we can also use critical region to decide. Based on the data at hand, the critical area is between 5.991 to 7.378, i.e., >= chi-square test statistic 5.991. So, we reject the null hypothesis.

4. Conclusion: Rejection of null hypothesis (H0) shows that the new product will likely alter historical market shares.

## Chi-Square Test of Independence by Krishna Damarla

1. Definition: Determine the independence of two categorical variables from the same population (Anderson et al., 2020).

2. Importance / Use: Determines whether the observed frequencies differ from expected frequencies under the assumption of independence. It is widely used in industries such as social sciences, marketing, and medicine, to investigate the relationship between categorical variables and make decisions based on observed data.

3. Example: A beer industry conducts survey on beer preferences (mild, regular, strong) by gender (male, female), to determine if preferences are independent (Anderson et al., 2020).

3a. Hypotheses (The Organic Chemistry Tutor, 2019b):
• Null Hypothesis (H0): Beer preference has nothing to do with gender.
• Alternative Hypothesis (Ha): There is a relationship between beer preference and gender.

3b. Test Statistic: The test is based on comparison of observed and expected frequencies in a contingency table. Formula is as shown below (Anderson et al., 2020).

Formula <img width="193" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/ded0efce-48fe-4d6a-a152-4711faf3240c">

Where, fij represents the observed frequency in the ith row and jth column, and eij
denotes the expected frequency in the ith row and jth column. The degrees of freedom of chi-square test statistic is given by (r−1)(c−1),and are determined by the number of rows (r) and columns (c). In this case, there are three beer preferences (r=3) and two genders (c=2), with degrees of freedom (3−1)(2−1).

The Excel formula of CHISQ.TEST(actual_range, expected_range) can also be used to determine the Chi-Square test of independence (Microsoft, n.d).

3c. P-Value: Based on statistic test, we determine that P < α. Therefore, we reject the null hypothesis.

4. Conclusion: There is a relationship between beer preference and gender.

## References

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Microsoft. (n.d). CHISQ.TEST function. https://support.microsoft.com/en-gb/office/chisq-test-function-2e8a7861-b14a-4985-aa93-fb88de3f260f

The Organic Chemistry Tutor. (2019a). Chi Square Test. YouTube.


The Organic Chemistry Tutor. (2019b). Hypothesis Testing - Difference of Two Means - Student's -Distribution & Normal Distribution. YouTube.

<img width="1110" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/d609d2b3-1e5b-49eb-ab78-9d63d014f6e3">

# Sampling distributions, interval estimation & hypothesis testing by Krishna Damarla

**Infograph**

https://www.canva.com/design/DAF68mqg1GE/ZkRy4_shfKg-aoeXjJv2jg/edit?utm_content=DAF68mqg1GE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

**Infograph Explanation**

The Infograph illustrates three key statistical concepts, each with a specific example as discussed below.

**Sampling Distributions**
Context: Analyzing the heights of basketball players.

1.	Population Distribution: Illustrated by the violet graph, it showcases basketball players' heights with a mean (μ) of 63 inches and standard deviation (σ) of 2.165 inches.
2.	Sample Means Distribution: Displayed in orange and green graphs, this demonstrates how the distribution of sample means progressively normalizes as sample size increases from n=2 to n=30, in accordance with the Central Limit Theorem.
3.	Standard Error: Highlighted as 2.165 / √n, it underscores how standard error diminishes as sample size grows.

**Interval Estimation**
Scenario: Determining the average weight of apples in an orchard.

1.	Interval Estimate: A sample mean weight of 150 grams, with a 10-gram margin of error, at a 95% confidence interval ranges from 140g to 160g. Interval = Point estimate ± Margin of Error = 150 ± 10= [140, 160]
2.	Influencing Factors: The interval's width is influenced by the variability in apple weights and the size of the sample. It also depends on the known (z-score) or unknown (t-score) status of the population's standard deviation, and on the selected confidence level, whether it’s 95% or 99%.

**Hypothesis Testing**
Example: Evaluating the effectiveness of a new drug versus an existing drug by a pharmaceutical company.

1.	Hypothesis Formulation: The null hypothesis (H0) suggests no enhanced efficacy for the new drug, while the alternative hypothesis (H1) supports increased effectiveness.
2.	P-Value & Test Statistic Calculation: Employed to gauge the evidence against H0.
3.	Interpreting Results: A p-value below 0.05 leads to rejecting H0, implying the new drug’s superior effectiveness. Conversely, a higher p-value indicates inadequate evidence to assert the new drug's superiority.

**References**

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.
 
Dr Nic's Maths and Stats. (2013). Hypothesis testing: step-by-step, p-value, t-test for difference of two means - Statistics Help. YouTube. https://www.youtube.com/watch?v=0zZYBALbZgg

Dr Nic's Maths and Stats. (2013). Understanding Confidence Intervals: Statistics Help. YouTube. https://www.youtube.com/watch?v=tFWsuO9f74o

Emmanuel, J. (2016). Sampling Distribution - Central Limit Theorem - Normal Distribution. YouTube. https://www.youtube.com/watch?v=hqiMcHqlZ4s

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55
Venngage - Visualize your ideas. (2018). The 9 Types of Infographics [TIPS AND EXAMPLES]. YouTube. https://www.youtube.com/watch?v=tN8_85gKOTc

**Comments**
significance level, denoted by alpha (α) is a critical value to determine the threshold at which you reject the null hypothesis (H0), setting context to discuss further about the 3 key questions Dr. Allua Mam has posed.

1. What factors should be considered when assigning the alpha level?

The choice of α depends on sample size, the researcher's judgment, specific requirements, nature, and goals of the study. Selecting an alpha level may also need to align with the power of test, established standards in certain industries / fields as it involves a trade-off between the risks of Type I and Type II errors (Kim, 2015).

When conducting hypothesis testing, we usually set ‘α’ to define the probability of making a Type I error (rejecting a null hypothesis). At 95% confidence level, α = 1 – 0.95 = 0.05. Commonly used significance levels (α ) are 0.05, 0.01, or 0.10 (PennState Eberly College of Science, 2023a). 


2. What implications does a more stringent have on the results?

Larger samples may allow for more stringent alpha levels (e.g., 0.01 at 99% confidence level) with the following implications (Marcos, n.d).

1. Reduces the likelihood of Type I errors (false positives).
2. Increases the risk of Type II errors (false negatives).
3. Requires stronger evidence to reject the null hypothesis.

3. What situations would one use a more stringent vs a less stringent alpha level?

More stringent alpha level is critical in situations with high stakes or serious consequences for Type I errors (e.g., medical research) and when demanding a higher level of confidence in results. Less stringent alpha level is appropriate in exploratory studies or situations where Type II errors are less critical and a balance between Type I and Type II errors is acceptable (PennState Eberly College of Science, 2023b).


# Discrete Vs Continuous Probabilities by Krishna Damarla

**Infographic**

https://www.canva.com/design/DAF6SRZAAIo/foyXGe6LM_y1sfWuI0udGg/edit?utm_content=DAF6SRZAAIo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

**Infographic Explanation**

Above infographic offers a comprehensive exploration of discrete and continuous probabilities, which are fundamental concepts in probability and statistics for analyzing different types of data. Discrete probabilities, which deal with countable outcomes, utilize a probability function f(x) to enumerate all possible outcomes, typically involving summation in their calculations. In contrast, continuous probabilities cover a range of values and use integration in their calculations, with the probability density function (PDF) determining probabilities as areas under a curve. Both types of probabilities consider mean and variance as crucial statistical metrics, calculated in distinct ways as depicted in the infographic. The infographic further highlights key distributions in discrete probability such as Binomial distribution, which is often used in survey analysis; the Hypergeometric distribution, crucial in quality control; and the Poisson distribution, applied in traffic analysis. For continuous probabilities, the Uniform distribution is key for random time selection, while the Normal (Gaussian) distribution is widely used in analyzing stock market trends, and the Exponential distribution is crucial for lifespan predictions.

**References**

Akshay Pachaar. (2023). Discrete & continuous random variables. https://twitter.com/akshay_pachaar/status/1668234250343305216/photo/1. Twitter. 

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.
CalcWorkshop (2020). Expected Value & Variance of Continuous Random Variable. https://calcworkshop.com/continuous-probability-distribution/expected-value-variance-continuous-random-variable/ ;

Genengnews. (2017). 16 Biomarkers May Predict Human Lifespan. https://www.genengnews.com/news/16-biomarkers-may-predict-human-lifespan/ ;

Learn Something. (2015). Discrete Probability Distributions. YouTube. https://www.youtube.com/watch?v=m9U4UelWLFs

Seema Singh. (2019). Probability Distributions: Discrete and Continuous. https://medium.com/@seema.singh/probability-distributions-discrete-and-continuous-7a94ede66dc0 ;

Sentiment analysis concept icon. (n.d). https://www.alamy.com/sentiment-analysis-concept-icon-client-satisfaction-survey-idea-thin-line-illustration-customer-reviews-feedback-service-rating-content-analysis-image340602884.html ;

Skills Factory. (2023). Canva - Tutorial for Beginners in 13 Minutes. YouTube. https://www.youtube.com/watch?v=6M8axhCQP7M

The Organic Chemistry Tutor. (2019). Continuous Probability Distributions - Basic Introduction. YouTube. https://www.youtube.com/watch?v=QxqxdQ_g2uw

Venngage - Visualize your ideas. (2018). The 9 Types of Infographics [TIPS AND EXAMPLES]. YouTube. https://www.youtube.com/watch?v=tN8_85gKOTc




# Optimizing Claim Management with Descriptive Statistics by Krishna Damarla


**Descriptive Statistics: Definition and Examples**

Descriptive statistics is a method focused on summarizing and structuring data in formats that are straightforward and easily understandable / accessible, such as tables, graphs, numerical reports. This approach typically encompasses calculations of the mean (average), median (middle value), mode (most common value), as well as indicators of data spread like the range and standard deviation (Anderson et al., 2020).

For example, an analysis of daily energy levels on a scale of 1 to 5 might reveal an average (mean) of 3.2, suggesting a generally moderate energy level. Mean is usually used for data with repetitive patterns. The median is used in scenarios where data has more extreme values, like income range from $20,000 to $200,000. Finding the middle value, offers a more accurate version of the 'average' in such scenarios. Similarly, for a retail business like a shoe store, identifying the most frequently sold shoe size of 8 (mode) can be crucial for inventory management (Learning Puree, 2019).

**Summary of Business Problem**
The primary issue faced by a health insurance company, such as Humana (Morse, 2020), involves the efficient handling of a varied and extensive array of claims while maintaining accuracy, reducing processing duration, and enhancing customer satisfaction. These claims differ in complexity and occurrence rate, necessitating timely and fair treatment for insured individuals.

**Descriptive Statistics in Addressing the Challenge**

Descriptive statistics play a pivotal role in comprehending the characteristics of the claims. For instance, an observed mean processing time of 15 days, with a median of 10 days, indicates a skew in processing times.

For instance, a few very complex claims that took a significantly longer time to process could raise the average (mean), even if most claims are processed more quickly. Such a disparity indicates that while the average time is 15 days, the median (less influenced by extreme values) reflects that half of the claims are processed in 10 days or fewer. This disparity can signal the need for process refinement, especially for claims that take longer than usual. 
Additionally, identifying the most frequent type of claim (mode), enables strategic resource allocation and specialized team deployment for more common claim categories (e.g., claims based on COVID-19 infection during the pandemic period).

**Utilizing Descriptive Statistics to Tackle the Business Problem by Krishna Damarla**

Humana can leverage insights from descriptive statistics, such as average processing times and prevalent claim types, to optimize resource distribution and expedite processing for more frequent claim categories.

Analyzing the distribution (range) and fluctuation (standard deviation, z-scores) in processing times is crucial for pinpointing exceptional cases that might require special attention. A notable dispersion in processing times or claim amounts, as indicated by a high standard deviation, suggests inconsistency in claim handling. Conversely, a low standard deviation signifies a closer grouping of values around the mean, indicating a more uniform process.

Implementing tools like Excel’s descriptive statistics, combined with the graphical capabilities of R (e.g., ggplot2 package), can illuminate patterns in processing times. Such patterns, presented in a visual format like a heatmap, can uncover specific claim types that disproportionately impact processing times (outliers), highlighting areas for enhancement or the need for specialized handling teams (Anderson et al., 2020).

These statistical insights, ideally showcased in a comprehensive dashboard or report, empower the insurance company to make informed decisions for streamlining operations, elevating customer satisfaction, and achieving more efficient claim management.

**References**

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Learning Puree. (2019). What is Descriptive Statistics [Examples and Concept - Mean Median Mode]. YouTube. https://www.youtube.com/watch?v=B_kWOlxxQYo 

Morse, S. (2020). Humana is expediting claims processing and prior authorization during COVID-19 pandemic. Healthcare finance. 
https://www.healthcarefinancenews.com/news/humana-expediting-claims-processing-and-prior-authorization-during-covid-19-pandemic 
