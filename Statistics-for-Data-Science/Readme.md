
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
