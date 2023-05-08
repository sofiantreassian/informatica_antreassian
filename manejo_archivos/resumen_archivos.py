#Manipulacion de archivos: Lectura y escritura de archivos con Python

# 1. Archivos
# existen de texto y binarios

# 2. Apertura de archivos

#para abrir un archivo de texto: funcion open()
#open(path_al_archivo, modo) 

#"path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. 
#"modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión.

#modos de lectura:
#r: abre el archivo solo para lectura 
#r+: lectura y escritura
#a: abre el archivo para agregar info. si el archivo no existe, crea uno nuevo para escritura
#w: abre un archivo solo para escritura. sobreescribe el archivo si este ya existe. si el archivo no existe, crea un nuevo archivo para escritura

# 3. Cierre de archivos 

#metodo close()
#archivo = open(path_al_archivo, modo) 
#archivo.close()

#existe otra forma de apertura de archivos que nos ahorra este paso y siempre nos asegura el cierre de adecuado:
#with open(path_al_archivo, modo) as miarch:
#Aquí van las líneas de procesamiento del archivo

# 4. Rutas absolutas y relativas 

# 5. Automatizacion en la contruccion de rutas 
#biblioteca os: proporciona funciones para interactuar con el sistema operativo. incluye métodos que como os.getcwd() o os.chdir(), que nos permitirá conocer el directorio de trabajo o cambiar de directorio de forma automática

# 6. Lectura y escritura de archivos

#como escribir en un archivo python: 
# with open(path_al_archivo, modo) as miarch:
#   miarch.write("Este es el contenido del archivo")

#un archivo se puede leer linea a linea o el archivo completo 

#bio = open("bio.txt", "r")
#bio.read()

#bio = open("bio.txt", "r")
#bio.readlines()

#En resumen, podemos utilizar los siguientes modos de lectura de archivos:

# .read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

# .readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.

# .readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.







#Resumen Mora 

'''
> Paso 1: pienso lo que quiero hacer en palaras, y lo escribo.

> Paso 2: importo lo que necesite:
	> <os> → si quiero mover/ejecutar cosas
		> permite:
			> <pwd> → Obtener directorio actual → getcwd()
			> <chdir(path)> → cambiar el directorio.
			> <mkdir(path[,modo])> → crear un directorio.

 	> <sys> → biblioteca que toma parámetros entre terminales

> Paso 3: abro el archivo.
	> with open(nombre del archivo, "modo") as miarchivo
		> Modos: <r>(read), <w>(write), <r+>(las dos), <a>(append)
		> miarchivo (o la palabra que elija) es para refererise al archivo que abro.
		> como uso with, no tengo que usar close, es como un cierre automatico.
	> ej: 
		>def es_un_ejemplo(archivo)
		with open(archivo, "modo") as miarchivo
			#en ese caso, el archivo que decido abrir es un parametro. Si lo pusiera entre comillas, le asginaria un archivo especifico con .txt

> Paso 4: definir que metodo voy a usar, en base a que quiero hacer.
	> <readlines()> lee las lineas del archivo y las devuelve como listas.
	> <readline()>  lee la primer linea del archivo.
		> al agregarle un numero, lee esa cantidad de caracteres, de la primera linea.
	> <read()> lee el contenido del archivo y lo devuelve como cadena de texto.
		>acepta un parámetro extra, ahi se puede especificar el nro de caracteres a leer.
		>Ej:
		with open("lista_compras.txt", r) as miarch
		print(archivo.read(5))
		#eso va a leer los primeros 5 caracteres del archivo.

> Algunas Funciones:
> > ><replace>("lo que quier reemplazar", "el reemplazo")
		>ej:
		with open ("ejemplo.txt", "r")
		lineas = archivo.readlines()
		for l in lineas:
			return (l.replace("\n", "|"))

> > > <split>("lo que quier separar")
	> ej:
	with open ("ejemplo.txt", "r")
	contenido= archivo.read()
	lineas = contenido.split("\n")
	print(lineas)
		#devuelve una cadena con el contenido, sin los enters

'''