#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re 
import json
import argparse

class Counter_entities(object):
    """
    Count ent ocurrences for intent in file. The order of ents matters
    """
    
    def __init__(self, path):
        self.json_path = path
        self.output = {}
        
    
    def load_json(self):
        with open(self.json_path) as f:
            archivo = json.load(f)
        return archivo
        
    def get_keys(self):
        open_file = self.load_json()
        
        entidadRe = re.compile(r'\[.+?\]')
        entidades = []
        dic = {}

        for intent in open_file['intents'].keys():
            dic[intent] = []

            for utterance in open_file['intents'][intent]:
                ent = re.findall(entidadRe,utterance)

                if len(ent) >= 1:  
                    dic[intent].append(ent)
        return dic

    def count_ents_for_intent(self):
        claves = self.get_keys()

        output = {}
        for intent in claves:
            output[intent] = {}

            for utt in claves[intent]:
                #print(utt)
                key = ",".join(claves[intent][claves[intent].index(utt)])
                output[intent][key] = claves[intent].count(utt) 
        self.output = output ## lleno el atributo con la contabilización de las utt
        return output
    
    def save(self):
        with open('output.json', 'w') as file:
            json.dump(self.output, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
   
    Counter = Counter_entities(args.path)
    Counter.count_ents_for_intent()
    Counter.save()

