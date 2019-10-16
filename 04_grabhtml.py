
# coding: utf-8

# In[1]:


import requests


# In[2]:


url = 'http://www.ntcu.edu.tw/newweb/index.htm'


# In[3]:


htm = requests.get(url)


# In[4]:


htm.encoding="utf-8"


# In[5]:


htmllist = htm.text.splitlines()


# In[6]:


n = 0
for row in htmllist:
    if '本校' in row:
        n = n + 1
print("找到{}次".format(n))

