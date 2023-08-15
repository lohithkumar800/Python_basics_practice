#!/usr/bin/env python
# coding: utf-8

# In[4]:


number_list = range(-5,5)
less_than_zero =list(filter(lambda x:x**2, number_list))
print(less_than_zero)


# In[5]:


def loan(amount):
    if amount <= 200000:
        return  lambda new : new * amount 
    else:
        print("not eligible")

my_loan = loan(150000)

print(my_loan(1.11))


# In[6]:


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1)
print(list2)

list1 = list2
list1[2] = 45

print(list1)
print(list2)


# In[7]:


list1


# In[8]:


list2


# In[9]:


id(list1)


# In[10]:


id(list2)


# In[11]:


list3 = [60,61,62,63,64,65]


# In[12]:


list4 = [70,71,72,73,74,75]


# In[13]:


list3


# In[14]:


list4


# In[15]:


list11 = list3.copy()


# In[16]:


list11


# In[17]:


list3


# In[20]:


list3[2] = 55
list3


# In[21]:


list11[2]


# In[22]:


list3[2]


# In[23]:


id(list11[2])


# In[24]:


id(list3[2])


# In[27]:


from copy import deepcopy


# In[30]:


list55 = [[45,46,47,48,49,50], [54,55,56,57,58,59,60]]
list55


# In[32]:


list65 = deepcopy(list55)


# In[33]:


list65


# In[36]:


list55[1][1] =98
print(list55)
id(list55[1][1])


# In[37]:


print(list65)
id(list65[1][1])


# In[38]:


list55


# In[39]:


list65


# In[1]:


list101 =[71,72,73,74,75]


# In[2]:


list102 =[81,82,83,84,85]


# In[3]:


print(list101)
print(list102)

list102 = list101

list102[1] = 80

print(list101)
print(list102)


# In[6]:


id(list101[1])


# In[5]:


id(list102[1])


# In[7]:


list103 =[60,61,62,63,64,65]
list104 =[78,79,80,81,82,83]

list104 = list103.copy()


# In[8]:


list104


# In[9]:


list103


# In[10]:


list103[1]


# In[11]:


list104[1]


# In[12]:


id(list103[1])


# In[13]:


id(list104[1])


# In[14]:


list103[1] = 55


# In[15]:


list103


# In[21]:


list104
list104 = list103.copy()


# In[22]:


id(list103[1])


# In[23]:


id(list104[1])


# In[24]:


list104


# In[25]:


list103


# In[26]:


list104[1]


# In[27]:


list104[1]


# In[28]:


list103[1]


# In[30]:


list103[2] = 105
list103


# In[31]:


list104


# In[32]:


id(list104[2])


# In[33]:


id(list103[2])


# In[34]:


list104 = list103.copy()


# In[35]:


list103


# In[36]:


list104


# In[37]:


id(list104[2])


# In[38]:


id(list103[2])


# In[39]:


from copy import deepcopy


# In[40]:


list25 = [[145,146,147,148,149,50], [154,155,156,157,158,159,160]]
list25


# In[42]:


list26 = deepcopy(list25)
list26


# In[43]:


list25[1][1] = 108
print(list25)
id(list25[1][1])


# In[44]:


print(list26)
id(list26[1][1])


# In[48]:


list26 = deepcopy(list25)
id(list25[1][1])
list26


# In[50]:


id(list25[1][1])
list25


# In[51]:


id(list26[1][1])


# In[52]:


id(list25[1][1])


# In[ ]:




