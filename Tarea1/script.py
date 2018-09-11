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
print("Personajes de la pelicula: ")
print characters
d = dialogs(string,characters)

longestDialogue = ""
shortestDialogue = ""
L = 0
l = 1000000000000000
for i in d:
    for w in d[i]:
        if len(w.split()) > L:
            L = len(w.split())
            longestDialogue = i
        elif len(w.split()) < l:
            l = len(w.split())
            shortestDialogue = i

x = []
for i in d:
    t = (i,len(d[i]))
    x.append(t)

M = max(d)
print "Personaje con más dialogos: %s" % (M)
m = min(d)
print "Personaje con menos dialogos: %s" % (m)

p = raw_input("Nombre de personaje a buscar con quien interactua: ")
interacciones = modulo.dialogos(p,string)

