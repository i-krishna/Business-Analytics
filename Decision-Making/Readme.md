# 1. Health Insurance Analytics Experience by Krishna Damarla

Project Experience

In a project with an insurance client, I extracted data into a central data warehouse table for advanced analytics. At first, I worked with senior business analysts to understand the key business challenges and identified key performance indicators (KPIs) that directly affect enterprise operations. Later, I focused on cleansing, data modelling, and leveraging statistical, machine-learning models for descriptive and predictive analysis (Ariansen & Madecraft, 2022). This project culminated in recommending data-driven solutions to client to enhance their decision-making in business operations and marketplace positioning.

Tools Usage

In this project, I compared various business intelligence (BI) tools from major cloud vendors. I identified the pros and cons of these tools with a focus on client-specific reporting needs. This includes depth of analysis, chart selection, colour combinations, and data masking (security) for specific users. Although some BI tools offer customization, many fail, even with enterprise licenses. I decided upon Cognos due to its ease of on-premises integration, superior customization capabilities, data modelling options, and connectors for external data sources (Hiter, 2023).

Future Outlook

I am interested in learning about various techniques in integrating generative artificial intelligence (GenAI) into reporting and dashboard creation (Raghupathi & Raghupathi, 2021). For instance, enabling users to create reports with natural language commands like, "Create an interactive bar chart from recent sales data," which would then be converted into an SQL/NoSQL query. Such a query verified by developers would then pull information from the database, generate a creative report, and present it to the user for visual analysis. This type of innovation is cost-effective for non-technical clients, allowing them to save valuable time while enhancing their decision-making capabilities.

References

Ariansen, J. D., & Madecraft. (2022). Introduction to Business Analytics. LinkedIn Learning. https://www.linkedin.com/learning/introduction-to-business-analytics-14621877

Hiter, S. (2023). Cognos vs. Power BI: 2024 data platform comparison. eWeek.com.  https://www.eweek.com/cloud/cognos-vs-power-bi/

Raghupathi, W., & Raghupathi, V. (2021). Contemporary business analytics: An overview. MDPI Journal. https://doi.org/10.3390/data6080086

<img width="958" alt="image" src="https://github.com/user-attachments/assets/34f59064-a8af-4b01-9a50-0c7bc27b100d">

# 2. Healthcare Analytics Experience by Krishna Damarla

<img width="957" alt="image" src="https://github.com/user-attachments/assets/c293fe49-0909-4ae2-a260-37a3738894b3">

Code to Implement above Suggestion: [face-recognition.py](../Data-Science/Python/face-recognition.py)

Note: The above code snippet is intended for scenarios where a person's face has already been trained using a predefined set of images in a training model. In real-world applications, recognizing the face of an unknown individual requires using a government-approved ID and photograph to train the model, enabling it to match the person in live video for recognition purposes. Implementing such an architecture must align with healthcare security practices and regulations of local body, such as HIPAA in the U.S, PIPEDA in Canada, GDPR in Europe, DISHA in India, and PIPL in China.

# 3. Reporting Transformation at Landon Hotels with Tableau by Krishna Damarla

## Issue

Landon Hotels utilize Excel spreadsheets for reporting. Due to potential expansion of company, this model of reporting does not scale to meet the dynamic, complex requirements of the firm. To date, 360 employees use reports for analysis. Of these, 30 managers and 10 Business Intelligence (BI) team members create static Excel reports, creating confusion and lack of standardization across the organization. Without a centralized framework at place, employees led by these leaders are also vulnerable to such inefficiencies (Ngwena, 2022).

## Solution 

To address these issues, Landon Hotels plan to use Tableau to transition from static reporting to dynamic reporting. This change will enable real time data visualization and deliver accurate insights from a single source of truth across the organization. Further, they are focusing on deploying automated data pipelines to ensure timely data delivery for reporting. A Tableau deployment plan will be created with KPIs to track progress and measure success. In addition, the firms existing IT infrastructure management will be outsourced to third party provider (Red30) to integrate the new solutions into its cloud-based platform. Finally, the company is looking for turnkey training programs to equip its employees with the skills needed to use the newly implemented solution (Ngwena, 2022). 

## Key Lessons Learned and Reevaluations

**1. Strategic Planning**

I learned to create a clear plan for successful delivery. Using Tableau Blueprint (Baldwin, 2016) can further help align projects with company goals and create KPIs to track progress. This study also taught me that planning is as important as implementation. And, to consider the impact of external influences throughout all the phases of project from deployment to maintenance.

**2. User Groups and Licensing**

