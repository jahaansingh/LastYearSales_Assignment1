#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd 
import numpy as np


# In[121]:


df = pd.read_csv('Assignment-Business-Quant.csv')


# In[122]:


df


# In[123]:


df['Sales Last Year']= " "
df=df.assign(sortkey = df.groupby('Item')['Year'].transform('sum'))  .sort_values(['sortkey','Item','Year'], ascending=[False,True,True])  .drop('sortkey', axis=1)


# In[124]:


df=df.reset_index(drop=True)
for i in range(1,len(df)):
        if df.loc[i,'Year'] != 2010:
            df.loc[i,'Sales Last Year'] = df.loc[i-1,'Sales']
        else:
            df.loc[i,'Sales Last Year'] = 0
        df.loc[i,'Sales Growth %'] = (df.loc[i,'Sales']/df.loc[i,'Sales Last Year'])-1
df['Sales Growth %'].replace(np.inf, 0, inplace=True)
pd.options.display.float_format = '{:,.2f}'.format


# In[125]:


display(df)


# In[126]:


df.tail(50)


# In[127]:


import qgrid
for qgrid_functions in dir(qgrid):
    print(qgrid_functions)


# # User Interactive Dashboard

# In[128]:


qgrid_widget=qgrid.show_grid(df)
qgrid_widget


# In[ ]:





# In[ ]:





# In[ ]:




