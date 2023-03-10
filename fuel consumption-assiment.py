#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv (r'C:\Users\z0043w9p\Anaconda3\csv\FuelConsumptionCo2.csv')

df


# In[ ]:





# In[4]:


df.head()


# In[5]:


df.info ()


# In[6]:


df.describe ()


# In[7]:


df.columns


# In[8]:


df.dtypes


# In[16]:


import seaborn as sns
sns.lmplot(data=df,x='ENGINESIZE',y='FUELCONSUMPTION_COMB')


# In[14]:


df.corr ()


# In[17]:


plt.plot( df['ENGINESIZE'] , df['FUELCONSUMPTION_COMB'] , 'r') # 'r' is the color red
plt.xlabel('X ENGINESIZE')
plt.ylabel('Y FUELCONSUMPTION_COMB')
plt.show()


# In[12]:


import matplotlib.pyplot as plt

df.plot(kind = 'scatter', x = 'ENGINESIZE', y = 'CYLINDERS')

plt.show()


# In[13]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:



df.head()


# In[15]:


sns.distplot(df['CYLINDERS'])


# In[16]:


sns.pairplot(df)

