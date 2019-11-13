import pandas as pd, json, re

class Selector(object):
    
    def __init__(self, path):
        self.csv_path = path
        self.output = {}
        
    def load_df(self):
        df = pd.read_csv(self.csv_path, sep=';')
        return df
    
    def clean_bad_strings(self):
        
        data = self.load_df()
        print("WARNING: Chequeando caracteres inválidos")
        apos = re.compile(r'\'[a-z]')
        
        for index, v in data['phrase'].iteritems():

            if re.search(apos, v):
                print("WARNING: Se ha omitido la fila ", index, v, " por tener caractéres inválidos")

                data_good_str = data.drop(index, axis=0)
        
        return data_good_str
        
    def clean_data(self):        
        data = self.clean_bad_strings()
        
        for index, row in data.iterrows():
            
            for dato in data['entities_obtained']:

                if len(dato) > 0: #Changing values from obtained
                    repl = re.sub(r"_Entity__name", "vaule", str(dato))
                    repl = re.sub(r"_Entity__entity_type", "e_type", repl)
                    repl = re.sub(r"_Entity__start_index", "start_index", repl)
                    repl = re.sub(r"_Entity__end_index", "end_index", repl)
                    repl = re.sub(r"_Entity__canon", "canon", repl)
                    repl = re.sub(r"_Entity__label", "label", repl)
                    repl = re.sub(r"_Entity__order", "ent_id", repl)

                    # Changing quotes to load pretty js
                    data["entities_obtained"] = data['entities_obtained'].replace(dato, repl)
                    data["entities_obtained"] = data['entities_obtained'].str.replace('\'', '\"')
                    data["entities_obtained"] = data['entities_obtained'].str.replace(r'\"{', r'{')
                    data["entities_obtained"] = data['entities_obtained'].str.replace(r'\"}', r'}')
                    data["entities_obtained"] = data['entities_obtained'].str.replace('None', 'null')

            for dato in data['entities_expected']:
                
                if len(dato) > 0:
                    data["entities_expected"] = data['entities_expected'].str.replace('\'', '\"')
                    data["entities_expected"] = data['entities_expected'].str.replace('None', 'null')
                    
        return data
    
    def load_data_as_js(self):
        clean_data = self.load_df()
        clean_data = self.clean_data()

        for i in clean_data['entities_expected']:
            try:
                js_exp = json.loads(i)
                self.output.append(js_exp)
            except:
                print(i, ' EXP DA ERROR')
                continue

        for e in clean_data['entities_obtained']:
            #js=json.loads(e)
            try:
                js_obt = json.loads(e)
            except: 
                #print(e, ' OBT DA ERROR')
                continue
                    
        return "esperado", js_exp, "obtenido", js_obt
        
#         for e in data['entities_obtained']:
#             for k, v in e.items():
#                 print(k)