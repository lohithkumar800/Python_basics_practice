#!/usr/bin/env python
# coding: utf-8

# In[2]:


tup1 =()
tup1


# In[3]:


tup2 = (99,)


# In[5]:


tup3=("lohith", "rahul", "hello")
tup3


# In[12]:


week = ("mon", "tue", "wed", "thur", "fri", "sat", "sun")
print(week[0][2])
print(week[5][1])
print(week[:3])
print(week[-4:-1])
print(week[-4][-1])


# In[15]:


my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(my_data[2:5])
print(my_data[:4])
print(my_data[4:])
print(my_data[4:-1])
print(my_data[:-4])


# In[1]:


#PRACTICE


# In[2]:


#Empty tuple
my_tuple = ()
print(my_tuple)


# In[3]:


#tuple having integers
my_tuple =("1", "2", "3")
print(my_tuple)


# In[4]:


#tuple having mixed data types
my_tuple = ("1", "Lohith", "2.44")
print(my_tuple)


# In[5]:


#nested tuple
my_tuple = (1,2,3,{34, 35, 36},["ram", "arjun", "ravi"])
print(my_tuple)


# In[7]:


#tuple can be created without using paranthesis
my_tuple = 1, 2, 3, 4
print(my_tuple)


# In[8]:


#2
my_tuple = "1", "lohith", "2.35"
print(my_tuple)


# In[10]:


#Create a Python Tuple With one Element
my_tuple = ("hello")
print(my_tuple)


# In[12]:


my_tuple = ("hello",)
print(my_tuple)


# In[13]:


#type of variable
var1 = ("hello")
print(type(var1))


# In[15]:


var2 = ("hello",)
print(type(var2))


# In[17]:


var3 = "hello",
print(type(var3))


# In[18]:


#indexing
my_tuple = ('a', 'e', 'i', 'o', 'u')
print(my_tuple)


# In[20]:


print(my_tuple[0]) #positive indexing


# In[22]:


print(my_tuple[0:2]) #slicing


# In[23]:


print(my_tuple[-4]) #negative indexing


# In[24]:


print(my_tuple[-5:-1]) #slicing


# In[33]:


#Python Tuple Methods
#count
my_tuple = ('a', 'e', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'i','l')
print(my_tuple.count('i'))


# In[34]:


print(my_tuple.count('e'))


# In[35]:


#index
print(my_tuple.index('e'))


# In[36]:


print(my_tuple.index('a'))


# In[37]:


my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(my_data)


# In[38]:


print(22 in my_data)
print(2 in my_data)
print(88 not in my_data)
print(101 not in my_data)


# In[39]:


my_data1 =(1, 2, 3, 4, 5)
del my_data1


# In[40]:


print(my_data1)


# In[42]:


my_data2 =(1, 2, 3, 4, 5)
del my_data2[2]


# In[44]:


my_data2 =(1, 2, 3, 4, 5)
del my_data2
try:
    print(my_data2)
except Exception as ex
    print("print(my_data2) => Error:", ex)


# In[ ]:




