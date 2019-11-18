#!/usr/bin/env python
# coding: utf-8

# In[2]:


class json_facil(object):
    
    
    def __init__(self, path):
        self.json_path = path
        self.intents = []
        self.metadata = []
        
    
    def load_json(self):
        with open(self.json_path) as f:
            archivo = json.load(f)
        return archivo


# In[ ]:




