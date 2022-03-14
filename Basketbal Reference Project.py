#Lets Import the libraries
import pandas as pd
import seaborn as sns



#The building blocks
year = '2019'
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
#lets combine the str and year = URL
url = str.format(year)
url




#Read the irl with pandas 
df = pd.read_html(url,header =0)



#How many tables in the link:
len(df)



df[0]




df2019 = df[0]




df2019.shape




#Lets check if we have duplicates
df2019[df2019.Age =='Age']



df = df2019.drop(df2019[df2019.Age == 'Age'].index)
df.shape


# In[124]:


#check if we have more duplicates
len(df[df.Age =='Age'])


# In[125]:


#Lets get the shape of the dataframe
df.shape


# In[126]:


df.head()


# In[127]:


#Lets make an histogram to see how the data behave

sns.distplot(df.PTS,kde=False)


# In[128]:


#Lets check the data Types
df.dtypes


# In[129]:


#Change Data types to Float for PTS and Age
df['PTS'] = df['PTS'].astype(float, errors = 'raise')
df['Age'] = df['Age'].astype(float, errors = 'raise')

# In[130]:


df['PTS'].dtypes


# In[131]:


#lets sort values
Sort_PTS = df.sort_values(by='PTS',ascending=False)
Sort_PTS




#Now lets bring only the columns that we need for this data analysis
DF_set = Sort_PTS[['PTS', 'Player','Age','Pos','Tm']]
DF_set

Top_10_players = DF_set.head(10)
#Lets take a look in Excel
Top_10_players.to_excel("Top_10_players.xlsx", index =False)

#Lets plot this 10 top players
Top_10_players.plot(kind='bar',  y= 'PTS', x= 'Player')



####---------------####---------------------------####


#Lets grab data from another website

str = 'https://www.w3schools.com/html/html_tables.asp'
url = str

df = pd.read_html(url, header = 0)


# In[105]:


len(df)



df



#Lets bring the first table as a Data frame

Table_1 = df[0]
Table_1


# In[ ]:




#------------------------#----------------#------------------------#-----------------


#In a Loop / another way to do it
years = [2015,2016,2017,2018]
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

for year in years:
    #lets combine the str and year = get individual URL's
    url = str.format(year)
    print(url)
