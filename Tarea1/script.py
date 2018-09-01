import modulo
import re

def mainCharacters(string):
	automata = re.compile("(?<=-)[A-Z ]*(?=:)",re.MULTILINE)
	chars = list(set(automata.findall(string)))
	chars.sort()
	return chars

def dialogs(string,characters):
	d = dict()
	for char in characters:
		automata = re.compile("(?<=-"+char+": ).*$",re.MULTILINE)
		d[char]=automata.findall(string)
	return d


string = modulo.leer_archivo()
characters = mainCharacters(string)
print(characters)
d = dialogs(string,characters)
for wea in d["TONY"]:
	print(wea)