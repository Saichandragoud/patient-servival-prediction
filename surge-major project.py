#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("dataset.csv")
data


# In[3]:


data.describe()


# In[5]:


data.head(30)


# In[8]:


data.fillna({"bmi":29.185818}).head(30)


# In[9]:


data.fillna(1).head(30)


# In[ ]:




