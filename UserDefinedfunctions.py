#!/usr/bin/env python
# coding: utf-8

# In[16]:


def plus(*args):
    total = 0
    for i in args:
         total += i
    return total

plus(20,30)


# In[18]:


def plus(*args):
    total = 0
    for i in args:
         total += i
    print(total)

plus(20,30)


# In[24]:


def add(a, b):
    sum = a + b
    return sum

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
res = add(a, b)
print("Result =", res)


# In[3]:


a=10
c=20
def display():
    a=20
print(a)


# In[8]:


def course(a, b, c):
    subjects = [a, b, c]
    
    if "python" in subjects:
        print("student into datascience")
    else:
        print("student looking for other interests")
    
    if "power_bi" in subjects:
        print("student into visualization of datascience")
    else:
        print("student looking for other interests")
        
    if "data_analytics" in subjects:
        print("student into visualization of data analytics")
    else:
        print("student looking for other interests")

# Example usage:
course("python ", "data_analytics", "sql")
        


# In[20]:


def city(city1,city2,city3):
    if city1 == 'big':
        print('Bangalore')
    elif city2 == 'medium':
        print('Mangalore')
    else:
        print('Raichur')

city('big','medium','small')
        


# In[21]:


def plus(*args): #variable length arguents
    total = 0
    for i in args:
        total += i
    return total


# In[22]:


plus(1,2,3)


# In[24]:


plus(5,6,7)


# In[57]:


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# In[60]:


def man(country = "norway"):
    print("person lives in " + country)
    
man("norway")
man("india")


# In[ ]:




