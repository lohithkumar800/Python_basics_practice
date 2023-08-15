#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = ['apple','banana','orange','butterfruit','jackfruit','grape']
for x in fruits:
    print(x)


# In[8]:


for x in fruits:
    if x == 'orange':
        break
    print(x)


# In[9]:


for x in fruits:
    if x == 'orange':
        continue
    print(x)


# In[13]:


numbers = {1,20,2}
for x in numbers:
    print(x)


# In[19]:


numbers = {1,20,2}
for x in range({0,20,2}):
    print(x)


# In[17]:


numbers = (0,20,2)
for x in range(0,20,2):
    print(x)


# In[23]:


for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("completed")


# In[30]:


for x in range(6): 
    if x == 3:
        print(x)
    else:
        print("completed")


# In[25]:


def god('ganesha'):
    if god == 'ganesha':
        print("first god")
    
god('ganesha')


# In[45]:


def god(god_name):
    if god_name == 'ganesha':
        print("first god")
    elif god_name == 'shaneshwara swamy':
        print("god of goodwill")
    else:
        print("other gods")
        
god('venakteshwara')
god('ganesha')
god('shaneshwara swamy')


# In[9]:


def tv(price):
    tv_brands = 15000
    while tv_brands < 15000:
        print("choose croma")
        break
    else:
        print("go with others")

tv(15000)


# In[14]:


#conditional statements
a=505
b=1000

if b > a:
    print("b is greater than a")
    print(b)
else:
    print("b is less than a")


# In[17]:


a=35
b=33

if b > a:
    print("b is greater than a")
    print(b)
elif b==a:
    print("b is less than a")
else:
    print("a is not equal to a")
    print("b is less than a")


# In[18]:


price = 200
if price > 200:
    print("price is greater than a")
elif price == 100:
    print("price is equal to 100 rupees")
else:
    print("price is less than 200")


# In[19]:


a=100
b=150
c=250
if a>b and b<c:
    print("both conditions are true")
else:
    print("both conditions are not true")


# In[21]:


a=500
b=100
c=250
if a>b and b<c:
    print("both conditions are true")
else:
    print("both conditions are not true")


# In[24]:


a=500
b=100
c=250
if a>b or b==c:
    print("any one of the condition is true")
else:
    print("both conditions are not true")


# In[ ]:


#nested if
    basic_salary = 15000
    total_salary = 20000
    other_allowance = 5000
    total_salary = basic_salary + other_allowance
     
    


# In[27]:


sum = lambda x,y:x+y


# In[28]:


sum(1,2)


# In[ ]:




