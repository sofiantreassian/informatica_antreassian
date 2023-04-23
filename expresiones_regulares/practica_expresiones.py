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
    
#ejercicio 5
def empieza_con_numero(string,numero):
    return bool(re.search('^'+str(numero), string)) 

#ejercicio 6:

#ejercicio 7:
def min_num_espacios(string):
    return bool(re.search('[a-zA-Z0-9\s]+$',string))
    
#ejercicio 8 
def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for element in resultado:
        print (elemento)

#ejercicio 9 
def entre_guiones(string):
    return re.findall (r"-(.*?)-", string)

#ejercicio 10:
def subustrings(string):
    return re.findall('[@|&](.*?)[@|&]',string)

#ejercicio 11:
def dos_p(lista):
    lista_p = []
    posicion = -1
    for string in lista:
        posicion +=1
        if re.search("(P\w*)\W(P\w*)",string):
            lista_p.append(lista[posicion])
    return lista_p

#alternativa guille
def dos_P(lista):
    for elemento in lista:
        resultado = re.search("(P\w*)\W(P\w*)", elemento) 
        if resultado is not None:
            print(resultado.group())

#ejercicio 12:
def reemplazar_caracteres(string):
    return re.sub('[\s_:]','|',string)

#ejercicio 13:
def no_alfanumericos(string):
    return re.sub('[^a-zA-Z0-9]','_',string, count=2)

#ejercicio 14:
def reemplazar_espacio_tab(string):
    return re.sub('[\s\t]+',';',string)

#ejercicio 15:
def mail_correcto(string):
    return bool(re.search('^\w+[.-]?\w*@[a-zA-Z]+[.][a-z]+[.]?[a-z]?$',string))