#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt # for basic plotting 
import seaborn as sns; sns.set()


# In[43]:


norm_mean=70
gym_mean=80
sd_norm=5
sd_gym=6
norm_per=.70
gym_per=.30
tot=10000


# In[45]:


norm_dist=np.random.normal(norm_mean, sd_norm, int(tot*norm_per))
gym_dist=np.random.normal(gym_mean, sd_gym, int(tot*norm_per))


# In[46]:


pop_dist=np.append(norm_dist, gym_dist)


# In[47]:


plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
sns.distplot(pop_dist).set_title('Total Distribution')
plt.xlim([50,100])
plt.subplot(3,1,2)
sns.distplot(norm_dist).set_title('Non gym goers')
plt.xlim([50,100])
plt.subplot(3,1,3)
sns.distplot(gym_dist).set_title('Gym goers')
plt.xlim([50,100])


# In[48]:


len(pop_dist)


# In[97]:



pop_sam_mean=np.mean(random.choices(pop_dist, k=100))
pop_mean=np.mean(pop_dist)
norm_sam_mean=np.mean(random.choices(norm_dist, k=100))
norm_mean=np.mean(norm_dist)
gym_sam_mean=np.mean(random.choices(gym_dist, k=100))
gym_mean=np.mean(gym_dist)


# In[98]:


norm_mean=np.mean(norm_dist)


# In[99]:


plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
plt.axvline(x=pop_mean, color='r')
plt.axvline(x=pop_sam_mean)
sns.distplot(pop_dist).set_title('Total Distribution')
plt.xlim([50,100])
plt.subplot(3,1,2)
plt.axvline(x=norm_mean, color='r')
plt.axvline(x=norm_sam_mean)
sns.distplot(norm_dist).set_title('Non gym goers')
plt.xlim([50,100])
plt.subplot(3,1,3)
plt.axvline(x=gym_mean, color='r')
plt.axvline(x=gym_sam_mean)
sns.distplot(gym_dist).set_title('Gym goers')
plt.xlim([50,100])


# In[84]:



:


# In[95]:





# In[ ]:




