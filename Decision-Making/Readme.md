# Interactive Actions in Dashboard Visualizations: Naive to Advanced by Krishna Damarla

In Tableau, you can add six types of actions to a dashboard to explore data dynamically, increasing user engagement for visual insights. They are Filter, Highlight, Go to URL, Go to Sheet, Change Parameter, and Change Set Values (used for brushing or drill-down). Let’s look at the two most common actions: Highlight and Filter within a dashboard that shows regional sales and employee ratings (Francis, 2019).

1. Highlight Action

The Highlight action filters data in other sheets based on selections made in one sheet. In the left dashboard example below, selecting the SE region in the timeline (line chart) will highlight all relevant data across associated sheets, to show only results for that SE region. The action runs when you select an item, and de-selecting the same item will return you to the original dashboard view (right dashboard below).

![image](https://github.com/user-attachments/assets/1e3c8ed6-fd18-42d2-b071-474131d83185)   ![image](https://github.com/user-attachments/assets/1c87d380-c957-4188-adc4-a89d8f0acd0e)


 2. Filter Action

The Filter action dynamically updates data in other sheets based on selections. For example, clicking on a specific time point in the SW region of the timeline will filter the dashboard to display only products sold during that specific week and employees responsible for sales in that week. You can customize this action to run either on selection or on hover.

![image](https://github.com/user-attachments/assets/9a6bf141-9bdd-48ef-bdaf-b561ca123af5)


While these actions are widely used, they are limited in scope. For more complex research goals, such as exploring geospatial data, additional interactions may be required. Visual Information-Seeking Mantra proposed by Shneiderman (Aigner, 2007) is highly relevant in this context. This mantra, "overview first, zoom and filter, then details-on-demand," is useful for effectively navigating large datasets. 

3. Overview First, Zoom and Filter, Then Details-On-Demand Action

One example that follows this advanced action is Interactive Catchment Explorer (ICE), a web-based interactive data visualization framework (Walker et al., 2020). ICE is designed to help decision-makers explore complex geospatial environmental datasets and model predictions. The framework is built on Shneiderman's Mantra, allowing users to first gain a broad overview, zoom in for filtering, and then drill down into specific details. 

Key Components of ICE:

Map: Displays spatial features and allows users to pan and zoom at different scales.
Selection Menu: Enables the selection of variables (e.g., mean summer temperature) that determine the color coding of features.
Crossfilters: Histograms for crucial variables (e.g., elevation, forest cover) help users visualize data distributions and filter specific values. 
For example, filtering data by Forest Cover (%) in the histogram will highlight corresponding regions on the map, as demonstrated in the ICE dashboard below. 

![image](https://github.com/user-attachments/assets/d47d8c3b-b945-4e34-a34c-85e99d6537f6)


In another application, the ICE framework is used to assess the vulnerability of trout species towards climate change within the Crown of the Continent Ecosystems. It displays the overall risk level for various trout conservation population and uses cross-filters to analyze different risk levels, including overall risk, climate risk, and demographic risk as depicted in the dashboard below. This visual analysis helps stakeholders understand potential impacts of climate change on trout populations and recommend conservation strategies to reduce associated risks (Walker et al., 2020).

![image](https://github.com/user-attachments/assets/8f8de852-8e7c-4918-9f92-264b22c07883)

References 

Aigner, W. (2007). Visual information-seeking mantra. InfoVis Wiki. https://infovis-wiki.net/wiki/Visual_Information-Seeking_Mantra

Francis, M. (2019). Creating interactive Tableau dashboards. LinkedIn Learning. https://www.linkedin.com/learning/creating-interactive-tableau-dashboards/

Keim, D., Kohlhammer, J., Ellis, G., & Mansmann, F. (2010). Mastering the information age: Solving problems with visual analytics. Eurographics Association.

Walker, J. D., Letcher, B. H., Rodgers, K. D., Muhlfeld, C. C., & D’Angelo, V. S. (2020). An interactive data visualization framework for exploring geospatial environmental datasets and model predictions. U.S. Geological Survey. https://www.usgs.gov/apps/ecosheds/#/   

<img width="881" alt="image" src="https://github.com/user-attachments/assets/510a30f4-64ab-47e5-9421-ec7a47e9e2be">

<img width="894" alt="image" src="https://github.com/user-attachments/assets/7adebaf0-d355-4678-a432-f8f4069f4b63">

# Four Critical Questions for Designing Effective Dashboards

Creating an effective dashboard that displays useful information at a glance requires asking four critical questions to ensure it serves its purpose and meets user needs (Subotin, n.d.).

First, who is the dashboard suitable for? Understanding the target audience helps designers determine the visualization type, complexity, and detail level. While experienced viewers may need more complex insights, general viewers benefit from its simplicity (Francis, 2019).

Second, where should I view the dashboard? The display device impacts layout and interactivity, whether on desktop, tablet, or mobile. For example, mobile screens need more compact and touch-friendly interfaces (Francis, 2019).

Third, why is the dashboard being created? Understanding the purpose (whether for exploration, explanation, or tracking KPIs) leads to the selection of data and visualization. Dashboards often combine data from multiple departments in one place (Hayward, 2024). To increase organizational value, design choices should focus on creating dashboards that serve a purpose (Subotin, n.d.).


Finally, what data and elements need to be shown? Choosing relevant data avoids clutter and confusion. Additionally, deciding whether the dashboard displays real-time or historical data (Francis, 2019) can guide the use of interactive elements such as drill-down, drop-down, and zooming, thus improving user experience and engagement.

Failure to ask these questions can lead to poor design, low usability, and the risk of dashboards that are too complex or simplistic, misaligned for user needs, or cluttered with irrelevant and inconsistent information. Misaligned dashboards may overwhelm or distract the audience, while cluttered displays may dilute the intended insights.

In summary, asking these questions is crucial to creating a purposeful and user-friendly dashboard suited to its context. These questions ensure the dashboard is designed with clarity, focus, and relevance, enhancing its impact and usability to deliver meaningful insights (Francis, 2019).

References

Francis, M. (2019). Creating interactive Tableau dashboards. LinkedIn Learning. https://www.linkedin.com/learning/creating-interactive-tableau-dashboards/

Hayward, E. (2024). Starter guide to dashboards. Klipfolio. https://www.klipfolio.com/blog/starter-guide-to-dashboards#WhatDashboard

Subotin, S. (n.d.). Dashboard design best practices. Toptal. https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices

<img width="981" alt="image" src="https://github.com/user-attachments/assets/f8027b82-bf22-4e30-b12d-11b9809a1e40">

<img width="980" alt="image" src="https://github.com/user-attachments/assets/70eebb16-ae0d-4f79-a6b5-02095815739c">

# Reporting Transformation at Landon Hotels with Tableau by Krishna Damarla

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

# Healthcare Analytics Experience by Krishna Damarla

<img width="957" alt="image" src="https://github.com/user-attachments/assets/c293fe49-0909-4ae2-a260-37a3738894b3">

Code to Implement above Suggestion: [face-recognition.py](../Data-Science/Python/face-recognition.py)

Note: The above code snippet is intended for scenarios where a person's face has already been trained using a predefined set of images in a training model. In real-world applications, recognizing the face of an unknown individual requires using a government-approved ID and photograph to train the model, enabling it to match the person in live video for recognition purposes. Implementing such an architecture must align with healthcare security practices and regulations of local body, such as HIPAA in the U.S, PIPEDA in Canada, GDPR in Europe, DISHA in India, and PIPL in China.


# Health Insurance Analytics Experience by Krishna Damarla

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

# Best Practices for Using Color in Data Visualization by Krishna Damarla

If a colleague or stakeholder suggests that the dashboard could be made more impactful by adding more or bolder colors, my response would be: I understand the desire to make the dashboard stand out more. But adding more or darker colors can reduce the effectiveness. Instead, we should focus on using color strategically, as Jeffrey suggests in his "The Big Book of Dashboards” (Wexler et al., 2018) and as Krause suggests in his book “Color for Designers” (Krause, 2014). 

The main points regarding the use of color in data visualization are:

1. Five Uses of Color (Wexler, 2021): The following graphic by Jeffrey Schaefer outlines the ways color can be used in data visualization.

   o   Sequential Colors: Using gradient colors to show value progression (low to high).
   
   o   Diverging: Showing the contrast between two extremes with a neutral mid-point.
   
   o   Categorical: Using distinct colors to separate different categories. It’s best to use no more than 4 distinct colors. Group similar categories and then use sequential coloring for differentiation. Example applications are heat-maps, and density maps.
   
   o   Highlight: Drawing attention to specific data points.
   
   o   Alert Colors: Colors like red can highlight important data or signal alerts, but cultural contexts are important as color meanings can differ from region to region.

2. Use Color Sparingly (Wexler et al., 2018): Too much color can overwhelm and obscure insights. Minimal, well-placed color helps make data clearer and more understandable. Adding more or bolder colors to dashboards won’t always make dashboard more impactful.

3. Avoid Traffic Light Colors: Red-green color blindness affects many people, so using the typical traffic light colors can be problematic. Adjusting colors to be less dense or using alternatives like blue and orange can make visuals more accessible.

4. Maintain Color Harmony: Make visuals appealing without overwhelming them by trying different color harmony palettes (complementary, analogous, triadic).

5. Color in Branding (Krause, 2014): Understanding that color plays a major role in brand identity, and recognition, and can influence consumer behavior.

6. Emotional Impact of Colors: Color can evoke emotions and influence a viewer’s thought process and behaviors. Use color choices to set the mood or tone of a design, whether professional or elegant.

7. Testing Color Combinations: Test different colors in the real world to see how they perform and resonate with your audience. Experiment with color to discover unique palettes and combinations to enhance your designs.

8. Color in Digital and Print: Understand the difference between digital screen (RGB) and print (CMYK) colors to ensure accurate color reproduction.

9. Feedback and Revision (Krause, 2014): Get feedback from peers or audiences on color choices and be willing to make changes based on their feedback. Find color inspiration in nature, art, and everyday surroundings to develop original color palettes. Use tools like color wheel (primary, secondary, tertiary colors), swatches, and software in selecting and managing colors.

References

Krause, J. (2014). Color for designers: Ninety-five things you need to know when choosing and using colors for layouts and illustrations. New Riders.

Wexler, S. (2021). How to use data visualization to make better decisions—Faster. LinkedIn Learning. https://www.linkedin.com/learning/how-to-use-data-visualization-to-make-better-decisions-faster/

Wexler, S., Shaffer, J., & Cotgreave, A. (2018). The big book of dashboards: Visualizing your data using real-world business scenarios (1st ed.). Wiley. https://www.tableau.com/big-book-dashboards



