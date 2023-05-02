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
        return precio -= porcentaje 

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