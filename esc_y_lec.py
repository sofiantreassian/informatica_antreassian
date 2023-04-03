#clase teorica 20/3

#!/bin/python3

with open("mi_nombre.txt", "a") as mi_arch:
    mi_arch.write("Ana Julia Velez Rueda")

#tarea: armar un script que lea el archivo "un_arch.txt" y me cree otro archivo "nuevo_arch.txt" con los primeros 5 caracteres del archivo que leimos

#with open("un_archivo.txt", "r") as mi_arch:
    #with open("nuevo_archivo.txt", "a") as nuevo:
        #nuevo.write(mi_arch.readline(5))


texto_leido = open ("un_archivo.txt", "r").read()

texto_para_escribir = texto_leido[0:6]

with open("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_para_escribir)

import os
os.rename("nombre_archivo1", "nombre_archivo2" + ".temp")
os.rename("nombre_archivo2", "nombre_archivo1")
os.rename("nombre_archivo2.temp", "nombre_archivo2")
