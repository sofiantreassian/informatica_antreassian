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

#ejercicio 11
def empieza_con_h(palabra):
    if str.startswith(palabra, "H"):
        return len(palabra)
    
#tambien se puede usar palabra.startswith("H") o str.startswith (palabra, "H")
    
#ejercicio 12
def buenos_buenas(palabra):
     return str.startswith(palabra, "Buenos") or str.startswith (palabra, "Buenas")