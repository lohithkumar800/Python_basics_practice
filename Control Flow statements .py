#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Control flow statements
#if statements
car_speed = 60
if car_speed >= 60:
    print("Bangalore traffic police impose the fine for over speed ")


# In[2]:


#if_else statements
data = True
if data is True:
    print('Engineer starts using database')
else:
    print('Engineer not using database')


# In[3]:


#if_elif_else statements
is_distinction = True
is_passed = True

if is_distinction:
    print("Awesome, you have passed in distinction")
elif is_passed:
    print("Congrats, you have passed")
else:
    print("Sorry you have failed")


# In[4]:


#Nested_if statements
age = int(input("age:  "))
is_student = input("student? (yes/no):  ")

if age >= 60:
    print("Eligible for discount in Bus pass")
else:
    if is_student == "yes":
        print("Students are also eligible for Bus pass discounts")
    else:
        print("Not eligible for any discount")


# In[5]:


#pass statements
age = 10
if age >= 10:
    pass
    print("kids eligible for chocolates")


# In[6]:


#Break statements
for age in range(10):
    if age == 5:
        break
    print(age)


# In[7]:


#continue statements
for place in range(5):
    if place == 3:
        continue
    print(place)


# In[8]:


#for loop 

cart = { 'banana': '40 rupees',
       'apple': '50 rupees',
       'orange': '60 rupees',
       'mosambi': '60 rupees'}

print(cart.items())

for item, price in cart.items():
    print(f"{item}: {price}")


# In[9]:


# for loop

cart = { 'banana': '40 rupees',
       'apple': '50 rupees',
       'orange': '60 rupees',
       'mosambi': '60 rupees'}

print(cart.items())

for item, price in cart.items():
    numerical_price = int(price[:-7])
    if numerical_price >= 50:
        print(f"{item}: {price}")


# In[10]:


#while loop

attempts = 0
maximum_attempts = 3

while attempts < maximum_attempts:
    print("attempts are over, please try later")
    attempts += 1
else:
    print("next attempt starts")

