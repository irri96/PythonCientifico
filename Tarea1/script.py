# -*- coding: utf-8 -*-
import modulo
import re

def mainCharacters(string):
	""" Genera una lista con los personajes
		Argumentos:
		string -- guion completo de la pelicula

	"""
	automata = re.compile("(?<=-)[A-Z ]*(?=:)",re.MULTILINE)
	chars = list(set(automata.findall(string)))
	chars.sort()
	return chars

def dialogs(string,characters):
	""" Genera un diccionario (personaje : lista de dialogos)
		Argumentos:
		string -- guion completo de la pelicula
		characters -- lista de strings de personajes

	"""
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
        (L,longestDialogue,Dial) = (len(w.split()),i,w) if len(w.split()) > L else (L,longestDialogue,Dial)
        (l,shortestDialogue,dial) = (len(w.split()),i,w) if len(w.split()) < l else (l,shortestDialogue,dial)
print("Dialogo mas corto %s : '%s'"%(shortestDialogue,dial))
print("Dialogo mas largo %s : '%s'"%(longestDialogue,Dial))
# list compression for the win
x = [(i,len(d[i])) for i in d]

M = max(d)
print "Personaje con más dialogos: %s" % (M)
m = min(d)
print "Personaje con menos dialogos: %s" % (m)

p = raw_input("Nombre de personaje a buscar con quien interactua: ")
interacciones = modulo.dialogos(p,string)

