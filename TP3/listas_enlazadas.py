from constantes import *

class Nodo:
	"""
	Modela un Nodo para la lista Enlazada con una operacion que permite
	representar al Nodo.
	"""
	def __init__(self,elemento):
		"""Crea un nodo. El elemento recibido es un caracter.
		"""
		self.elemento = elemento
		self.sig = None

	def __str__(self):
		"""
		Devuelve una representacion del nodo.
		"""
		return str(self.elemento)

class ListaEnlazada:
	"""
	Modela una ListaEnlazada con operaciones agregar, eliminar, insertar, iter y
	su representacion.
	"""
	def __init__(self):
		"""
		Crea un lista enlazada vacia.
		"""
		self.primero = None
		self.ultimo = None
		self.len = 0

	def append(self,elemento):
		"""
		Agrega un elemento al final de la lista.
		"""
		_nodo = Nodo(elemento)

		if self.len == 0:
			self.primero = self.ultimo = _nodo
			self.len += 1
			return
		self.len += 1
		self.ultimo.sig = _nodo
		self.ultimo = _nodo


    #no se si se usa
	def pop(self, indice = None):
		"""
		Elimina el ultimo elemento de la lista y lo devuelve.
		En caso de que la lista este vacia levanta una excepcion.
		"""
		if self.len == 0:
			raise IndexError(ERROR_LISTA_VACIA)
			return
		if indice is None:
			indice = self.len - 1
		if not (-1 < indice < self.len):
			raise IndexError(ERROR_FUERA_DE_RANGO)
			return
		self.len -= 1
		if indice == 0:
			elemento = self.primero.elemento
			self.primero = self.primero.sig
			return elemento
		previo = self.primero
		actual = self.primero.sig
		for i in range(1,indice):
			previo = actual
			actual = actual.sig
		previo.sig = actual.sig
		self.ultimo = previo
		return actual.elemento

	def insertar_al_principio(self,elemento):
		"""
		Inserta un elemento al principio de la lista.
		"""
		nodo = Nodo(elemento)
		nodo.sig = self.primero
		self.primero = nodo
		self.len += 1
		return

	def __iter__(self):
		"""
		Devuelve un iterador de la lista enlazada.
		"""
		return IteradorLista(self.primero)

	def __str__(self):
		"""
		Devuelve una representacion de la lista.
		"""
		lista = []
		for c in self:
			lista.append(str(c))
		return str("".join(lista))

class IteradorLista:
	"""
	Modela un iterador para la LISTAENLAZADA con una operacion next.
	"""
	def __init__(self,primero):
		"""
		Crea una referencia al primer elemento de la LISTAENLAZADA.
		"""
		self.actual = primero

	def next(self):
		"""
		Devuelve el proximo valor al actual.
		En caso de que no haya un elemento actual se lanza una excepcion.
		"""
		if not self.actual:
			raise StopIteration
		elemento = self.actual.elemento
		self.actual = self.actual.sig
		return elemento

	def __next__(self):
		"""
		Itera la LISTAENLAZADA y devuelve cada valor que se encuentre en la
		misma.
		"""
		return self.next()
