# User-Engagement-Analysis-Using-Python
User Engagement Analysis to assess and understand user involvement, interaction, and satisfaction with a product, service, or platform.
* Title :-        **User Engagement Analysis**
* Created by :-   SAMARTH
* Date :-         16-07-2023
* Tool used:-     Google collab For Python

# Introduction :- 
* In this project, we will be analyzing user engagement data to gain insights for average session duration and analyzing user retention
* We will use Python to extract, transform and analyze the data.
* The insights derived from this analysis will serve to uncover the underlying factors that shape and impact user engagement..
* We explored the relationship between Bounce rates and the Average Session Duration.

# Data :- 
* We found this dataset from online site to explore EDA
* This contain 1 CSV file named Bounce Rates
* Client ID(Each row uniquely identifies a client who engaged)
* Bounce Rates (Bounce rate refers to the percentage of users who visit a website or webpage but leave without taking any further action or navigating to other pages within the same site.)
* Average Session Duration (measure the average amount of time users spend on a website during a single session.) 


# Approach :
* Acquired the user engagement data from a publicly available source and import it into a Python .
* Used Python to clean the data and ensure that it is in a format that can be easily analyzed.
* This tasks performed using the python library (Pandas) and task include checking null values and duplicate values.
* Used Python to extract relevant information from the data, such as correlation, analyzing bounce rates and comparison of user engagement by bounce rate segment.
* Analyzing User retention and average bounce rate by retenton segment .
* Visualize the data using Plotly Library
* Bar Chart for Average Bounce Rate for retention Segment
* Pie chart for User retention rate.
* We analyzed various metrics using Python Library.

# Python Library Used :
* Pandas
* Plotly
# Python Function Used :
* Data.corr()
* Data.drop
* to_timedelta,astype (for data manipulation)
* px.scatter
-------
# Key Insights:-
## 1. Bounce Rates: 
► Define the threshold for high, medium and low bounce rates.<br>
► 70 for high bounce rate threshold 30 for low bounce rates threshold.<br>
► 71 clients for low bounce rate, 480 for medium bounce  rates and 399 for high bounce rates .<br>


## 2. Average Bounce Rate by retention segment: 
► Divided thr user into frequent and occasion users through session column.<br>
► if Session > 32 then frequent otherwise occasional (32 is the mean of the session column).<br>
► Calculate Average bounce rate using group by function.<br>
► Average Bounce Rate for Frequent Users 64.45.<br>
► Average Bounce Rate for Ocassional Users 65.67.<br>

## 3. User Engagement By Bounce Rate Segment: 
► Visualize the User engagement through Average Session using Bar Chart.<br>
► Average Session Duration for low bounce rate is 9.05.<br>
► Average Session Duration for Medium bounce rate is 5.04.<br>
► Average Session Duration for High bounce rate is 1.43.<br>


------
