from constantes import *
from pilas import *
from colas import *
import os
import platform

def limpiar_pantalla():
    """
    Borra pantalla.
    """
    os.system(CLS if platform.system() == WIN else CLEAR)

class Cinta:
    """
    Modela una cinta que trasporta elementos con la operaciones cargar, ver
    el actual, avanzar, retroceder, ver si esta vacia y su representacion.
    """
    def __init__(self):
        """
        Crea una cinta vacia.
        """
        self.items = Cola()
        self.contenedor = Pila()

    def cargar(self,elemento):
        """
        Inserta un elemento a la cola. El elemento recibido es un caracter.
        """
        self.items.encolar(elemento)

    def actual(self):
        """
        Devuelve al elemento que se encuentre al frente de la cinta.
        """
        return self.items.ver_primero()

    def avanzar(self):
        """
        Avanza a la siguiente posicion de la cinta.
        En el caso de que la cinta este vacia levanta una excepcion.
        """
        if self.items.esta_vacia():
            raise ValueError(ERROR_COLA_VACIA)
        self.contenedor.apilar(self.items.desencolar())

    def retroceder(self):
        """
        Retrocede a la anterior posicion de la cinta.
        """
        self.items.insertar_primero(self.contenedor.desapilar())

    def esta_vacia(self):
        """
        Chequea si la cinta esta vacia, devolviendo True en caso verdadero
        o False en caso contrario.
        """
        return self.items.esta_vacia()

    def __str__(self):
        """
        Muestra una representacion de la cinta.
        """
        return str(self.items)

class Maquina:
    """
    Modela una maquina que procesa la informacion de la cinta con las
    operaciones procesar, avanzar, retroceder, mostrar, tipo de operacion a
    ejecutar, sumar uno, restar uno, desencolar mostrar dato y encolar, encolar
    un cero, desncolar encolar, saltar hata la barra opuesta y evaluar si hace
    un salto o no hasta la barra opuesta.
    """
    def __init__(self,cinta,debug=False):
        """Crea una maquina vacia.
        Recibe una Objeto cinta cargada previamente y se asume que la cinta esta
        cargada y contiene caracteres validos para procesar.
        """
        self.cola = [0]
        self.cinta = cinta
        self.pantalla = Cola()
        self.debug = debug

    def procesar(self):
        """
        Procesa la informacion de la cinta.
        """
        caracter = self.cinta.actual()
        self._operacion(caracter)()

    def _avanzar_cinta(self):
        """
        Avanza la cinta para adelante.
        """
        self.cinta.avanzar()

    def _retroceder_cinta(self):
        """
        Retrocede la cinta.
        """
        self.cinta.retroceder()

    def _mostrar(self):
        """
        Muestra en pantalla el funcionamiento de la maquina.
        """
        if self.debug == True:
            limpiar_pantalla()
            print("{}{}  {}{}".format(MENSAJE_COLA,self.cola,MENSAJE_PANTALLA,self.pantalla))
            print()
            print("{:.100}".format(str(self.cinta)))
            print("^")
            input(MENSAJE_AL_USUARIO)
            return
        if self.cinta.actual() == DESENCOLAR_IMPRIMIR_ENCOLAR:
            elemento = self.cola.pop()
            print(chr(elemento),end="")
            self.cola.append(elemento)

    def _operacion(self,dato):
        """
        Evalua el tipo de dato, devolviendo la funcion correspondiente a
        ejecutar.
         """
        funciones = { SUMAR_1 : self._sumar_1,

                      RESTAR_1 : self._restar_1,

                      DESENCOLAR_IMPRIMIR_ENCOLAR : self._descolar_mostrarDato_encolar,

                      ENCOLAR_0 : self._encolar_0,

                      DESENCOLAR_ENCOLAR : self._desecontar_encolar,

                      FIN : self._salta_hasta_la_barra_inicio,

                      INICIO : self._saltar_hasta_la_barra_fin_o_posterior }

        return funciones.get(dato,self._nada)

    def _nada(self):
        self._mostrar()
        self._avanzar_cinta()

    def _sumar_1(self):
        """
        Suma un bite a la cola del frente sin moverlo de lugar.
        En caso de que el byte sobrepase 255 vuelve a 0.
        """
        valor = self.cola[0] + 1
        self.cola[0] = valor % COTA_MAYOR
        #muestra para debug
        self._mostrar()
        self._avanzar_cinta()

    def _restar_1(self):
        """
        Resta un bite a la cola del frente sin moverlo.
        En caso de que el byte sea inferior a 0 vuelve a 255.
        """
        valor = self.cola[0] - 1
        self.cola[0] = valor if valor >= COTA_MENOR else COTA_MAYOR - 1
        #muestra para debug
        self._mostrar()
        self._avanzar_cinta()

    def _descolar_mostrarDato_encolar(self):
        """
        Desencola un byte, lo imprime en patalla y lo vuelve a encolar.
        """
        valor = self.cola.pop(0)
        self.cola.append(valor)
        self.pantalla.encolar(chr(valor))
        #muestra para debug
        self._mostrar()
        self._avanzar_cinta()

    def _encolar_0(self):
        """
        Encola un 0 en la cola.
        """
        self.cola.append(0)
        #muestra para debug
        self._mostrar()
        self._avanzar_cinta()

    def _desecontar_encolar(self):
        """
        Desencola el byte y lo vuelve a encolar en la cola.
        """
        self.cola.append(self.cola.pop(0))
        #muesta para debug
        self._mostrar()
        self._avanzar_cinta()

    def _salta_hasta_la_barra_inicio(self):
        """
        vuelve hasta la barra opuesta \ .
        """
        repeticion = 0
        self._mostrar()
        while True:
            self._retroceder_cinta()
            elemento = self.cinta.actual()
            if elemento == FIN:
                repeticion +=1
                continue
            if elemento == INICIO:
                if repeticion != 0:
                    repeticion -= 1
                    continue
                break
        #muestra para debug
        self._mostrar()

    def _saltar_hasta_la_barra_fin_o_posterior(self):
        """
        Evalua si el byte del frente es 0. Si ocurre eso salta hasta la
        siguiente posicion despues de / correspondiente. En caso contrario omite.
        """
        repeticion = 0
        if self.cola[0] == 0:
            while True:
                self._avanzar_cinta()
                elemento = self.cinta.actual()
                if elemento == INICIO:
                    repeticion += 1
                    continue
                if elemento == FIN:
                    if repeticion != 0:
                        repeticion -= 1
                        continue
                    self._avanzar_cinta()
                    #muestra para debug
                    if not self.cinta.esta_vacia():
                        self._mostrar()
                    return
        self._avanzar_cinta()
