#Practica expresiones regulares 

import re

#ejercicio 1
def caracteres_permitidos(string):
    return bool (re.search ('[a-zA-Z0-9.]', string))

#ejercicio 2 
def caracteres_permitidos(string):
    return not bool (re.search ('[^a-zA-Z0-9]', string))

#ejercicio 3 
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
#ejercicio 4 
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "patron encontrado"
    else:
        return "patron no encontrado"
    
#ejercicio 8 
def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for element in resultado:
        print (elemento)

#ejercicio 9 
def entre_guiones(string):
    return re.findall (r"-(.*?)-", string)
