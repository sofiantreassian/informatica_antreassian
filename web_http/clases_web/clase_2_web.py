# clase 2 web 22/05

import requests

respuesta =requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

#1 describir las partes de la url

#todas las urls empiezan con htts://    es el protocolo
#para q una api sea res tiene q la url mapear recursos 

# url es htts://       /recursos) # estos recursos son las cosas que puedo consultar en la base de datos 

#la parte del medio que no definimos se llama el dominio de la url. es el nombre con el cual voy a mapear ip particular 


#2 que rta obtenes al hacer un get a esa url? 
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print (respuesta.json()) # devuelve un monton de datos tipo diccionario 

contenido_respuesta = respuesta.json()
print(contenido_respuesta.keys())

#rta: me da por rta todos los contenidos asociados al recurso ditto con los detalles de habilidades, experiencia, forma, etc 

#3 cual es el content type de esa rta 
print(respuesta.headers["Content-Type"])

#json; charset=utf-

#htts solo permite texto 

#4 cual es el status code de la rta 
print(respuesta.status_code)

#devuelve 200. eso significa que esta todo ok 

#5 cuantas habilidades tiene este pokemon (ditto)
print(f'Tiene{len(contenido_respuesta["abilities"])} habilidades')

#Tiene 2 habilidades



#clase 3 de web falte 