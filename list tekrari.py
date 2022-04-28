#!/usr/bin/env python
# coding: utf-8

# In[4]:


def all_uniqe(lst):
    return len(lst) == len(set(lst))  
x = [1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_uniqe(x) #Fals
all_uniqe(y) #True


# In[ ]:




