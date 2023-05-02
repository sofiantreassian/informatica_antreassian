# ejercicio 1 (expresiones regulares )


#a.

# nos pide lista, entonces se que tengo que usar findall
# .* cualquier caracter que este antes o despues de ab

import re 
def entre_X_Y_con_ab(string):
    patron = "X([^XY]*ab[^XY]*)Y"                    #"X(.*?ab.*?)Y"
    return re.findall (patron, string)

print(entre_X_Y_con_ab("XabababababYXjskjdkkY"))

#b.

# 1. faltan guiones bajos y todo en minuscula. debe estar todo en minuscula separado por guiones. tambien el nombre debe ser mas expresivo. tamb falta el parametro
# 2. y 3. el error es un atribute error, porque findall esta mal escrito, falta una l. si se corrige eso, lanza type error
# 4. y 5. el 5 no debe devolverlo porque incluye numeros. luego de corregir la funcion debe devolver el 4

#funcion corregida:

def entre_ag_cta_sin_numeros(string):
    return re.findall ("ag([^\d]*)cta", string)

print(entre_ag_cta_sin_numeros("agjojojojocta"))

# ejercicio 2 

import glob, re, os
def filtrar (archivo):
    lista_txt = glob.glob("*.txt")

    with open (archivo, "a") as arch:
        for archivo in lista_txt:
            with open (archivo, "r") as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall ("[\w] + [-_\.]* [\w] + @gmail.com", texto)
                for email in lista:
                    arch.write (email + "\n")


#ejercicio 4 

#cambio de consigna: 
#come bolitas, gana doble cantidad de punto
#come fantasma, rosa 8, verde 6, naranja 4 y rojo 2
#velocidad depende de los puntos con esta formula: 2*puntos sobre 100
#perder vida= contador -1, reseteo puntos. si pierde las 3 vidas, game over 


class PacMan:
    def __init__(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional 

    def comer_bolitas(self, cantidad):
        self.puntos += (cantidad *2)

    def velocidad(self):
        return 2 + self.puntos / 100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print ("GAME OVER")

#esta es una opcion, no esta mal pero tampoco es la mejor. habria que usar delegar. cuanto menos ifs tiene una funcion, mejor
    def comer_fantasma(self, fantasma):
        if fantasma == "rosa":
            self.puntos += 8
        elif fantasma == "verde":
            self.puntos += 6
        elif fantasma == "naranja":
            self.puntos += 4
        elif fantasma == "rojo":
            self.puntos += 2

pacman = PacMan()
