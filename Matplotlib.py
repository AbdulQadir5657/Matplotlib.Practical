#!/usr/bin/env python
# coding: utf-8

# # matplotlib
# 

# In[1]:


get_ipython().system('pip install matplotlib')


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np


# In[5]:


x=np.arange(0,10)
y=np.arange(11,21)


# In[6]:


x


# In[7]:


y


# In[8]:


plt.scatter(x,y)


# In[10]:


plt.scatter(x,y,c='r') # c denotes colour 


# In[23]:


plt.scatter(x,y,c='r')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Grape in 2D')
plt.savefig('Test.png')


# In[24]:


y=x*x


# In[25]:


y


# In[28]:


# line plot
plt.plot(x,y,'y')


# In[29]:


plt.plot(x,y,'b*')


# In[30]:


plt.plot(x,y,'b>')


# In[32]:


plt.plot(x,y,'g+',linestyle='dashed')


# In[37]:


plt.plot(x,y,'g+',linestyle='dashed',linewidth=2)


# In[39]:


plt.plot(x,y,'g+',linestyle='dashed',linewidth=2,markersize=10)


# In[41]:


plt.plot(x,y,'g+',linestyle='dashed',linewidth=2,markersize=10)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Grape')
plt.savefig('Test.png')


# In[55]:


## Creating  subplots

plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(y,x,'g--')
plt.subplot(2,2,3)
plt.plot(x,y,'b--')
plt.subplot(2,2,4)
plt.plot(y,x,'y--')


# In[60]:


plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Grape')
plt.subplot(2,2,2)
plt.plot(y,x,'g--')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Grape')
plt.subplot(2,2,3)
plt.plot(x,y,'b--')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Grape')
plt.subplot(2,2,4)
plt.plot(y,x,'y--')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Grape')


# In[67]:


# Bar plots

x1=[2,3,4,5]
y1=[11,16,19,20]
plt.bar(x1,y1,color='g')

x2=[3,9,11,14]
y2=[6,15,7,9]
plt.bar(x2,y2,color='r')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




