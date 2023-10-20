# -*- coding: utf-8 -*-
"""user_engagement_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGsnv5B5DRDftKnCnc_WClCDNJLj6bWF
"""

# import the libraries that will be used for data analysis
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Read the CSV File
df=pd.read_csv('/content/bounce-rate.csv')

# we will check the data by using Head
df.head()

# we will check the information about the dataset mai ly the data type of the attributes
# we have seen both "avg session duration" and "Bounce Rate" are numerical but here in the data set is shown as object
# so we will change  the data type of both "avg session duration" and "bounce rte" to float
df.info()

# we will check that the data contains null value or not
df.isnull().sum()

df.columns

# In below code we remove the first character from each value in 'Avg Session Duration' column representing  a unit of time
df['Avg. Session Duration'] = df['Avg. Session Duration'].str[1:]
# Then,we converted the values of 'Avg session duration' to time delta format
df['Avg. Session Duration'] = pd.to_timedelta(df['Avg. Session Duration'])
#  Then after that we convert time delta format values to minutes and converting the 'avg session duration' into numerical values
df['Avg. Session Duration'] = df['Avg. Session Duration'] / pd.Timedelta(minutes=1)
# at last we remove the percentage sign from each value in the  'Bounce Rate' column and conver them into the float values
df['Bounce Rate'] = df['Bounce Rate'].str.rstrip('%').astype('float')

# this code is to check whether above codes to change the data types and further information is executed or not
df.head()

# 'Client ID' is of no use , so we will drop this column
df.drop('Client ID', axis=1, inplace=True)

# Descriptive statistics of the data
df.describe()

# Calculation of Correlation
correlation_=df.corr()

# Visualize the Correlation
correlation_figure=px.imshow(correlation_,labels=dict(x='Features',y='Features',color='Correlation'))
correlation_figure.update_layout(title='Correlation')

# Define the class for each bounce rate(high,medium,low)
high_bounce_rate = 70
low_bounce_rate = 30
# # Put the clients on each class based on the Bounce Rates

df['bounce_rate_class'] = pd.cut(
    df['Bounce Rate'],
    bins=[0, low_bounce_rate, high_bounce_rate, 100],
    labels=['Low', 'Medium', 'High'],
    right=False
)
#  Count the no. of clients in each class( that we made on the basis of the bounce rates)
class_counts = df['bounce_rate_class'].value_counts().sort_index()
#  Last code is to visualize the segment
class_figure = px.bar(class_counts, labels={'index': 'Bounce Rate Segment',
                                             'value': 'Number of Clients'},
                     title='Class of Clients based on Bounce Rates')
class_figure.show()

# average session duration for each bounce rate class
class_average_duration = df.groupby('bounce_rate_class')['Avg. Session Duration'].mean()

# bar chart to compare user engagement
engagement_figure = go.Figure(data=go.Bar(
    x=class_average_duration.index,
    y=class_average_duration,
    text=class_average_duration.round(2),
    textposition='auto'
))

# Customize the layout of the chart
engagement_figure.update_layout(
    title='Comparison of User Engagement by Bounce Rate Class',
    xaxis=dict(title='Bounce Rate Class'),
    yaxis=dict(title='Average Session Duration (minutes)')
)

# Display the chart
engagement_figure.show()

# Total Session duration for each client
df['Total_session_duration']=df['Sessions']*df['Avg. Session Duration']
# Sort the data frame  by total session duration in descending order
df_sorted_total_session=df.sort_values('Total_session_duration',ascending=False)
# Top Most Users
df_sorted_total_session.head(10)

# scatter plot to analyze the relationship between bounce rate and average session duration
scatter_figure=px.scatter(df,x='Bounce Rate',
                          y='Avg. Session Duration',
                          title='Relationship between bounce rate and average session duration')
scatter_figure.update_layout(xaxis=dict(title='bounce rate'),
                             yaxis=dict(title='average session duration'))
scatter_figure.show()

# Define the retention segment on the basis of the sessions
def get_retention_segment(row):
    if row['Sessions'] >= 32: # 32 is mean of sessions
        return 'Frequent Users'
    else:
        return 'Occasional Users'
# Create a new column for retention segment
df['retention_segment'] = df.apply(get_retention_segment, axis=1)

# calculate average of bounce rate for each retention segment
avg_segment_bounce_rates = df.groupby('retention_segment')['Bounce Rate'].mean().reset_index()

#Bar chart to visualize average bounce rate on the basis of the retention segment

bar_figure = px.bar(avg_segment_bounce_rates, x='retention_segment', y='Bounce Rate',
                 title='Average Bounce Rate by Retention Segment',
                 labels={'retention_segment': 'Retention Segment', 'Bounce Rate': 'Average Bounce Rate'})
bar_figure.show()

# count the number of users in each retention segment

retention_segment_counts = df['retention_segment'].value_counts()

# pie chart to anlyze no of user in frequent class and ocassional class

pie_chart = px.pie(
    retention_segment_counts,
    values=retention_segment_counts.values,
    names=retention_segment_counts.index,
    color=retention_segment_counts.index,
    title='User Retention Rate'
)

# Display the pie chart
pie_chart.show()
