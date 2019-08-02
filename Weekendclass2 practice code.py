#!/usr/bin/env python
# coding: utf-8

# In[10]:


#python numbers
    
x = 1 
y=2.0 
z=3+8j
print(type(x))
print(type(y))
print(type(z))


# In[12]:


x = 1 
y=2.0 
z=3+8j

a=float(x)
b=complex(x)

print(a,b)


# In[18]:


a=122343556678900
b=-1678490409576900
c=10.0766
d=-8.567
print(type(a))
print(type(b))
print(type(c)," ",type(d))


# In[19]:


f=float(z)
print(f, " ",type(f)," ",type(z))


# In[21]:


ff=int(z)
print(ff, " ",type(ff)," ",type(z))


# In[22]:


g=complex(y)
print(g,"",type(y))


# In[36]:


#list
mylist=["Gandhi","Sivaji","nehru","bose"]
print (mylist)
print(mylist[0].title())
print(mylist[2].upper())


# In[31]:


print(mylist[1])
print(mylist[1:])
print(mylist[1:3])
print(mylist*2)
print(mylist)


# In[32]:


myminilist=["Gujarat","Kolkata"]
print(myminilist.append[2,"delhi"])


# In[37]:


#append means just adding at the end of the list
#insert only adding new word to the wanted location

myminilist=["Gujarat","Kolkata"]
print(myminilist.append("kerela"))


# In[40]:


myminilist=["Gujarat","Kolkata"]
myminilist.append("kerela")
print(myminilist)


# In[42]:


myminilist=["Gujarat","Kolkata"]
myminilist.insert(3,"Goa")
print(myminilist)


# In[43]:


print(mylist+myminilist)


# In[ ]:




