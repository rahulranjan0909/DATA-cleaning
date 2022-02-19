#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[2]:


df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df.head()


# In[3]:


temp = pd.DataFrame(df.From_To)
temp.head()


# In[4]:


temp['Source'] = temp.From_To.str.split('_').str[0]
temp['Destination'] = temp.From_To.str.split('_').str[1]
temp.drop('From_To',axis=1,inplace=True)
temp['Source'] = temp['Source'].str.title()
temp['Destination'] = temp['Destination'].str.title()
temp.head()


# In[5]:


f = df.drop('From_To', 1)
df = pd.concat([df,temp], axis = 1)
df


# In[6]:


objs = pd.DataFrame(df['RecentDelays'].tolist(),columns=['delay_1','delay_2','delay_3'])
df = df.drop('RecentDelays', 1)
df.insert(2, "Delay_1", objs['delay_1'])
df.insert(3, "Delay_2", objs['delay_2'])
df.insert(4, "Delay_3", objs['delay_3'])
df


# In[ ]:




