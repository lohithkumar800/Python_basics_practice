#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


text = "I am Lohith,learing data analytics"


# In[4]:


re.sub("\s", "@", text)


# In[5]:


re.sub("\S","@",text)


# In[9]:


text2 = "Famous Kannada actor Shankarnag was died in 1992"


# In[10]:


re.sub("\d", "$", text2)


# In[11]:


re.sub("\D", "$", text2)


# In[12]:


re.split("\s",text2)


# In[13]:


text5 = "My address is 21/8A Navada, Delhi 319189"
#address-line1: 21/8A Navada
#address-line2: Delhi
#Pincode: 319189

#find
#findall
#split 
#{}
#/d


# In[14]:


re.split("\s",text5)


# In[20]:


print(text5)


# In[30]:


address1 = re.findall("21/8A Navada",text5)
print("address-line1:",address1)

address2 = re.findall("Delhi",text5)
print("address-line2:",address2)

address3 = re.findall("319189",text5)
print("Pincode:",address3)


# In[34]:


address5 = re.search("21/8A Navada",text5)
print("address-line1:",address5)

address6 = re.search("Delhi",text5)
print("address-line1:",address6)

address7 = re.search("319189",text5)
print("address-line1:",address7)


# In[36]:


re.sub("\s", "@", text5)


# In[37]:


re.sub("\S","@",text5)


# In[38]:


re.sub("\d", "$", text5)


# In[39]:


re.sub("\D", "$", text5)


# In[41]:


print(text5)

address8 = re.find("21/8A Navada",text5)
print("address-line1:",address8)

address9 = re.find("Delhi",text5)
print("address-line1:",address9)

address10 = re.find("319189",text5)
print("address-line1:",address10)


# In[ ]:




