# Practica objetos parte 1 

# Ejercicio 1: Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
    
#interfaz: energia, comer, acariciar, debil 
#estado: alimento y caricias 

#Ejercicio 2: Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

#Ejercicio 3: Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self):
        self.marca = 0
        self.modelo = 0
        self.precio = 0

    def descuento_al_precio(self, porcentaje):
        return self.precio -= porcentaje 

class Descuentos (Notebook):


#Ejercicio 4: Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
# inc() dis() reset() valorActual() valorNuevo(nuevoValor)

 class Modelo: 
    def __init__(self):
        self.contador = 0 



#Practica objetos parte 2 

#Ejercicio 1: Dadas las siguientes clases responder: cuales son sus estados, cuales son sus interfaces, ¿Comparten interfaz?, ¿Son polimórficas?

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
       print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
       self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
       print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4
    

#estados: alimento y caricias 
#interfaces: energia, comer, acariciar, debil, pasear
#comparten interfaz porque entienden los mismos mensajes 
#son polimorficos porque comparten interfaz 

#Ejercicio 4
#Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

#comienzan con una cantidad que podemos establecer de combustible
#los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido
#las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
#pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible
#saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

#Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

class MedioDeTransporte:
  def __init__(self, combustible):
    self.combustible = combustible
    
  def cargar_combustible(self, cantidad):
    self.combustible += cantidad
  
  def entran_personas(self, cantidad):
    return cantidad <= self.maximo_personas()

class Moto (MedioDeTransporte):
  def maximo_personas(self):
    return 2 
  def recorrer(self,kilometros):
    self.combustible -= kilometros
    
class Auto (MedioDeTransporte):
  def maximo_personas(self):
    return 5 
  def recorrer(self,kilometros):
    self.combustible -= kilometros / 2


#Practica modelos 

#1 

#En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes. Además instanciá a un Titan y ejecutá las siguientes líneas:

#DATOS:
    #salud = 100 de máxima
    #si llega a 0 = muere
    #al recibir este ataque la salud disminuye 1.5 por cada punto de daño recibido
    #pueden destruir casas: 
        # 8 casas cuando su salud es máxima
        # salud < maxima, destruye 4.8 casas


class Titan:
    def _init_(self, salud_actual):
        self.salud = salud_actual
        salud_actual = 100
        self.max_salud = 100
    
    def esta_vivo(self):
        return self.salud > 0
    
    def recibir_ataque(self, cantidad_ataques):
        self.salud -= cantidad_ataques * 1.5
    
    def salud_actual(self):
        return self.salud
    
    def grito(self):
        return "arghhh"
    
    def cuantas_casas(self):
        return self.salud * 8 /self.max_salud
    
    def destruir(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1) > 0):
                self.salud -= (self.cuantas_casas() // 1) * 12.5
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5
        else:
            print("No puede destruir ninguna casa")


titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.destruir())
print(titan1.grito())
titan1.destruir()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())


#2
#Nave espacial Enterprise 
#nivel de potencia 0 a 100
#nivel de coraza 0 a 20
#Nave puede:
    # encontrarse con una pila atómica = potencia aumenta en 25.
    #encontrarse con un escudo = nivel de coraza aumenta en 10.
    #recibir un ataque --> se especifican los puntos de fuerza del ataque recibido. 
    #La Enterprise "detiene" el ataque con la coraza
        #si la coraza no alcanza, el resto se descuenta de la potencia. 
# Enterprise nace con 50 de potencia y 5 de coraza

class Enterprise:
    def _init_(self):
        self.nivel_potencia=50
        self.nivel_coraza=5
        self.max_potencia=100
        self.min=0
        self.max_coraza=20
    
    def potencia(self):
        return self.nivel_potencia> self.min and self.nivel_potencia < self.max_potencia

    def coraza(self):
        return self.nivel_coraza > self.min and self.nivel_coraza < self.max_coraza
    
    def encontrarPilaAtomica(self):
        if self.nivel_potencia+25<=100:
            self.nivel_potencia+=25
        else:
            self.nivel_potencia=100
    
    def encontrarEscudo(self):
        if self.nivel_coraza+10<=self.max_coraza:
            self.nivel_coraza+=10
        else:
            self.nivel_coraza=self.max_coraza

    def recibirAtaque(self, puntos):
        if puntos <= self.nivel_coraza:
            self.nivel_coraza-=puntos
        else: self.nivel_potencia -= puntos - self.nivel_coraza
        self.nivel_coraza = self.min
    
    def fortalezaDefensiva(self):
        self.nivel_coraza + self.nivel_potencia
    
    def necesitaFortalecerse(self):
        return self.nivel_coraza==0 and self.nivel_potencia <=20
    
    def fortalezaOfensiva(self):
        if self.nivel_potencia < 20:
            return 0
        else:
            return (self.nivel_potencia - 20)/2


enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.nivel_potencia)
print(enterprise.nivel_coraza)


#3


class Persona:
    def _init_(self, la_energia):
        self.energia = la_energia
        self.feliz = False

    def energia_actual(self):
        return self.energia
    
    def dormir (self, horas):
        if self.energia + horas <= 100:
            self.energia += horas * 12.5
        else:
            self.energia = 100
    
    def comer(self):
        if self.energia + 10 <=100:
            self.energia += 10
        else:
            self.energia = 100
    
    def hacer_ejercicio(self, minutos):
        if (self.energia - minutos * (25/30)) >= 0:
            self.energia -=minutos * (25/30)
        else:
            self.energia=0
    

class Estudiante(Persona):
    def estudiar(self, horas):
        if (self.energia - 20 * horas) >= 0:
            self.energia -= 20 * horas
        else:
            self.energia=0
    
    def aprobar(self):
        return not self.feliz 

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())

class Persona:
    def _init_(self, la_energia):
        self.energia = la_energia
        self.feliz = False

    def energia_actual(self):
        return self.energia
    
    def dormir (self, horas):
        if self.energia + horas <= 100:
            self.energia += horas * 12.5
        else:
            self.energia = 100
    
    def comer(self):
        if self.energia + 10 <=100:
            self.energia += 10
        else:
            self.energia = 100
    
    def hacer_ejercicio(self, minutos):
        if (self.energia - minutos * (25/30)) >= 0:
            self.energia -=minutos * (25/30)
        else:
            self.energia=0
    

class Estudiante(Persona):
    def estudiar(self, horas):
        if (self.energia - 20 * horas) >= 0:
            self.energia -= 20 * horas
        else:
            self.energia=0
    
    def aprobar(self):
        return not self.feliz 

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())