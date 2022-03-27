#!/usr/bin/env python
# coding: utf-8

# # Heart Rate and Heart Rate Variability

# In[1]:


#import necessary packages
import numpy as np
import pandas as pd
import heartpy as hp
import matplotlib.pyplot as plt


# In[122]:


#reads in IR values as data frame

df = pd.read_csv('file_name', index_col = None, sep=',', header=None)


# In[123]:


display(df)  # adjust to needed
x = df[0].values.tolist()
data = np.array(x)


# In[119]:


#peak enhancement
enhanced = hp.enhance_peaks(data, iterations=1)


# In[120]:


#plot PPG
plt.plot(enhanced)
plt.show()


# In[121]:


#performs processing
wd, m = hp.process(enhanced, sample_rate = 50.0)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))


# In[ ]:




