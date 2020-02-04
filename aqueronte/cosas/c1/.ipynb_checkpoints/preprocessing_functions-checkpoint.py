import re
from string import punctuation

def make_lowercase(string):
    return string.lower()

def remove_diacritics(string):
    return string.translate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'))

def remove_punctuation(string):
    return re.sub('[{}]'.format(punctuation + '¿¡…'), ' ', string)

def remove_excess_whitespace(string):
    return re.sub(r' +', ' ', string).strip(' ')