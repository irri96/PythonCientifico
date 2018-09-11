# -*- coding: utf-8 -*-
import re
def leer_archivo(nombre = "guion.txt"):
    #entrada: nombre archivo
    #salida: string
    #guion.txt y modulo.py deben estar en el mismo directorio de su script
    with open(nombre, "r") as a:
        return a.read()
        
#Para usar la funcion, puede utilizar la siguiente linea de codigo en su script
#string = leer_archivo()

def dialogos (personaje, guion):
    #entrada: personaje (string), guion (string)
    #salida: otro_personaje (string)
    lista = guion.split("\n\n")
    otro_personaje = []
    automata = re.compile("(?<=-"+personaje+": ).*$",re.MULTILINE)
    for i in lista:
        x = automata.findall(i)
        if len(x)>0:
            y = lista[lista.index(i)+1]
            z = findCharacter(y)
            if z is not None and z != personaje:
                otro_personaje.append(findCharacter(y))
            
        otro_personaje = list(set(otro_personaje))
    print "Personajes con los que %s interactúa: " % (personaje)
    print otro_personaje
    return otro_personaje
        
    
def findCharacter(string):
    automata = re.compile("(?<=-)[A-Z ]*(?=:)",re.MULTILINE)
    chars = automata.findall(string)
    if len(chars) > 0:
        return chars[0]

    #return otro_personaje
