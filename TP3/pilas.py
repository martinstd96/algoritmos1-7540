from constantes import *

class Pila:
	"""
	Modela una pila con operaciones de apilar, desapilar, ver si esta vacia,
	ver el tope de la misma y su representacion.
	"""
	def __init__(self):
		"""
		Crea una pila vacia.
		"""
		self.items=[]

	def esta_vacia(self):
		"""
		Devuelve un buleano indicando si la pila esta vacia o no.
		"""
		return len(self.items) == 0

	def apilar(self,elemento):
		"""Apila el elemento recibido"""
		self.items.append(elemento)

	def desapilar(self):
		"""
		Desapila el ultimo elemento que se apilo. En caso de que la pila este
		vacia levanta una excepcion.
		"""
		if self.esta_vacia():
			raise ValueError(ERROR_PILA_VACIA)
		return self.items.pop()

	def ver_tope(self):
		"""
		Muestra el ultimo elemento que se apilo. En caso de estar vacia
		levanta una excepcion.
		"""
		if self.esta_vacia():
			raise ValueError(ERROR_PILA_VACIA)
		return self.items[-1]

	def __str__(self):
		"""Devuelve una representacion de la pila.
		"""
		lista = []
		for c in self.items:
			lista.append(c)
		return str("".join(lista))
