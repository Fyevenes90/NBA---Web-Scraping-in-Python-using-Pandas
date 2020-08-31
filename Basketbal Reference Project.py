#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd


# In[104]:


#Lets bring the data from url
year ='2019'
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'


# In[105]:


#lets combining both together 
url = str.format(year)
url


# In[106]:


df = pd.read_html(url,header = 0)


# In[47]:


#Example doing it with dif website

#str = 'https://www.w3schools.com/html/html_tables.asp'
#url = str

#df = pd.read_html(url, header = 0)


# In[107]:


len(df)


# In[108]:


DF_2019 = df[0]
DF_2019.head()


# In[109]:


##Data cleaning
DF_2019[DF_2019.Age =='Age']


# In[110]:


New_2019DF = DF_2019.drop(DF_2019[DF_2019.Age =='Age'].index)


# In[111]:


New_2019DF.shape


# In[64]:


import statistics


# In[67]:


New_2019DF['Age']


# In[79]:


New_2019DF[['Age']]


# In[112]:


New_2019DF.describe()


# In[114]:


New_2019DF.head()


# In[132]:


New_2019DF.dtypes


# In[133]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[131]:


New_2019DF.PTS=pd.to_numeric(New_2019DF.PTS)
#New_2019DF.age=pd.to_numeric(pf.age)


# In[136]:


#Always make sure that the numerical column is in the right format
New_2019DF.plot(kind='bar',x='Player',y ='PTS')


# In[137]:


#plot data
fig, ax = plt.subplots(figsize=(15,7))
New_2019DF.groupby(['Age']).count()['PTS'].plot(ax=ax)


# In[ ]:




