from listas_enlazadas import *

class Cola:
	"""
	Modela una cola con operaciones insertar el primero, encolar, desencolar,
	ver el primero, ver si esta vacia y su representacion.
	"""
	def __init__(self):
		"""
		Crea una cola vacia.
		"""
		self.items = ListaEnlazada()

	def insertar_primero(self,elemento):
		"""
		Es una implementacion que se creo que Inserta un elemento al principio de la cola.(no es una primitiva)
		"""
		self.items.insertar_al_principio(elemento)

	def encolar(self,elemento):
		"""
		Encola un elemento a la cola.
		"""
		self.items.append(elemento)

	def desencolar(self):
		"""
		Desencola el primer elemento que se encuantra en la cola y lo
		devuelve.
		"""
		return self.items.pop(0)

	def ver_primero(self):
		"""
		Devuleve el primer elemento de la cola.
		"""
		if self.esta_vacia():
			raise ValueError(ERROR_COLA_VACIA)
		
		return self.items.primero.elemento

	def esta_vacia(self):
		"""
		Devuleve un buleano indicando si la cola esta vacia o no.
		"""
		return self.items.len == 0

	def __str__(self):
		"""
		Devuelve una representacion de la cola.
		"""
		return str(self.items)
