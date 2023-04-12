# si dice main es que estoy en mi repo
#en bash pongo git add . // despues pongo git commit -m "y algun comentario aca" // por ultimo pongo git push 
#asi ya subi lo que quiero a mi repo de github 
#chequeo en github que se actualizo mi repo

#os.mkdir(ruta) me permite crear una carpeta. de ruta (entre comillas) le pongo donde la quiero crear. con os.chdir(ruta) me muevo a la carpeta que quiero crear 
#os.mkdir("../Escritorio/carpeta")

#siempre antes de hacer un script pongo #!
#!/usr/bin/env python3 asi le digo que busque y ejecute en la ruta python 

# (../../) PARA moverme a una carpeta de arriba si todavia no estoy ahi. x ejemplo (../../"informes")

#ejercicio de practica

#!

import os
import glob
import sys

# Movemos a la carpeta Informes
os.chdir('Informes')

# Obtenemos los archivos .txt en la carpeta
archivos_txt = glob.glob('*.txt')

# Inicializamos un diccionario para almacenar los resultados
resultados = {}   

# Iteramos sobre cada archivo_txt
for archivo in archivos_txt:

    # Abrimos el archivo
    with open(archivo, 'r') as archivo:

        # Leemos todas las líneas
        lineas = archivo.readlines()

        # Obtenemos la cantidad de líneas
        cantidad_lineas = len(lineas)

        # Obtenemos la cantidad de veces que aparece la palabra 'estado'
    for linea in lineas:
	    if 'estado' in linea:
		    cantidad_estado = cantidad_estado + 1	

        # Guardamos los resultados en el diccionario
resultados[archivo] = (cantidad_lineas, cantidad_estado, lineas[0])

# Creamos la carpeta Apellidos (si no existe)
if not os.path.exists('Apellidos'):
    os.mkdir('Apellidos')

# Creamos el archivo Lista.txt y escribimos la primera línea de cada archivo
with open('Apellidos/Lista.txt', 'w') as f:
    for archivo, (cantidad_lineas, cantidad_estado, primera_linea) in resultados.items():
        f.write(primera_linea)
        f.write('\n')


#Resolucion Guille 

#!/usr/bin/env python3

import os, glob, sys

def ejercicio_rutas():
     os.chdir("Informes")
     txt = glob.glob("*.txt")
     cantidad_estado = []
     cantidad_lineas = []
     for archivo in txt:
          with open(archivo, "r") as file:
               file_completa = file.read()
               cantidad_estado.append(file_completa.count("estado"))
               cantidad_lineas.append(file_completa.count("\n"))

     os.mkdir ("Apellido")
     with open ("Apellido/Lista.txt" , "w") as salida:
        for archivo in txt:
             with open(archivo, "r") as file:
                  #primer_linea = file.readline()
                  #salida.write(primer_linea)
                  salida.write(file.readline())
     return cantidad_estado, cantidad_lineas

c1, c2 = ejercicio_rutas()
