#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1,2,3,4,[5,6,7]]
for i in a:
    if isinstance(i,list):
        print(i)


# In[2]:


try:   
    get_ipython().system('jupyter nbconvert --to python test1.ipynb')
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass


# In[ ]:




