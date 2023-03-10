#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd

df = pd.read_csv (r'C:\Users\z0043w9p\Anaconda3\csv\Ecommerce Customers.csv')

df 


# In[23]:


df.head()


# In[24]:


df.info ()


# In[25]:


df.describe ()


# In[26]:


df.columns


# In[27]:


df.dtypes


# In[28]:


import matplotlib.pyplot as plt

df.plot()

plt.show()


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


import matplotlib.pyplot as plt

df.plot(kind = 'scatter', x = 'Avg. Session Length', y = 'Yearly Amount Spent')

plt.show()


# In[31]:


import matplotlib.pyplot as plt

df.plot(kind = 'scatter', x = 'Time on App', y = 'Time on Website')

plt.show()


# In[32]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


df.head()


# In[34]:


sns.pairplot(df)


# In[35]:


sns.pairplot(df,hue='Avg. Session Length',palette='coolwarm')


# In[36]:


sns.jointplot(x='Avg. Session Length',y='Yearly Amount Spent',data=df,kind='reg')

