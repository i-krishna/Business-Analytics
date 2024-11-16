AI vs ML: Artificial Intelligence (AI) refers to machines that can simulate human intelligence to sense, reason, act, empathize, or adapt like a human. Examples include Apple's vision technology, Amazon Alexa, and Meta’s Code LIama. Machine Learning (ML) refers to a subset of AI that empowers machines to learn and improve using algorithms (such as linear regression, HOG, CNN) to analyze large amounts of data. Alternative definition of ML: Machine learning is a subfield of computer science that means "the programming of a digital computer to behave in a way which, if done by human beings or animals, would be described as involving the process of learning." That's a 1959 definition by Arthur Samuel, a pioneer in computer gaming and artificial intelligence

# Spatial Data Science by Krishna Damarla

The below map is a graphical representation of the London underground transport system (commonly known as the Tube). To explain it to a transportation manager with no technical background on spatial data analysis (Rey, et al., 2020), I will use the following points: 

1. Zone Information (Transport for London, 2024): The map divides London city into 9 zones (see numbers at top of the map: 1 to 9), helping travelers understand transportation costs and travel distances from point A to point B. For instance, price from Zone 1 to Zone 2 my cost less (say £5), while price may increase to £25 for travelling from Zone 1 to 9, as these zones are located at opposite ends.

2. Color-Coding: Each line on the map is represented by a unique color, making it easier for passengers to distinguish different lines. For example, the Bakerloo Line is brown, the Central Line is red, the Jubilee Line by silver, etc.,

3. Transfers: Stations wherein passengers can transfer between different lines are marked with white circles, highlighting them on the map for easy transfer from one line to another.

4. Landmarks: The map additionally consists of important landmarks, like stations with connections to other transportation modes, along with country wide rail offerings and airports (see entire list of symbols utilized at the bottom left of the map).

The 2D map of a city transportation may seem complex at first. However with a background in data science and design, I aim to go beyond conventional mapping techniques. By integrating principles of spatial data analysis into interactive digital maps combined with computer graphics, AR (Augmented Reality), and parallel reality, I create personalized travel experiences for passengers selected routes. Major airlines (Delta Air Lines, 2022) already have such projects in place, enhancing their passengers journey experience as they travel from Gate A to Gate Z within airport area. Such projects can provide foundations for wider use in creating digital neighborhoods and entire digital cities (Anselin,  2020).

![image](https://github.com/i-krishna/Business-Analytics/assets/114757733/93ad3b40-3c67-489c-8814-786e4b607715)

References

Anselin, L. (2020). Week 1a: What is spatial analysis? (Introduction to Spatial Data Science). University of Chicago. Retrieved from https://www.youtube.com/watch?v=JwHxJsesG2Y&t=2s 

Delta Air Lines. (2022). The PARALLEL REALITY™ experience. Delta News Hub. https://news.delta.com/mediakit/parallel-realitytm-experience https://news.delta.com/mediakit/parallel-realitytm-experience 

Rey, S. J., Arribas-Bel, D., & Wolf, L. J. (2020). Geographic Thinking for Data Scientists. Retrieved from https://geographicdata.science/book/notebooks/01_geo_thinking.html

Transport for London. (2024). Tube map. Retrieved from https://tfl.gov.uk/maps/track/tube

# Collective Intelligence in Predictive Analytics by Krishna Damarla

In predictive analysis, we can use existing bigdata to train AI models to make predictions. One of the disadvantages of this type of prediction is that we need clean data or spend time cleaning bad data or have only limited data. Sometimes we need to predict uncertain events, such as epidemics and elections, without sufficient data. In those cases, where AI stops, crowd prediction begins (Smarter Together, 2023). 

The concept of the crowd prediction or wisdom of crowds (aka, collective intelligence) can best be understood from the popular TV show – Who Wants to Be a Millionaire ? In this show, player can choose to answer the final question by calling an expert friend or by asking audience for help. Research shows that audience votes help player win the game with an 89% accuracy rate (HyperMind, 2021), whereas, Calling a friend, on the other hand, is only 54% accurate, which is almost same as tossing coin (StoryWorks, 2024). So, approximately 1337 times answers were accurate on audience poll, with only 147 times being incorrect.

Let’s consider a case study of Johns Hopkins Center for Health Security, which predicts outbreak of infectious diseases. Two crowd groups were included in this study to provide valid forecasts.
1.	Crowd 1 (Industry Experts): 70% public health experts. Example: Medical epidemiologists, microbiologists, etc. 
2.	Crowd 2 (Forecasting Experts): 30% skilled forecasters. Example: Hyperminds prediction team of market analysts.

The 2 groups mentioned above were asked to enter their answers into a central platform with questions to assess the severity of the outbreak. Sample question looked like: How many states report over 1000 infectious cases by March end. The outcomes could help governments create better policies or make more informed decisions. The results showed good forecasters are more likely to be open-minded, prone to criticism / negative views (Smarter Together, 2023). Using crowd intelligence to improve predictions go beyond policymaking to understanding operations, disaster management, global economics, and geopolitics.

References

HyperMind. (2021). The Wisdom of Crowds: The Science of Getting Smarter Together. YouTube. https://www.youtube.com/watch?v=HNQ3GccCAI0 

StoryWorks. (2024). E80 - The Wisdom of Crowds. YouTube. https://www.youtube.com/watch?v=jvgPPiWN7yU 

Smarter Together. (2023). Crowd Forecasting: how Johns Hopkins harnessed the wisdom of crowds to predict infectious disease. YouTube. https://www.youtube.com/watch?v=z-V-lPzBVA4 

# Kaggle Overview and Competition Submission by Krishna Damarla

Kaggle Overview 

Kaggle is a platform for data science enthusiasts to improve their prediction skills through building ML (Machine Learning) models, and visualizing data, while contributing to the community. My Kaggle homepage highlights the three main features of the platform: 
1.	Search for competitions, explore datasets and understand models.
2.	Learn programming and ML through notebooks, courses, and peer discussions.
3.	Measure progress through contributions and user ranking.
Other features include hosting competitions, mentorship, and an introduction to Kaggle's CEO (formerly from Google Brain) and his crew.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/c517b583-d026-43bf-b3ab-c0a5f7129c11">

Competitions

Before entering the competition, it's important to understand six points (Rashed, 2021):
1.	Overview: Identify evaluation metric used (mean average precision in this competition), submission file data types, and the start (April 4) / end date (July 8) of the competition.
2.	Data: The dataset consists of binary classification with train.csv and test.csv files, and our goal is to predict three targets. Instructions on submission file format are also provided.
3.	Code & Models: Submissions can be filtered by votes. The Random Forest and ECFP models have been the winning models in this competition. 
4.	Discussions: In addition to the discussion thread on the Kaggle, there is also a  Discord channel for this competition. 
5.	Leaderboard: The winners are determined by public score of candidate’s based on their submissions.
6.	Rules: Maximum of 5 submissions per day, and teams cannot exceed 5 people. The prize distribution are as follows. 

<img width="468" alt="image" src="https://github.com/user-attachments/assets/8f2f0024-1103-4523-b46a-873d84d74c13">

Submissions to Competition

In this section, I will explain how to submit prediction’s to the famous “Titanic Disaster Survival” competition. 

1. Search for the competition: Search by keyword “Titanic” from Host: Kaggle (Knowledge category instead of Kudos)

<img width="468" alt="image" src="https://github.com/user-attachments/assets/44a93555-642b-418d-beb2-93a64140fda6">

2. Submit prediction: We can submit as a CSV file or as a Zip pf CSV’s. There are two ways to submit.
 
<img width="468" alt="image" src="https://github.com/user-attachments/assets/36f53097-2774-4570-a5f4-65e8f3b04bd2">

1.	Direct upload via GUI (I chose this option): Based on the Titanic disaster survival input dataset, the prediction results from our presentation are as follows:
•	Titanic_Gender.csv:  The public score that only female passengers will survive is around 0. 76. 
•	Titanic_Perfect.csv: The public score of survival with a perfect dataset is 1.00
•	Titanic_Random.csv: The public sore of survival with randomly selected dataset is around 0.51.
2.	Command line 

Reference

Rashed, A. (2021). Making a submission to Kaggle competitions. YouTube.  https://www.youtube.com/watch?v=3oRFyuj4udI&t=2s 

# Wine Rating Analysis by Krishna Damarla

The following is a summary of wine ratings analysis extracted from the [Excel](https://github.com/i-krishna/Business-Analytics/blob/main/Data-Science/Statistics/Regression_WineRatingsAnalysis.xlsx), where each of the eight worksheets in the file corresponds to the eight points outlined below.

1. Table (Anderson et al., 2020): A pivot table was created to calculate the average wine price, score, and count of wine bottles per rating category. The analysis reveals a clear relationship between price and rating score, indicating that higher scores generally correspond to higher wine prices. Upon conducting initial summary and descriptive statistics, it was observed that classic wine has the highest average price among all categories, standing at $269.57, with an average score of 96.4. Further, most wine bottles are concentrated in the outstanding (40 bottles) and very good (45 bottles) categories, with average prices of $73 and $30.4, respectively. Notably, the mediocre category includes only one wine bottle priced at $21, which also exhibits the lowest rating score of 78.
 
2. Scatter Diagram: Correlation analysis demonstrated through a scatterplot, revealed a positive linear correlation between price (horizontal x-axis) and Wine rating score (vertical y-axis), indicated by the upward trendline.

3. Linear Regression Model (Anderson et al., 2020): Employing linear regression analysis in Excel, linear regression equation of y = 87.763 + 0.028 * x was derived to predict the wine rating score (y) based on the price of the wine (x).

4. Second-Order Regression Model (Foltz, 2013): Further, a second-order model regression equation was formulated as y = 86.1659 + 0.0713 * x - 0.0001 * x^2 to forecast the wine rating score (y) considering the price of the wine (x).

5. Comparison of Linear and Second-order Regression Models: Evaluation of R^2 (coefficient of determination) results indicates that the second-order model is a superior fit for predictions, attributed to its higher R^2 value in comparison to the linear model.

6. Logarithmic Regression Model (Foltz, 2020): A logarithmic regression equation with natural logarithm of price as the independent variable was developed: y = 77.731 + 3.156 * ln(x), presenting a potentially better fit (˜57.6% model reliability for prediction) than the second-order model.

7. Conclusion: Analysis conclude that spending more price for a bottle of wine will provide a better wine quality, supported by the Logarithmic regression model test statistics with a P-value of 5.89783E-20 at a 95% confidence interval (P <= Alpha).
 
8. Prediction (Sanderson, 2023): Considering a maximum budget of $30 for a bottle of wine, the prediction interval indicates that investing closer to the upper price limit does not guarantee a superior wine quality compared to a significantly lower price, highlighting the wider prediction interval.

References

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Foltz, B. (2013). Statistics 101: Multiple Linear Regression, The Very Basics. YouTube. 

Foltz, B. (2020). Statistics 101: Model Building, GLM Relationships Between ANOVA and Linear Regression. . YouTube.

Sanderson, S. (2023). Logarithmic Regression in R: A Step-by-Step Guide with Prediction Intervals. R bloggers. https://www.r-bloggers.com/2023/11/logarithmic-regression-in-r-a-step-by-step-guide-with-prediction-intervals/

<img width="1098" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/259a82a7-1905-4009-ab51-d1b08c1286c1">

![image](https://github.com/i-krishna/Business-Analytics/assets/114757733/15b9fa92-881a-45d5-ab22-1e157c551798)


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

**References**

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Jalayer Academy. (2019). Simple Linear Regression Example. YouTube. https://www.youtube.com/watch?v=apRkIy73sxg

PennState Eberly College of Science. (2023). Regression Methods. https://online.stat.psu.edu/stat501/lesson/1

<img width="920" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/5fdd369e-f707-4bcb-8930-97c0e8055bf9">

<img width="902" alt="image" src="https://github.com/i-krishna/Business-Analytics/assets/114757733/586dd641-6e09-4e25-a975-941922c235cc">

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

**References**

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

Datatopia. (2023). Retrieved from https://www.datatopia.be/en/home-en  

Learning Puree. (2019). What is Descriptive Statistics [Examples and Concept - Mean Median Mode]. YouTube. https://www.youtube.com/watch?v=B_kWOlxxQYo 

Morse, S. (2020). Humana is expediting claims processing and prior authorization during COVID-19 pandemic. Healthcare finance. 
https://www.healthcarefinancenews.com/news/humana-expediting-claims-processing-and-prior-authorization-during-covid-19-pandemic 


Tools:
- Excel Data Analysis Toolpak
- R
- https://www.palisade.com/decisiontools_suite/

<img width="885" alt="image" src="https://github.com/user-attachments/assets/1bd3fc76-da56-459a-91cd-d2f5b47e80c5">

# Forecasting Food and Beverage Sales by Krishna Damarla

The attached Excel primarily emphasizes the following three concepts, aimed at assisting Karen in making informed business decisions.

1. Time Series Analysis:
The time series plot illustrates the sales of the Vintage Restaurant over the past 3 years of operation. It demonstrates a noticeable seasonal pattern coupled with a horizontal trend in the data. Each year exhibits a consistent pattern, as highlighted by distinct colors representing individual years in the background of the plot. The data revolves around a relatively stable mean value (Research By Design, 2020).

Specifically, during the 9th month (3rd quarter) of each year, the lowest sales are recorded. Subsequently, there is a gradual uptick in sales from the 9th month onwards, culminating in peak sales during the 1st month (1st quarter) of each year. The horizontal x-axis denotes the month, spanning from 1 to 36 with increments of 1. Beneath the x-axis, data labels indicate the corresponding sales value for each month. The vertical y-axis represents the sales value, ranging from 110 to 282. The plot encompasses 36 data points, with a line traversing these points, explaining the trend and seasonality in the sales data over the three-year operational period.

2. Time Series Decomposition:
The calculated seasonal indexes unveil that month 1 boasts the highest seasonal sales index, closely followed by month 3. Conversely, month 9 registers the lowest seasonal sales index, with month 10 ranking second lowest.

These seasonal indexes align seamlessly with intuitive expectations. Months 1 and 3 typically coincide with peak tourist seasons, contributing to heightened sales. In contrast, months 9 and 10 often represent off-peak seasons, resulting in diminished sales. This analysis harmonizes with the observed seasonal pattern depicted in the time series plot.

Deseasonalized values facilitate the removal of the seasonal component from the time series data, enabling a clearer understanding of underlying trends. The forecasted monthly sales values derived using time series decomposition, for the entire fourth year unveil intriguing patterns (Dr. Harper's Classroom, 2016).

3. Dummy Variable Regression:
The forecast equation for sales is computed, yielding a predicted sales value of $262,334 for year 4, month 1 (January). However, the actual sales value stands at $295,000. This discrepancy results in a forecast error of $32,666.

To mitigate forecast error, I recommend Karen to retrain the model by considering additional variables beyond sales data. Integrating other pertinent factors such as customer demographics, marketing strategies, economic indicators, and seasonal influences can enhance the accuracy of predictions and reduce forecast errors (Anderson et al., 2020).

References

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Dr. Harper's Classroom. (2016). Time Series Decomposition Using Excel. YouTube. 

Research By Design. (2020). Time Series Analysis for Business Statistics (part 1). YouTube.

# Decision Tree Analysis by Krishna Damarla

In the attached Excel file, the first worksheet illustrates the decision tree and its logical sequence of nodes for solving the decision problem of Oceanview Development Corporation (ODC). 

In second worksheet, we recommended what ODC should do when the market research information is not available. For instance,  Node 5 specifies the scenario when no market research is utilized in the bidding process. If no bid is submitted in this scenario, costs are 0$ for Oceanview Development Corporation. If bid is submitted and the zone change request is not approved, ODC can forfeit the actual bid amount without any loss. As the expected value of submitting bid is positive, there is possibility of losing deposit if zone change request is not approved.  

In third worksheet, It is advised to OCD to submit a bid if the market research successfully predicts the approval of the zone change request. Conversely, if the market research fails to predict the approval of the zone change request, it is advisable not to submit a bid.

In the fourth worksheet, the expected value of sample information (EVSI) is computed using the formula: EVSI = EV with Perfect Information (EVwPI) - Maximum EMV. In our case, EVSI is $247,700. Therefore, the corporation would need to pay $247,700. Given the high EVSI value, it can be concluded that investing on market research analysis is not recommended. 

References

Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D., & Cochran, J. J. (2020). Modern Business Statistics with Microsoft Excel (7th ed.). Cengage Learning.

Emmanuel, J. (2015a).  Decision Analysis 3: Decision Trees. YouTube. 

Emmanuel, J. (2015b).  Decision Analysis 1: Maximax, Maximin, Minimax Regret. YouTube. 

<img width="1050" alt="image" src="https://github.com/user-attachments/assets/482608e7-ca67-4cb4-84b4-e1bb4f6b6126">

<img width="872" alt="image" src="https://github.com/user-attachments/assets/e1f9441b-ffc6-43a5-afa0-beeb5d6572b0">




