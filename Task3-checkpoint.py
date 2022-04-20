#!/usr/bin/env python
# coding: utf-8

# # Author - Nikhil Kumar Mishra
# ## Data Science and Business Analytics Intern
# ## GRIP - The Sparks Foundation
# ### Task-3  Exploratory Data Analysis-Retail

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                            
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[2]:


df=pd.read_csv("SampleSuperstore.csv")                      


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.duplicated().sum()


# In[8]:


df.drop_duplicates()


# In[9]:


fig,axes = plt.subplots(1,1,figsize=(8,6))
sns.heatmap(df.corr(), annot= True)
plt.show()


# In[50]:


sub_category = df['Sub-Category'].value_counts()
category = df['Category'].value_counts()
sub_category, category


# In[11]:


sub_category.plot.pie(figsize = (10,10), autopct="%1.1f%%", shadow = True)


# In[12]:


category.plot.pie(figsize = (10,10), autopct="%1.1f%%", shadow = True)


# In[81]:


plt.figure(figsize=(20,10))
sns.set_theme(style="darkgrid")
sns.countplot(x='Sub-Category',data=df)


# In[20]:


plt.figure(figsize=(8,8))
sns.set_theme(style="darkgrid")
sns.countplot(x='Category',data=df)


# In[32]:


sale_profit_sum = df.groupby('Sub-Category')['Sales','Profit'].sum()
sale_profit_sum


# In[80]:


sale_profit_sum.plot.bar(figsize = (20,10),title = "Sub-Category Vs Sales and Profit")
plt.ylabel("Sales and Profit")


# In[54]:


col=['Postal Code']
df1= df.drop(columns=col,axis=1)


# In[56]:


sns.pairplot(df1,hue='Category')


# In[79]:


plt.figure(figsize=(20,10))
sns.countplot( data=df1, x='Sub-Category', hue='Region')
plt.title("Count of sub-category products distributed in each region", fontsize=15)


# In[82]:


statewise_profit=df1.groupby(['State'])['Profit'].sum()
statewise_sales=df1.groupby(['State'])['Sales'].sum()
category_profitandSales = df1.groupby('Category')[['Profit','Sales']].sum()


# In[75]:


statewise_profit.plot.bar(figsize = (20,10),title = "State Vs State-wise Profit",color='red', edgecolor='black')
plt.ylabel("State-wise Profit")


# In[73]:


statewise_sales.plot.bar(figsize = (20,10),title = "State Vs State-wise Sales", color='skyblue', edgecolor='blue')
plt.ylabel("State-wise Sales")


# In[89]:


category_profitandSales.plot.bar(figsize = (20,10),title = "Category Vs Profit and Sales",color=['blue','red'], edgecolor='black')
plt.ylabel("Category-wise Sales and Profit")


# ## Observations:

# 1. Technology category have the highest Profit.
# 2. Furniture category have the lowest Profit.
# 3. Phones and chairs sub-category have high sales but chairs have less Profits compared to Phones.
# 4. Bookmarks and tables Sub-Category faces high Loss.
# 5. People from west region shop more as compared to other regions.
# 6. The store has wide variety of office supplies especially in binders and paper department

# ## Thank You!!!
