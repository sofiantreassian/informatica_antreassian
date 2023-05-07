#algunos ejercicios de mumuki

#otro
class Celular:
  def __init__(self, una_bateria, un_saldo, el_sistema_operativo):
    self.bateria = una_bateria
    self.saldo = un_saldo
    self.sistema_operativo = el_sistema_operativo

  def tiene_bateria_maxima(self):
    return self.bateria == 100
  
  def cargar_a_tope(self):
    self.bateria = 100
    
  def necesita_saldo(self): 
    return self.saldo <= 0
  
  def cargar_saldo(self, un_saldo):
    self.saldo += un_saldo


#otro

class Caballo:
  def __init__(self,una_energia, una_raza):
   self.energia = una_energia
   self.raza = una_raza

  def comer(self, gramos):
    self.energia += gramos * 2

  def galopar(self,kms):
   self.energia -= kms


#otro

class Golondrina:
  def __init__(self,una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self, cantidad_gramos):
    self.energia += cantidad_gramos / 2

  def volar_hacia(self, ciudad_destino):
    self.ciudad = ciudad_destino
    self.energia /= 2

#otro

class Gato:
  def __init__(self, una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad
    
  def comer(self, gramos):
    self.energia += gramos
  
  def cumplir_anios(self):
    self.edad += 1

#otro

class EstudianteDeVeterinaria:
  def alimentar(self, animal, gramos):
    animal.comer(gramos)
 
  def rehabilitar (self,animal):
    animal.recibir_rehabilitacion()
  
  def puede_dar_el_alta(self, animal):
    return animal.esta_feliz()           

class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
    
  def recibir_rehabilitacion(self):
    self.comer(400)
    
  def esta_feliz(self):
    return self.energia > 30    

class Caballo:
  def __init__(self,una_energia, una_raza):
    self.energia = una_energia
    self.raza = una_raza

  def comer(self,gramos):
    self.energia += gramos * 2

  def galopar(self,kms):
    self.energia -= kms

  def recibir_rehabilitacion(self):
    self.galopar(3)
    self.comer(3000)
    self.galopar(5)
    
  def esta_feliz(self):
    return True 
  
class Golondrina:
  def __init__(self,una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self,gramos):
    self.energia += gramos / 2

  def volar_hacia(self,destino):
    self.ciudad = destino
    self.energia /=  2 
  
  def recibir_rehabilitacion(self):
    self.volar_hacia("Lihuel Calel")
    
  def esta_feliz(self):
    return self.ciudad == "Lihuel Calel"
  
#otro

class Zombi:
  def __init__(self, hambre):
    self.hambre = hambre
    
  def sabe_correr(self):
    return "¡Corre, zombi, corre!"
  
  def recibir_danio(self, danio):
    self.hambre -= danio * 2
    
  def es_un_peligro(self):
    return self.hambre > 50
 
class SuperZombi:
  def __init__(self, hambre):
    self.hambre = hambre
    
  def sabe_correr(self):
    return "¡Corre, superzombi, corre!"
  
  def recibir_danio(self, danio):
    self.hambre -= danio 
    
  def regenerarse(self):
    self.hambre = 100
    
  def es_un_peligro(self):
    return True
  
#otro

class Sobreviviente:
    def _init_(self, adrenalina):
        self.adrenalina = adrenalina

    def atacar(self, contrincante):
        if not contrincante.es_un_peligro():
            danio = self.adrenalina/2
            contrincante.recibir_danio(danio)
            self.adrenalina += 20
            return "¡Ataque exitoso! Contrincante recibió " + str(danio) + " de daño."
        else:
            raise Exception("Es peligroso atacar a este zombi")
        
#otro

class PlantaCarnivoraZombi:
  def __init__(self, clorofila):
    self.clorofila = clorofila
    
  def es_un_peligro(self ):
    return self.clorofila > 40
  
  def hacer_fotosintesis(self, minutos):
    self.clorofila += minutos
  
  def recibir_danio(self, danio, *args):
    self.clorofila -= 10

#otro

class Pasta:
    def _init_(self):
        self.ajies = 0
        
    def suavizar(self):
      self.ajies -=1

class Pizza:
    def _init_(self):
        self.condimento = "adobo"
        
    def suavizar (self):
      self.condimento = "oregano"
      
class Chef:
    def _init_(self, plato_del_dia):
        self.plato_del_dia = plato_del_dia
    
    def picantear(self):
        if isinstance(self.plato_del_dia, Pasta):
            if self.plato_del_dia.ajies > 10:
                raise Exception("El plato ya está demasiado picante")
            else:
                self.plato_del_dia.ajies += 5
        elif isinstance(self.plato_del_dia, Pizza):
            if self.plato_del_dia.condimento == "cayena":
                raise Exception("El plato ya está demasiado picante")
            else:
                self.plato_del_dia.condimento = "cayena"
        else:
            raise Exception("El chef solo puede picantear pastas o pizzas")

class AyudanteDeCocina:
    def suavizar(self, plato):
       plato.suavizar()

#otro

class Dispositivo:
  def __init__(self, bateria):
    self.bateria = bateria
  def tiene_bateria(self):
    return self.bateria > 20
  
  def tiene_bateria_maxima(self):
    return self.bateria == 100
  
  def sin_carga(self):
    return not self.tiene_bateria()
  
  def cargar_a_tope(self):
   self.bateria = 100
  
class Tablet(Dispositivo):
  def utilizar(self,minutos):
    self.bateria -= minutos / 2
    
class Notebook(Dispositivo):
  def utilizar(self, minutos):
    self.bateria -= minutos

#otro

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

#
class Colectivo (MedioDeTransporte):  
  def __init__(self):
    super().__init__(100)
    self.pasajeros = 0
    
  def entran_personas(self, pasajeros):
    return self
  
  def cargar_combustible(self, cantidad_combustible):
    super().cargar_combustible(cantidad_combustible)
    self.pasajeros = 0


#otro

class Zombi:
  def __init__(self, un_hambre):
    self.hambre = un_hambre

  def sabe_correr(self):
    return True

  def es_un_peligro(self):
    return self.hambre > 50

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio * 2
    
  def descansar(self, cantidad):
    self.hambre += cantidad

class SuperZombi (Zombi):
  def es_un_peligro(self):
    return True

  def recibir_danio(self,puntos_de_danio):
    self.hambre -= puntos_de_danio

  def regenerarse(self):
    self.hambre = 100



#otro 

class Biblioteca:
  def __init__(self):
    self.libros = []
    
  def agregar_libro(self, libro):
    if libro not in self.libros:
      self.libros.append(libro)
    
  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  
  def titulos_disponibles(self):
    return [libro.titulo for libro in self.libros]
    
class Libro (Biblioteca):
  def __init__(self, titulo, cantidad_de_paginas, genero, autoria):
    self.titulo = titulo
    self.genero = genero
    self.paginas = cantidad_de_paginas
    self.autoria = autoria
    
  def es_largo(self):
    return self.paginas > 300  
  
  def nacionalidad(self):
    return self.autoria["nacionalidad"]
  

#otro 

contacto = Libro("Contacto", 400, "Ciencia ficción", {"nombre": "Carl", "apellido": "Sagan", "nacionalidad": "Estados Unidos"})
socorro = Libro("Socorro", 250, "Terror", {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina"})


biblioteca_de_emma = Biblioteca()
biblioteca_de_emma.agregar_libro(contacto)
biblioteca_de_emma.agregar_libro(socorro)

#otro (el mismo de antes pero con set)

class Biblioteca:
  def __init__(self):
    self.libros = set()
    
  def agregar_libro(self, libro):
    self.libros.add(libro)
    
  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  
  def titulos_disponibles(self):
    return [libro.titulo for libro in self.libros]
    
class Libro (Biblioteca):
  def __init__(self, titulo, cantidad_de_paginas, genero, autoria):
    self.titulo = titulo
    self.genero = genero
    self.paginas = cantidad_de_paginas
    self.autoria = autoria
    
  def es_largo(self):
    return self.paginas > 300  
  
  def nacionalidad(self):
    return self.autoria["nacionalidad"]
  

#otro 

class Persona:
  def __init__(self, un_nombre, un_segundo_nombre, un_apellido):
    self.nombre = un_nombre
    self.segundo_nombre = un_segundo_nombre
    self.apellido = un_apellido
  
  def iniciales(self): #este metodo devuelve una tupla 
    return (self.nombre[0], self.segundo_nombre[0], self.apellido[0])
  

#otro 

class Juguete:
  def __init__(self, nombre, precio_minorista, precio_mayorista, partes):
    self.nombre = nombre
    self.precio_minorista = precio_minorista
    self.precio_mayorista = precio_mayorista
    self.partes = partes
  
  def es_barato(self):
    return self.precio_minorista < 1000 and self.precio_mayorista < 600
  
  def precios_con_iva(self): #esto retorna una tupla 
    return self.precio_minorista * 1.21, self.precio_mayorista * 1.21
  
  def es_electronico(self):
    return "bateria" in self.partes


#otro 

class Jugueteria:
  def __init__(self):
    self.productos = []
    
  def adquirir_producto(self, producto):
    return self.productos.append(producto)
  
  def catalogo_de_oferta(self):
    return [Juguete.nombre for Juguete in self.productos if Juguete.es_barato()]