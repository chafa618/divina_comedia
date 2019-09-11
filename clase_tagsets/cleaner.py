import unidecode
#Uso estas estructuras para meter las lineas de freeling
class FreelingLine:
	def __init__(self, word, posibleLemmmas):
		self._word = word
		self._posibleLemmmas = posibleLemmmas

	def printLemmas(self):
		lemmas = []
		for posibleLemmma in self._posibleLemmmas:
			if self._word == posibleLemmma.concept():
				lemmas.append(posibleLemmma)

		if lemmas:
			print(self._word, end='')
			for lemma in lemmas:
				print("\t", end='')
				lemma.print()
			print("")

	def printExceptions(self, exceptionsList):
		lemmas = []
		for posibleLemmma in self._posibleLemmmas:
			if unidecode.unidecode(self._word) in exceptionsList:
				lemmas.append(posibleLemmma)

		if lemmas:
			print(self._word, end='')
			for lemma in lemmas:
				print("\t", end='')
				lemma.print()
			print("")

	def word(self):
		return self._word

	def lemmas(self):
		return self._posibleLemmmas

class Concept:
	def __init__(self, concept, msi):
		self._concept = concept
		self._msi = msi

	def concept(self):
		return self._concept

	def print(self):
		print(self._concept + "\t" + self._msi, end='')

	def msi(self):
		return self._msi

freeling = "ES.dict" 
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
print("Concepto: " + freelingList[0].word() + " msi: " + freelingList[0].lemmas()[0].msi())
