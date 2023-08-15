#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_set = {55,45,67,77,1,5,7,0,3,4, 3, 3 ,3}
my_set


# In[4]:


get_ipython().run_cell_magic('time', '', 'my_set = {55,45,67,77,1,5,7,0,3,4, 3, 3 ,3}\nmy_set\n\nmy_set ={1.0}\n')


# In[5]:


thisset ={"apple", "banana", "cherry", True, 1, 2} #true and 1 are same, treated as duplicates
print(thisset)


# In[6]:


#length of set
print(len(thisset))


# In[13]:


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {(2, 3, 4, 5)}
print(set1)
print(set2)
print(set3)
print(set4)


# In[12]:


print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))


# In[14]:


print(set1)


# In[15]:


set1.add('orange') #add


# In[16]:


print(set1)


# In[17]:


print(set1.update(set2)) #update


# In[18]:


print(set1)


# In[23]:


print(set1)


# In[24]:


print(thisset)


# In[25]:


thisset.remove('apple') #remove


# In[26]:


print(thisset)


# In[27]:


thisset.discard('banana') #discard


# In[28]:


print(thisset)


# In[29]:


set5 = {'ravi', 'raj', 'kiran', 'ram', 'kumar'}
print(set5)


# In[39]:


set5 = {'ravi', 'raj', 'kiran', 'ram', 'kumar'}
x = set5.pop() #pop
print(x)
print(set5)


# In[40]:


x = set5.clear()
print(set5)


# In[46]:


set5 = {'ravi', 'raj', 'kiran', 'ram', 'kumar'}
del set5
print(set5)


# In[ ]:


#joining two sets

