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
* We analyzed various metrics using Python Library.
* We used the insights gained from the analysis to make recommendations for improvement for the restaurants, and suggest ways in which the data can be used to drive business decisions.

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
## 1. Customer Demographics: 
► 62% customers are from "San Luis Potosi".<br>
► 70% customers have medium budget & 0.4% customers have high budget.<br>
► Most of the drinkers & smokers are students and they are casual drinkers or social drinkers.<br>
► 80% of our customers are in the age bucket of 18-25.<br>
► Most preferred cuisines are Mexican, American, Pizzeria, Cafeteria & Coffee shop.

## 2. Restaurant Details: 
► There are a total 129 restaurants & majority are in the city of "San Luis Potosi".<br>
► Only 41 restaurants are serving drinks & 65 restaurants don't have parking.<br>
► Most restaurants offer cuisines like Mexican, Bar, Cafeteria, Fast Food, Brewery, Seafood, Burgers.<br>
► 18% of restaurants are of High budget, 49% of them are of Medium budget & 33% are low budget.

## 3. Ratings Analysis: 
► There are 26 restaurants who received an average overall rating of more than 1.50.<br>
► 44% responses from the customers were positive for the food experience.<br>
► 22% responses from the customers were negative for overall experience.<br>
► 131 customers are visiting their local restaurants & 14 customers are visiting outside of their locality.<br>
► Customers from cities of Ciudad Victoria, Cuernavaca & jiutepec are visiting restaurants of San Luis Potosi.<br>
► We analyzed the best restaurants for each cuisine based on average ratings.<br>
► We analyzed bad restaurants for each cuisine based on average ratings.<br>
► For overall & food experience best average cuisine is International & for food experience it is Mexican.<br>
► There are 293 responses (25%) of customers who gave the highest ratings in all the experiences.

------
# Strategies:
⭐ We found that the average rating for food experience in our dataset was around 1.21/2.00. This indicates that overall, customers were pleased with their dining experiences. But some restaurants didn't receive good ratings for the service. So the restaurants should focus on improving their service experience.<br>
⭐ Most of the good restaurants are in the city of San Luis Potosi for which outsiders were travelling to this city. We can improve our food & services in other cities as well.<br>
⭐ American cuisine is the second most preferred cuisine by customers but we don't have that many restaurants with american cuisine. We can improve the business in that segment as well.<br>
⭐ Students & teenagers are more into drinking & smoking so we can plan some marketing strategy for them like special student entry or student discount to acquire customers.
