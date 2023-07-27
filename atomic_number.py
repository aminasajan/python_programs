#!/usr/bin/env python
# coding: utf-8

# In[4]:


# python program to get details of an element by atomic number
import periodictable
atomic_no=int(input("Enter element atomic no. "))
element=periodictable.elements[atomic_no]
print('Atomic no.:',element.number)
print('Symbol: ',element.symbol)
print("Name: ",element.name)
print("Atomic mass: ",element.mass)
print("Density: ",element.density)


# In[ ]:





# In[ ]:




