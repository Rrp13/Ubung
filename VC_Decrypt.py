#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string

def cipher(key,text):
    text=list(text)
    result=""
    for j, k in enumerate(key):
        mapping=generate_mapping(k)
        result+=("".join(mapping.get(text[j],text[j])))
    return result
    
def generate_mapping(k):
    return{**generate_partialmapping(k,string.ascii_lowercase),
      **generate_partialmapping(k,string.ascii_uppercase)}

def generate_partialmapping(k,alphabet_string):
    offset=offsetgen(k,string.ascii_lowercase)+offsetgen(k,string.ascii_uppercase)       
  
    return{char : alphabet_string[((i-offset+26)%26)] for i, char in enumerate(alphabet_string)}

def generateKey(text, keyword): 
    keyword = list(keyword) 
    if len(text) == len(keyword): 
        return(keyword) 
    else: 
        for i in range(len(text) - 
                       len(keyword)): 
            keyword.append(keyword[i % len(keyword)]) 
    return("" . join(keyword)) 

def offsetgen(k,string):
    for m,c in enumerate(string):
        if k==c:
            offset=m
            break
        else:
            offset=0
              
    return offset   
text=input("Enter Text ")
keyword=input("Enter Key ")
key=generateKey(text,keyword)
print("Decrypted Text "+ cipher(key,text))


# In[ ]:




