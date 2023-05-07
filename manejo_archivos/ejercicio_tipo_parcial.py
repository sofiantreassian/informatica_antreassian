#ejercicio manipulacion de archivos tipo parcial

#dentro del repo new que descargo, abro resultados, abro marzo y estan los archivos txt 

#!/usr/bin/env python3
import os, glob, sys 

# primero me voy a mover a esa carpeta (marzo), despues extraigo los archivos txt, leo las primeras lineas, hacemos carpeta de salida (resultado), despues hacemos el nuevo archivo (salida.txt), despues ponemos las lineas en el archivo nuevo

def primeras_lineas(path_a_txt, path_resultado, salida):


    os.chdir(path_a_txt) #movemos a marzo
    textos = glob.glob("*.txt") #extraemos los txt
    primer_linea = []
    for txt in textos:
        with open (txt, "r") as texto:
            primer_linea.append (texto.readline())
    
    os.chdir ("../../")
    os.mkdir (path_resultado)
    with open (path_resultado)
    with open (salida, "a") as final.txt:
        for linea in primer_linea:
            final_txt.write(linea)


primeras_lineas ("datos/marzo", "resultado", "salida.txt")


#guada 

#definir un procedimiento que lea los archivos .txt que esten en la carpeta de marzo,
# y copie la primera linea de cada uno en un archivo dentro de la carpeta resulados
#(que debe estar dentro de new) 

#!-/usr/bin/en python3
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    #movemos a marzo
    #extraemos los .txt
    #leemos las primeras primeras_lineas
    #hacemos carpeta de salida (resultado)
    #hacer archivo (salida.txt)
    #poner lineas en archivo nuevo

    os.chdir(path_a_txt) #change direcory
    textos=glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())
    os.chdir("../../") # para moverse para atras 2 veces
    os.mkdir(path_resultado)
    with open(salida, "a") as  final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")
