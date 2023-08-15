#!/usr/bin/env python
# coding: utf-8

# # if Statements

# In[1]:


#increment the value by 1
value = int(input("enter the value: "))
if value >= 0:
    value = value + 1
    print("incremented value is: ", value)


# In[2]:


#Determine weather a person is eligible to vote by using  input 
age = int(input("enter the your age: "))
if age >= 18:
    print("This person is eligible for voting")


# # if - else Statements

# In[3]:


#Determine weather a person is eligible to vote by using input 
age = int(input("enter the your age: "))
if age >= 18:
    print("This person is eligible for voting")
else:
    print("This person is not eligible for voting")


# In[4]:


#find the number is even or odd by using input 
number = int(input("enter the number: "))
if number % 2 == 0 :
    print("number is even")
else:
    print("number is odd")


# In[5]:


# A company decides to give bonus to all its employees on New year. A 10% bonus on salary for all the male workers and
# 25% to females. build a programme to enter Salary and Gender(m or F) of employee. 

salary = float(input("Enter the salary: "))
Gender = input("Are you Male/Female (m/F): ")
bonus = 0
if Gender == 'm' or Gender == 'M':
    bonus = 0.10
if Gender == 'f' or Gender == 'F':
    bonus = 0.25
    
total_salary = salary + (salary * bonus)  # Calculating total salary with bonus

if bonus == 0:
    print("Invalid gender input")
else:
    print("Total salary with bonus: ",total_salary)


# # if -elif- else Statement

# In[6]:


# check weather the number is positive or negitive or equal to zero using input
number = int(input("Enter the number: "))
if number == 0:
     print("number is equal to zero")
elif number < 0:
   print("number is negative to zero")
else:
   print("number is positive to zero")


# In[7]:


# Test Weather the charcter is vowel or not vowel using input
character = input("Enter a value: ")
if character == 'a' or character == 'A':
    print("it  is a vowel.")
elif character == 'e' or character == 'E':
    print("It is a vowel.")
elif character == 'i' or character == 'I':
        print("It is a vowel.")
elif character == 'o' or character == 'O':
     print("It is a vowel.")
elif character == 'u' or character == 'U':
     print("It is a vowel.")
else:
    print("It is not a vowel.")


# In[8]:


#Given an integer input perform the following conditional actions:

#If n is odd, print odd
#If n is even and in the inclusive range of 2 to 5, print small
#If n is even and in the inclusive range of 6 to 20, print medium
#If n is even and greater than 20, print big
n = int(input("enter the number: "))
if n % 2 != 0 :
    print("odd")
elif n % 2 == 0 and 2<=n<=5:
    print("small")
elif  n % 2 == 0 and 6<=n<=20:
    print("medium")
else:
    print("big")


# # while loop 

# In[9]:


# print first 10 numbers 
n = 1
while n<=10:
    print(n)
    n = n+1
    pass


# In[10]:


# find average and sum for first 10 numbers 

print("Enter 10 numbers")

i = 0  
s = 0  

while i < 10:
    n = int(input())  
    s = s + n  
    i += 1  

avg = s / 10  

print("The sum is =", s)
print("The average is =", avg)


# In[11]:


#Draw a line using while loop 
n = 0
while n>=0:
    print("___________")
    break
    


# In[12]:


#calculate the sum of m to n  numbers using input
m = int(input("Enter the first user_input: "))
n = int(input("Enter the second user_input: "))
sum = 0
while m<=n:
    sum += m
    m += 1
    
print("The sum of two numbers from m to n is ",sum)


# In[13]:


# countdown 10 to 0 using input
count = int(input("Enter the start number: "))
while count >= 0:
    print(count)
    count -= 1


# # for loop 

# In[14]:


#Multiplication table using input
num = int(input("Enter the number for multiplication table: "))

print(f"Multiplication table for {num}:")

for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")


# In[15]:


#print even and odd for range of number
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


# In[16]:


# break statement
fruits = ['apple','banana','orange','butterfruit','jackfruit','grape']
for x in fruits:
    if x == 'orange':
        break
    print(x)


# In[17]:


#countinue statement 
fruits = ['apple','banana','orange','butterfruit','jackfruit','grape']
for x in fruits:
    if x == 'orange':
        continue
    print(x)


# In[18]:


# all leap years from 1800 - 2021
for year in range(1800, 2022):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)


# # User defined function 

# In[19]:


#creating arethematic operators using user defined functions
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))


# In[20]:


#Welcome With input 



# In[ ]:





# # Lambda function 

# In[26]:


# sum using lambda function 
sum = lambda x,y:x+y


# In[22]:


# create a list using loop
list = []
for i in range(1, 11):
    list.append(i)

print(list)

# Create a list of first 10 number using list comprehension
numbers = [i for i in range(1, 11)]
print(numbers)


# In[37]:


# select all the even number form the list with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# In[34]:


# get  the squiares of numbers form the list with map()
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


# In[35]:


#get the sum of numbers of the list using reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)


# In[ ]:




