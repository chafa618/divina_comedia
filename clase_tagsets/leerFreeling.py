
import cleaner

freeling = "freeling_es_sm.dict" 
freelingList = []
#parseo todas las lineas y las meto en la estructura correspondiente
for line in open(freeling, 'r', encoding='cp1252'):
	line =line.replace("\n",'')
	parsedLine = line.split("\t")
	lemmas = []
	if "//" in parsedLine[0]:
		continue
	for i in range(1,len(parsedLine),2):
		if "//" in parsedLine[i] or "//" in parsedLine[i+1]:
			break
		lemmas.append(Concept(parsedLine[i], parsedLine[i+1]))
	freelingList.append(FreelingLine(parsedLine[0], lemmas))
#Agarro la primera linea de freeling e imprimo el concepto y el
print("Item: " + freelingList[0].word() + " msi: " + freelingList[0].lemmas()[0].msi())