I learned that to determine the appropriate Tableau licenses, I needed to understand different roles of users, and their level of involvement in the organization. For example, the BI team needs access to Tableau Desktop and Prep Builder (Baldwin, 2016) as Creators, while managers and employees need Explorer and Viewer licenses, respectively. 

Previously, I focused more on creating technical solutions, than clustering user groups. This business case taught me that users should be assigned different types of licenses to avoid unnecessary costs and to ensure that all users have access to the right tools.

**3. Data pipeline Automation**

I learned that automation is key for timely and accurate data extraction. Tableau Prep Conductor can be used to schedule data workflows (or) Hyper API to extract with ETL script (Ngwena, 2022).

**4. IT Infrastructure Management**

I learned the value of focusing on the business’s priorities and re-using existing IT infrastructure rather than building it from scratch. For Landon Hotels, choosing Tableau Cloud and to outsource IT infrastructure management to Red30 (Ngwena, 2022) can reduce the need for in-house expertise and save time.

**5. Adaptability to growth and Integration**

I learned to develop solutions with future growth in mind. Continuous learning and the ability to integrate with other platforms like R and Salesforce (including CRM Analytics, formerly Tableau CRM and the Einstein One for AI model deployment), allow BI tools like Tableau to expand its capabilities and adapt to evolving customer needs (Salesforce, n.d.)

**References**

Baldwin, D. (2016). Mastering Tableau: Smart business intelligence techniques to get maximum insights from your data. Packt Publishing. https://www.packtpub.com/en-us/product/mastering-tableau-9781784397692

Ngwena, T. (2022). Everybody's introduction to Tableau. LinkedIn Learning. https://www.linkedin.com/learning/everybody-s-introduction-to-tableau-2022/solution-business-use-case-landon-hotels?u=130423532

Salesforce. (n.d.). Tableau analytics: Make better, faster decisions with enterprise analytics tailored to your CRM. Salesforce.com. https://www.salesforce.com/eu/products/einstein-analytics/overview/ 

Tableau. (n.d.). Pass Expressions with Analytics Extensions. Tableau.com. https://help.tableau.com/current/pro/desktop/en-us/r_connection_manage.htm

<img width="949" alt="image" src="https://github.com/user-attachments/assets/4e04d179-bb60-42ef-bd21-cf04c339dd8a">


<img width="984" alt="image" src="https://github.com/user-attachments/assets/8b547574-f632-4d47-a58e-b757a611cfb2">

# 4. Evolution of Analytics: From Descriptive to Cognitive by Krishna Damarla 

Descriptive analytics summarizes historical data to answer the question "what happened," giving numerical statistical insights into past business performance. It can be based on a sample (part of the population), or a census (the entire population). For example, in examining the average age of 100 randomly selected Trine University students (AbdulHussein, 2022), the average age is a statistic for the sample, and the mean age of all Trine University students is a parameter of the entire population.

Exploratory analytics focuses on "understanding the data" rather than summarization. Finding correlations and identifying relationships are part of it (Devopedia, 2022). For instance, it can be noticed from email marketing data (Ponnambalam, 2024) that a 30% discount on items, such as USB drives and headphones, worked better than a 40% off. An income-based study showed that people who earn more than $150,000 expressed less interest in the ads. These insights help us in re-evaluating our pricing strategies in terms of sales and revenue.

Explanatory analytics determines the "underlying reasons for the problem" and presents narratives with future vision. For example, a recent CrowdStrike software update caused a global IT outage (Sato, 2024). According to an investigation by CrowdStrike, a bug in the update's test program stopped it from validating the configuration content before deployment. The main reason is an inconsistency between the input fields provided in the update and what was intended. Because of inadequate testing procedures, this was overlooked. To prevent similar issues in the future, it is crucial to test different test scenarios and validate software modifications thoroughly.

A new era of analytics powered by AI is emerging. With solutions like SAP Predictive Analytics, we can forecast results more accurately. AI is used in prescriptive analytics to model scenarios and suggest the optimal action. Experimental analytics is conducting virtual experiments and AI-driven testing (Ponnambalam, 2024). Automated analytics uses solutions like Google’s AutoML to automate business processes without human intervention. Cognitive Analytics (Ulster University, n.d) is improving the quality of analytics by imitating human intelligence and providing deep insights into complex data with products like IBM Watson and Microsoft Cortona.

<img width="896" alt="image" src="https://github.com/user-attachments/assets/45e5bbaf-d075-41b7-9f9b-38d569a2d98d">

<img width="897" alt="image" src="https://github.com/user-attachments/assets/913839f3-37c7-4946-bfc0-fb1fb9636498">
