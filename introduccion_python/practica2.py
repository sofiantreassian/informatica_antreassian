#Practica de introduccion a python parte 2

#ejercicio 1
def verificar_control(lista):
    if "control" in lista:
        indice = lista.index("control") 
        lista[indice] = "control revisado" 

#ejercicio 2
def eliminar_primer_elemento(lista):
    if len(lista) > 0:
        lista.pop(0)
        print("La lista está vacía")

#ejercicio 3 
def posicion_elemento(lista,elemento):
    posicion = -1
    for element in lista:
        posicion+=1
        if elemento == element:
            return 'posición: '+str(posicion)

#ejercicio 4
def eliminar_y_agregar(lista1,lista2,elemento):
        if elemento in lista1:
            lista2.append(elemento)
            del lista1[lista1.index(elemento)] 

def eliminar_y_agregar2(lista1,lista2,elemento):
    if elemento in lista1:
        lista1.remove(elemento)
        lista2.append(elemento)

#ejercicio 5
def par_impar(lista):
    for numero in lista:
        posicion = lista.index(numero)
        lista[posicion] = (numero%2 == 0)
    return lista

def par_impar2(lista):
    return [(num % 2 == 0) for num in lista]  

#ejercicio 6
def cant_por_caracter(string):
    caracteres ={}
    for caracter in string:
        if caracter in caracteres:
            caracteres[caracter] += 1
        else:
            caracteres[caracter] =1
    return caracteres

#ejercicio 7 

#ejercicio 8 
def palabra_palindroma(string):
    return string.lower() == string.lower()[::-1]

#ejercicio 9 
def productoria(lista):
    producto = 1
    for numero in lista:
        nuevo_prod = producto * numero
        producto = nuevo_prod
    return producto

#ejercicio 10
socios = {
    1: {"nombre": "Florencia", "apellido": "Ocampo", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    2: {"nombre": "David", "apellido": "Estévez", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    3: {"nombre": "Sofía", "apellido": "Cáceres", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    4: {"nombre": "Lionel", "apellido": "Messi", "fecha_ingreso": "21/10/2017", "cuota_al_dia": True}
}

# CANTIDAD DE SOCIOS
def cant_socios(diccionario):
    return len(diccionario)
# print(len(socios)) -- SABER CANTIDAD DE SOCIOS --

# REVISAR PAGO CUOTA
def revisar_pago(numero_socio):
    return socios[numero_socio]['cuota_al_dia']
# print(revisar_pago(3))

# CAMBIO FECHA
def cambio_fecha(fecha1, fecha2):
    for socio in socios:
        if socios[socio]['fecha_ingreso'] == fecha1:
            socios[socio]['fecha_ingreso'] = fecha2
# cambio_fecha('21/10/2017','22/10/2017')
# print(socios)

def dar_de_baja(nombre, apellido):
    for numero_socio, datos in socios.items(): # Ciclo for recorre dicc -socios- con método .items() retorna una lista de tuplas donde cada tupla contiene la clave y el valor correspondiente al elemento del diccionario.
        if datos["nombre"] == nombre and datos["apellido"] == apellido:
            del socios[numero_socio]
            break
    else:
        print("No se encontró al socio") #PARA CERRAR BUCLE FOR POR SI LOS DATOS FUERON MAL INGRESADOS O NO EXISTE EL SOCIO
# dar_de_baja('Florencia','Ocampo')
# print(socios)