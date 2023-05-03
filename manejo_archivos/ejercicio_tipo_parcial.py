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
