#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[35]:


# Load the dataset
data = pd.read_csv('Unempolyment_data.csv')

# Display the first few rows of the dataset
print(data.head())


# In[39]:


# Check for missing values
print(data.isnull().sum())


# In[57]:


data.columns= ["Area","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region"]


# In[51]:


#Now let’s have a look at the correlation between the features of this dataset:
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()


# In[52]:


#Now let’s visualize the data to analyze the unemployment rate. I will first take a look at the estimated number of employees according to different regions of India:
data.columns= ["Area","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# In[58]:


#unemployment rate according to different regions of India:
plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()


# In[73]:


# Group data by region and date, and calculate the mean of other attributes
grouped_data = data.groupby(['Region', 'Date']).mean()

# Print the grouped data
print(grouped_data)


# In[82]:


# Set up the plotting style
sns.set(style="whitegrid")

# Create a line plot of estimated employment rate over time for different regions
plt.figure(figsize=(12, 6))
sns.lineplot(data=grouped_data, x='Date', y='Estimated Employed', hue='Region')
plt.title('Estimated Employment Rate by Region over Time')
plt.xlabel('Date')
plt.ylabel('Estimated Employment Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


# In[ ]:




