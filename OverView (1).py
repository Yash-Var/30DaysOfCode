#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("yash varshney")


# In[4]:


print("yash is good coder")


# In[5]:


print("yash")


# # Learn Basics


new_string=input("Enter the even lenght string : ")
user=new_string
ans=""
emp_str = ""
f=""

for m in new_string:
    if m.isdigit():
        emp_str = emp_str + m
       
for n in user:
    if n.isalpha():
        ans = ans + n

flag=0

for q in emp_str:
    temp=ord(ans[flag])-ord('a')
    temp=(temp+int(q))%26
    f=chr(temp+ord('a'))
    flag+=1
    print(f,end="")



n= int(input(" Enter any Number: "))
count=0;
for i in range(2, n+ 1):
    if(n % i == 0):
        prime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                prime = 0
                break
            
        if (prime == 1):
            count+=1
print(count)







lt=[1,2,3,4,5,6,7,8,9]
print(lt)
# List comprehension
new_list=[]
for i in lt:
    new_list.append(i**2)
    print(i)
print(new_list)