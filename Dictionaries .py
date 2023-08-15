#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {}


# In[3]:


my_dict = {1:'apple', 2:'ball'}
print(my_dict)


# In[4]:


thisdict = {"brand":"ford",
           "model":"mustang",
           "year":"1992"}
print(thisdict)


# In[7]:


print(thisdict["brand"])


# In[8]:


thisdict = {"brand":"ford",
           "model":"mustang",
           "year":"1992","year":1994} #Duplicates are not allowed
print(thisdict)


# In[10]:


#length
print(len(thisdict))


# In[11]:


print(type(thisdict))


# In[13]:


#dict constructor used to make dictionary
thisdict = dict(name = 'john', country = 'norway', age= '36')
print(thisdict)


# In[14]:


#acess dictionary values 
#to acess particular item in a dictionary we can use key
thisdict = {"brand":"ford",
           "model":"mustang",
           "year":"1992"}
print(thisdict)


# In[15]:


print(thisdict['model'])


# In[16]:


x = thisdict.get('model') #get method to acess particular item in dictionary
print(x)


# In[17]:


# key() method to acess all items in dictionary
x = thisdict.keys()
print(x)


# In[20]:


car = {'brand': 'toyota', 'model': 'glanza', 'year': '2023'}
print(car)


# In[21]:


x = car.keys()
print(x) #before update of keys in car dictionary


# In[23]:


car['color'] = 'red'
print(x) #after update of keys in car dictionary


# In[24]:


x = car.values()
print(x) #before update of values in car dictionary


# In[25]:


car['year'] = 2024
print(x) #after update of values in car dictionary


# In[26]:


print(car)


# In[28]:


x = car.items()
print(x) #before update of items in car dictionary


# In[29]:


car['brand'] = 'maruthi'
car['model'] = 'baleno'
car['year'] = '2023'
car['color'] = 'white'
x = car.items() #after update of items in car dictionary
print(x)


# In[30]:


print(car)


# In[36]:


#check if key exists
if 'model' in car:
    print("yes,'model' exists car dictionary")


# In[39]:


#update methood
car.update({'color':'red'})
print(car)


# In[41]:


#pop method is use to remove specific item in a dictionary
car.pop('color')
print(car)


# In[42]:


car.popitem() #popitem method is use dto remove last item in a dictionary
print(car)


# In[43]:


car = {'brand': 'tata', 'model': 'tiago', 'year': '2023'}
print(car)


# In[3]:


car = {'brand': 'tata', 'model': 'tiago', 'year': '2023'}
print(car)


# In[4]:


car.clear()
print(car)


# In[5]:


car = {'brand': 'tata', 'model': 'tiago', 'year': '2023'}
print(car)


# In[6]:


for x in car: #to print keys in for loops
    print(x)


# In[7]:


for x in car: # to print values in for loops
    print(car[x])


# In[8]:


for x in car.values(): #to return values of a dictionary
    print(x)


# In[10]:


for x in car.keys(): #to return the keys of a dictionary
    print(x)


# In[9]:


for x in car.items(): #method to return the keys of a dictionary
    print(x)


# In[12]:


facebook = {'Username':'Ravi', 'Year':'2003', 'Education' :'B.E', 'Working in':'Bosch'}
print(facebook)


# In[13]:


online_user = facebook.copy() #copy method
print(online_user)


# In[14]:


online_user = dict(facebook)
print(online_user)


# In[22]:


#nested dictionaries
Instagram = {'user1':{'Username': 'Lohith', 'No of Followers': '745', 'Following': '55', 'status': 'active'},
             'user2':{'Username': 'Rajkumar', 'No of Followers': '1265', 'Following': '135', 'status': 'not active'},
             'user3':{'Username': 'Vishnu', 'No of Followers': '1125', 'Following': '87', 'status': 'active'}}
print(Instagram)


# In[23]:


print(Instagram['user1']['Username'])


# In[24]:


raj = {'films':'200', 'awards':'58', 'Fansclub':'1100'}
print(raj) 


# In[27]:


x = raj.setdefault('awards', '58') #setdefault
print(x)

