#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

df = pd.read_csv('income_evaluation.CSV')

print(df) 


# In[11]:


df.head ()


# In[12]:


df.info()


# In[13]:


df.describe ()


# In[14]:


df.columns


# In[15]:


df.dtypes


# In[16]:


df.corr()


# In[17]:


import matplotlib.pyplot as plt

df = pd.read_csv('income_evaluation.csv')

df.plot()

plt.show()


# In[18]:



df = pd.read_csv('income_evaluation.csv')
print(df)


# In[19]:


print(df.age)


# In[20]:


import matplotlib.pyplot as plt


# In[28]:


df.columns


# In[29]:


X=df[' fnlwgt']


# In[30]:


plt.plot( df['age'] , df[' education-num'] , 'r') # 'r' is the color red
plt.xlabel('X age')
plt.ylabel('Y education-num')
plt.show()


# In[24]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


df.head ()


# In[26]:


sns.distplot(df['age'])


# In[ ]:




