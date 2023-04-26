#Practica de introduccion a python parte 1 

#ejercicio 1 
def anterior_y_posterior(numero):
    return numero - 1, numero + 1 

print (anterior_y_posterior(5))

#ejercicio 2
def doble(numero):
    return numero * 2

#ejercicio 3 
def doble_anterior (numero):
    return (numero -1) * 2, (numero +1) *2

#ejercicio 4
def retirar_dinero(saldo, monto):
    return max(saldo-monto,0)
    
#ejercicio 5 
def dia_de_la_semana_favorito(dia):
    return dia == "Sábado"

#ejercicio 6 
def longitud_onda(onda):
    return 223<=onda<=586.8

#ejercicio 7 
def longitud_onda(onda):
    return 223<=onda<=586.8 and onda != 314.5

#ejercicio 8 
def tiene_descuento(edad):
    return 12>=edad or edad>=60

#ejercicio 9
def xor (booleano1, booleano2):
    return booleano1 != booleano2

#ejercicio 10
def saludo (nombre, apellido):
    return "Hola " + nombre + ", como estas " + apellido + "?"

#ejercicio 11
def empieza_con_h(palabra):
    if str.startswith(palabra, "H"):
        return len(palabra)
    
#tambien se puede usar palabra.startswith("H") o str.startswith (palabra, "H")
    
#ejercicio 12
def buenos_buenas(palabra):
     return str.startswith(palabra, "Buenos") or str.startswith (palabra, "Buenas")

#ejercicio 13 
def es_multiplo (num1, num2):
    return num2 % num1 == 0

#ejercicio 14
def par_impar_cero (num):
    if num % 2 == 0 and num != 0:
        return "es par"
    elif num % 2 != 0:
        return "es impar"
    else:
        return "es cero"

#ejercicio 15
def a_en_frase (frase):
    ases = 0
    for letra in frase:
        if letra == "a" or letra == "A":
            ases += 1
    return ases

#ejercicio 16
def cuantos_meses_me_quedan_de_vida (dinero):
    return dinero / 60000
