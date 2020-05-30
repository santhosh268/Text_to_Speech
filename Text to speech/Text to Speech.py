
# coding: utf-8

# In[4]:


import pyttsx3


# In[11]:


engine=pyttsx3.init()
engine1=pyttsx3.init()


# In[9]:



engine.say("this is simple code")
engine.runAndWait()


# In[10]:


#let's create a function which converts our text to sppech


# In[12]:


def speechfun(audio):
    engine1.say(audio)
    engine.runAndWait()
speechfun("Function Created")

