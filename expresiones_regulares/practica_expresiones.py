#Practica expresiones regulares 

import re

#ejercicio 1: Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
def caracteres_permitidos(string):
    return bool (re.search ('[a-zA-Z0-9.]', string))

#ejercicio 2: Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9
def caracteres_permitidos(string):
    return not bool (re.search ('[^a-zA-Z0-9]', string))

#ejercicio 3: Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de cero o una e.
#si un string dado tiene una h seguida de dos o tres e.

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
    
#ejercicio 4: Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "patron encontrado"
    else:
        return "patron no encontrado"
    
#ejercicio 5: Escribí un programa que diga si un string empieza con un número específico.
def empieza_con_numero(string,numero):
    return bool(re.search('^'+str(numero), string)) 

#ejercicio 6: Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

#ejercicio 7: Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
def min_num_espacios(string):
    return bool(re.search('[a-zA-Z0-9\s]+$',string))
    
#ejercicio 8: Escribí un programa que separe y devuelva los caracteres númericos de un string.
def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for element in resultado:
        print (element)

#ejercicio 9: Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
def entre_guiones(string):
    return re.findall (r"-(.*?)-", string)

#ejercicio 10: Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
def subustrings(string):
    return re.findall('[@|&](.*?)[@|&]',string)

#ejercicio 11: Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
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

#ejercicio 12: Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
def reemplazar_caracteres(string):
    return re.sub('[\s_:]','|',string)

#ejercicio 13: Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def no_alfanumericos(string):
    return re.sub('[^a-zA-Z0-9]','_',string, count=2)

#ejercicio 14: Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
def reemplazar_espacio_tab(string):
    return re.sub('[\s\t]+',';',string)

#ejercicio 15: Realizá un programa que validar si una cuenta de mail está escrita correctamente.
def mail_correcto(string):
    return bool(re.search('^\w+[.-]?\w*@[a-zA-Z]+[.][a-z]+[.]?[a-z]?$',string))