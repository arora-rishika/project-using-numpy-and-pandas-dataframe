#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
bank_train=pd.read_csv('bank_train.csv')
df=pd.read_csv('bank_train.csv')
df


# In[ ]:


#copy the file into bank_train3?


# In[3]:


bank_train3=bank_train.copy()


# In[ ]:


#How many categorical columns are there in the dataframe?


# In[31]:


#How many rows in the dataframe contain missing values? If there are null values, then drop the rows with null values.
bank_train3.isnull().sum()


# In[32]:



bank_train3.isnull().sum().sum()


# In[39]:


df_omit=df.dropna(axis=0)


# In[40]:


df_omit.isnull().sum().sum()


# In[11]:


bank_train.shape


# In[12]:


bank_train.shape


# In[13]:


pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            margins=True,
            normalize=True,
            dropna=True)


# In[14]:


bank_train.head()


# In[18]:


#What percentage of clients with secondary education have not subscribed to a deposit?
pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='index')


# In[19]:


#Using Seaborn’s countplot API, plot a grouped bar plot of marital status and deposit (as hue). Identify the category that has more clients who have subscribed to a deposit than clients who have not
pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='index')
pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='columns')
pd.crosstab(index=bank_train3['housing'],columns='count',dropna=True)
pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            normalize=True,
            dropna=True)
count=0
for i in range(0,len(bank_train3),1):
    if ((bank_train['deposit'])[i]=="yes") and ((bank_train['contact'])[i]=="cellular" or (bank_train['contact'])[i]=="telephone"):
      count=count+1;
print(count)

t=0
for i in range(0,len(bank_train3),1):
    if ((bank_train['deposit'])[i]=="no")and((bank_train['housing'])[i]=="yes"or(bank_train['loan'])[i]=="yes"):
      t=t+1;
print(t)

pd.crosstab(index=bank_train3['poutcome'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='index')
pd.crosstab(index=bank_train3['poutcome'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='columns')
pd.crosstab(index=bank_train3['poutcome'],
            columns=bank_train3['deposit'],
            margins=True,
            normalize=True,
            dropna=True)

pd.crosstab(index=bank_train3['housing'],columns='count',dropna=True)
pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            normalize=True,
            dropna=True)

sns.countplot(x="marital", data=bank_train, hue="deposit")
pd.crosstab(index = bank_train['deposit'],
            columns=bank_train['marital'],
            dropna=True)

bank_train.dropna(axis=0, inplace=True)
sns.lmplot(x='age',y='balance',data=bank_train,
           fit_reg=False,legend=True,palette="Set1")


pd.crosstab(index = bank_train['age'],
            columns=bank_train['balance'],
            dropna=True)


# In[23]:


pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            margins=True,
            dropna=True,
            normalize='columns')


# In[21]:


pd.crosstab(index=bank_train3['housing'],columns='count',dropna=True)


# In[22]:


pd.crosstab(index=bank_train3['education'],
            columns=bank_train3['deposit'],
            normalize=True,
            dropna=True)


# In[ ]:




