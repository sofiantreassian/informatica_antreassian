#Resumen expresiones regulares

#siempre importar re 

# 1. Lo esencial es invisible a los ojos
#hay caracteres especiales, representados por secuencias de escape
#Las secuencias de escape son una combinación de caracteres que tiene un significado distinto de los caracteres literales contenidos en ella y se utilizan para definir ciertos caracteres especiales dentro de cadenas de texto, tipicamente aquellos que dan formato al mismo. Y aún cuando son un conjunto de caracteres, una secuencia de escape se considerada un carácter único.
#Estas combinaciones constan tipicamente de una barra invertida (\) seguida de una letra o de una combinación de dígitos, que tendrá un significado distinto según cuales sean.

#Ejemplos:
# \n:salto de línea
# \t:Tab o cambio de pestaña
# \s:espacio
# ':Comillas simples
# ":Comillas dobles

# 2. Que son las expresiones regulares
#son cadenas de caracteres basadas en reglas sintácticas, que permiten describir secuencias de caracteres. Es decir es un criterio para buscar, capturar o reemplazar texto utilizando patrones. Estas son una herramienta poderosa a la hora de hacer búsquedas sofisticadas en Strings de forma simple.
#Las expresiones regulares se pueden concatenar para formar nuevas expresiones regulares; si, por ejemplo, A y B son expresiones regulares, AB también es una expresión regular.

# 3. Metacaracteres
#son caracteres especiales que, dependiendo del contexto, tienen un significado especial para las expresiones regulares.

#metacaracteres delimitadores:nos permitirán delimitar dónde queremos buscar los patrones de búsqueda.

#Ejemplos:
# ^: Inicio de línea
# $: Fin de linea
# \A: Inicio de texto
# \Z: Fin de texto
# .: Coincide con cualquier caracter en una línea dada

#metacaracteres cuantificadores: permite repitir cierta cantidad de veces una busqueda dada.

#Ejemplos:
# *: Cero o más: todas las ocurrencias de un dado substring
# +: Una o más ocurrencias del patrón
# ?: Cero o una (si esta combinado con un metacaracter significa favorecer matches internos)
# {n}: Exactamente n veces
# {n,m}: Por lo menos n pero no más de m veces. mínimo número de ocurrencias en n y el máximo en m.

#metacaracteres predefinidos: facilitan el uso de las expresiones regulares

#Ejemplos:
# \w: Caracter alfanumércio
# \W: Caracter NO alfanumércio
# \d: Caracter numércio
# \D: Caracter NO numércio
# \s: Un espacio, de cualquier tipo (\t\n\r\f)
# \S: Cualquier caracter que no sea un espacio

#Así como podemos listar los caracteres posibles en cierta posición de la cadena, también podemos listar caracteres que no deben aparecer utilizando el ^. Así, por ejemplo rango [^a-d] coincide con cualquier caracter que no sea abcd.

#4. Expresiones regulares en Python
#libreria re: pip install re 
#antes: import re 

#5. Coincidencias o matches

#si un String se corresponde con el criterio que define una expresión regular, se dice que el String hace match con la expresión, y equivalentemente, se dice que la expresión acepta al String.
#Podemos encontrar patrones en un texto con el función search
#El función match() de re busca el patrón y devuelve la primera aparición y solo al principio de la cadena. Si se encuentra una coincidencia en la primera línea, devuelve el objeto de coincidencia. Pero, si se encuentra una coincidencia en alguna otra línea, devulve un valor nulo.
#el método group() sirve para mostrar el resultado de una búsqueda
#El método group() (o group(0)) nos devuelve la coincidencia. Sin embargo si lo que se quiere no es encontrar un patrón en particular, sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas palabras) hay que modificar el patrón.
#cuando se quieren obtener todas las apariciones del patrón se utiliza el método findall el cual actúa para cada coincidencia como si devolviera el group(1), es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores.

#6. Reemplazos o sustituciones masivas
#La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.