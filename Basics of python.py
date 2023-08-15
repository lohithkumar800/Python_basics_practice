#!/usr/bin/env python
# coding: utf-8

# In[1]:


#module
a = 5
b = 3
c = a%b


# In[2]:


print(c)


# In[3]:


#floor division
a = 5
b = 3
c = 5//3
print(c)


# In[4]:


cricketers = ["sachin", "dravid", "ganguly", "sehwag", "yuvraj"]


# In[5]:


print(cricketers)


# In[6]:


print(cricketers[-1]) #negative indexing


# In[7]:


print(cricketers[1]) #positive indexing


# In[8]:


li= [1,2,3,4,5,"hello"]


# In[9]:


print(li)


# In[10]:


li[5][2]


# In[11]:


print(cricketers)


# In[12]:


#range operator for dravid
cricketers[1][:3]


# In[13]:


cricketers.append('vvs lakshman') #append funtion


# In[14]:


print(cricketers)


# In[15]:


cricketers.remove('sehwag') #remove function
print(cricketers)


# In[16]:


cricketers.pop() #pop function
print(cricketers)


# In[17]:


cricketers.index('dravid') #index function


# In[18]:


print(cricketers.count('dravid')) #number of dravid name in the list


# In[19]:


en = [5,6,7,77,78,"lohith", [22,23,24]] #nested list
en [6][1] = "kiran"
print(en)


# In[20]:


tu = 33, 34, 35, 36, 'ranjith'


# In[21]:


type(tu)


# In[22]:


tu2 = tuple(en)


# In[23]:


type(tu2)


# In[24]:


print(tu2)


# In[25]:


tu2[6][1]


# In[26]:


tu2[6][1] = 'manu' #list property so value is changed


# In[27]:


print(tu2)


# In[28]:


tu2[1] = 'raj'


# In[29]:


set = {45, 46, 47, "rajkumar", "vishnuvardhan", "ambarish"}
print(set)


# In[30]:


di = {'course': ['DA', 'DS', 'RPA','AWS'], 'salary':[3.4, 5.6, 6.5, 7.5]} #key under value pair =Dictionaries
print(di)


# In[ ]:


di


# In[31]:


di['salary'][3] = 8.0
print(di)


# In[ ]:


di


# In[32]:


di['salary'][3] = 8.0


# In[ ]:


di


# In[34]:


di1 = {'a':{5,6,7,8}, 'b':{1,2,3,4}}


# In[33]:


print(di1)


# In[ ]:


di1['b'][2] = 'raj'
print(di)


# In[ ]:


di


# In[35]:


di['course'][3]


# In[ ]:


print(di)


# In[ ]:


li
tu
abc
se
di


# In[ ]:


li
tu
set
di


# In[36]:


print(li)
print(tu)
print(set)
print(di)


# In[37]:


ds_class = {'List':li, 'Tuple':tu, 'set':set, 'di':di}


# In[40]:


ds_class


# In[39]:


ds_class = {'List':li, 'Tuple':tu, 'set':set, 'di':di}


# In[44]:


#Control flow
science = 35
if science >= 35:
    print("pass")
else:
    print("fail")


# In[57]:


is_passed = True
if is_passed:
    print("Congrats, you have passed.")
else:
    print("Sorry, you have failed.")


# In[58]:


is_distinction=True
is_passed=True
if is_distinction:
    print("Awesome you have earned distinction")
elif is_passed:
    print("You have passed")
else:
    print("sorry you have failed")


# In[69]:


#For loop
for num in range(1, 11):
    print(num)


# In[70]:


#while program

num = 1

while num <= 5:
    print(num)
    num += 1


# In[11]:


#def function

def display():
  b = 20
  print("global",a)
  print("local", b)
display()


# In[12]:


a=10
c=30
def display():
    a=20
    print(a)    #local variable given first preference
display()

a=40
print(a)
d=a+c
print(d)


# In[14]:


#lambda function
sum = (lambda x,y:x+y)
print("sum =",sum(2,3))


# In[23]:


#escape sequence
print("Hello\nworld") #newline
print("Hello\'world") #singlequote
print("Hello\'' world")#doublequote
print("Hello\rworld")#carriage return
print("Hello\tworld")#tab
print("Hello\aworld")#bellescape sequence


# In[ ]:




