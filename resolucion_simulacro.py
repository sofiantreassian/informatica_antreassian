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







#parcialito guada 

# Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'.
# Por ejemplo para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].

import re

patron = "X(.*?ab.*?)Y" #signo de preg favorecer matches internos

patron_ok = "X([^X]*?ab[^Y].*?)Y"

def funcion1(string):
    print(re.findall(patron_ok, string))

funcion1("XbaaaYjXababYqXbabbbbaaYqXffeeY")

# . cualquier carac 
# * 0 o mas veces
# ? matches internos --> que mire adentro y no solo los bordes


# Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer
# la lista de substrings delimitadas por los patrones 'ag' y 'cta', no incluyan números.
# Revisá su código propuesto y marcá con una `x` las opciones correctas. JUSTIFICA tus respuestas.

import re

def funcionDeExpresiones_Regulares(string):
    print(re.findall("ag(\d.*?)cta", string))

funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta')


'''
  - El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python.
    NO, las convenciones dicen que las funciones tienen que estar en separadas por un _ en minus.
X - La función devuelve NameError al ser ejecutada. VERDADERO.
        Previo al codigo de de la funcion, hay que llamar a la biblioteca RE con un import re
  - La función devuelve SintaxError al ser ejecutada
  - Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['gaaa']
X - Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['24gra1nde']
    Falso, si se corrige la funcion agregando un print para que devuelva el resultado ['24gra1nde'].
# Findal --> Atribuite Error
'''

def entre_ag_y_cta_sin_numeros2(string):
    print(re.findall("ag([^\d]*)cta", string))

entre_ag_y_cta_sin_numeros2('aabocaggaaactazu4lggaasag24gra1ndecta')



# pacman


class PacMan:

    def __init__(self):
        self.puntos = 0
        self.vidas = 3               # Velocidad Puede ser opcional. Puede ser como metodo o atributo.
        
    def velocidad(self):                    #como metodo 
        return 2 + self.puntos / 100

    def comerBolita(self, cantidad):
        self.puntos = self.puntos + (cantidad * 2) 

    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER") 

    def comerFantasma(self, fantasma):
        if fantasma == "Rojo":
            self.puntos += 2
        elif fantasma == "Rosa":
            self.puntos += 8
        elif fantasma == "Naranja":
            self.puntos += 4
        elif fantasma == "Verde":
            self.puntos += 6

pacman = PacMan()

# pacman.comerBolita(22)
# pacman.perderVida()
# pacman.comerFantasma("Rojo")
# pacman.comerFantasma("Rosa")
# print(pacman.puntos)
# pacman.comerBolita(20)
# print(pacman.velocidad())
# pacman.perderVida()
# pacman.perderVida()

# 10
# 2.5
# GAME OVER

# B) Pac-Man nuevas habilidades:

# Ganar una vida extra si llega a 200 puntos, restando esta cantidad de puntos al puntaje
# Además ahora gana más velocidad a medida que suma puntos de la forma: velocidad = 3 + puntos / 100.
 
# Definí la clase PacManMejorado que herede de PacMan, pero que además entienda:
# vidaExtra(): comprobar si se cumple con la condición y aumentar en 1 la cantidad de vida
# y en caso contrario debe aparecer un cartel indicando cuántos puntos le faltan para conseguir una nueva vida.
# 
# También se tiene que redefinir el método velocidad() para que cumpla con lo indicado.

class PacManMejorado(PacMan):

    def vidaExtra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print ("Faltan", 200 - self.puntos, "puntos para ganar una vida extra") 
    
    def velocidad(self):                    #como metodo 
        return 3 + self.puntos / 100

pacmanMejorado = PacManMejorado()

# Ejecutando las siguientes líneas:

pacmanMejorado.comerBolita(22)
pacmanMejorado.perderVida()
pacmanMejorado.comerFantasma("Rojo")
pacmanMejorado.comerFantasma("Rosa")
print(pacmanMejorado.puntos)
pacmanMejorado.comerBolita(80)
print(pacmanMejorado.velocidad())
print(pacmanMejorado.vidas)
pacmanMejorado.comerBolita(30)
pacmanMejorado.vidaExtra()
print(pacmanMejorado.vidas)
pacmanMejorado.vidaExtra()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()


# El resultado de esto debería ser:	
# 10
# 4.7
# 2
# 3
# Faltan 170 puntos para ganar una vida extra
# GAME OVER




#-----------------------------------------------------------------------
#Pacman
class PacMan:
    def _init_(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional
    
    def comer_bolita(self, cantidad):
        self.puntos += (cantidad*2)
    
    def velocidad(self):
        return (2 + self.puntos)/100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("Game over")
    
    def comer_fantasma(self, fantasma, color):
        self.puntos += fantasma.puntos_color(color)
class Fantasma:
    def _init_(self):
        self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
    def puntos_color(self, color):
        return self.fantasmas[color]
    


pacman = PacMan()
fantasma = Fantasma()


class PacMan:
    def _init_(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional
    
    def comer_bolita(self, cantidad):
        self.puntos += (cantidad*2)
    
    def velocidad(self):
        return (2*self.puntos)/100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("Game over")
    
    def comer_fantasma(self, fantasma, color):
        fantasma.set_color(color)
        self.puntos += fantasma.puntos_color()

class Fantasma:
    def _init_(self):
        self.color = None

    def set_color(self, color):
        self.color =color
    
    def puntos_color(self):
        return self.color.puntos()
    

class Rojo:
    def puntos(self):
        return 2        

class Rosa:
    def puntos(self):
        return 4      

class Naranja:
    def puntos(self):
        return 6     

class Verde:
    def puntos(self):
        return 8     
    
pacman = PacMan()
rojo = Rojo()
rosa = Rosa()
naranja = Naranja()
verde = Verde()
fantasma = Fantasma()


#b) mejor forma de hacerlo

class PacManMejorado(PacMan):
    def vida_extra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")

    def velocidad(self):
        return 3 + self.puntos / 100
