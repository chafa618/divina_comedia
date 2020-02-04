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
        
    def get_ents(self):
        """
        Obtain entity values ( r'\[.+?\]' ) for each sent of an intent (key) in a trainingset json file
        """
        open_file = self.load_json()
        
        entidadRe = re.compile(r'\[.+?\:(.+?)\]')
        #entidades = []
        dic = {}

        for intent in open_file['intents'].keys(): # Recorro mirando cada intent
            dic[intent] = []

            for utterance in open_file['intents'][intent]: # Recorro mirando cada oracion en cada intent
                ent = re.findall(entidadRe,utterance)

                if len(ent) >= 1:  
                    dic[intent].append(ent)
                else:
                    dic[intent].extend(ent)

        return dic

    def count_ents_for_intent(self):
        claves = self.get_ents()

        output = {}
        for intent in claves:
            output[intent] = {}

            for utt in claves[intent]:
                #print(utt)
                key = ",".join(claves[intent][claves[intent].index(utt)])
                output[intent][key] = claves[intent].count(utt) 
        self.output = output ## lleno el atributo con la contabilización de las utt
        return output

    def cross_check(self, ):
        cuenta = self.count_ents_for_intent()
        outpt = {}

        for int_group in cuenta:
            dic_chec = {}
            for combinacion in int_group:
                print(combinacion)
                chec = []
                if combinacion in chec:
                    continue
                else: 
                    chec.append((combinacion, int_group))
                print(chec)
            dic_chec[chec[1]] = chec[0]
        outpt=dic_chec

        return outpt

    
    def save(self, name):
        with open(name+'.json', 'w') as file:
            json.dump(self.output, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
   
    Counter = Counter_entities(args.path)
    Counter.count_ents_for_intent()
    #Counter.cross_check()
    Counter.save("contabilizacion")
