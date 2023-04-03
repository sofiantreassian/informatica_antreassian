#clase teorica 20/3

#!/bin/python3

#atajos
#control a: seleccionar todo
#control s: guardar
#control j: terminal
#control d: selector multiple

#pongo ls para averiguar donde estoy, me voy metiendo a las carpetas poniendo cd y el nombre textual de la carpeta
#pongo exit () para salir de python (>>>). pongo python para entrar (e importo bibliotecas)
#ls: lista de archivos de un dir
#pwd: path del dir en que estoy
#cd: cambio de dir

import os, sys

#son dos bibliotecas. os me permite dialogar ccon la terminal fuera del interprete, mover archivos, manipular, ejecutar. system dialoga con el sist operativo y toma parametros que le paso al script desde la terminal.

usuario = sys.argv[1]

#sys.argv toma todos los arg que le paso al script por la terminal

def saludador(nombre):
    return "Hola " + nombre

if __name__ == "__main__":
    print (saludador(usuario))

#tarea: desafio final
