#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(5,6.54555)


# In[3]:


print("integer: %d, float: %.2f" %(5,6.54555) )


# In[4]:


print("integer: %2d, float: %10.2f" %(5,6.54555) )


# In[5]:


print("integer: %d, float: %5.f" %(5,6.54555) )


# In[10]:


print("integer: %d, float: %.f" %(5,6.54555) )


# In[19]:


#format() method

print("default_order: ")
print("{},{} and {}".format('Lohith','Ramesh','Tilak'))


# In[20]:


print("positional_order: ")
print("{0},{2} and {1}".format('Lohith','Ramesh','Tilak'))


# In[21]:


print("keyword_order: ")
print("{s0},{s1} and {s2}".format(s0='Lohith', s1='Ramesh', s2='Tilak'))


# In[22]:


a = 345
b = 455.5677

print("{},{}".format(a,b))


# In[25]:


print("{:d},{:.2f}".format(a,b))


# In[31]:


print("{:2d},{:10.2f}".format(a,b))


# In[36]:


name = "John"
print("hello, %s!" %name)


# In[ ]:




