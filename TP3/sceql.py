from constantes import *
from objetos import *
import os, sys

def main():
    """
    Funcion principal del programa. Se encarga de cargar los datos en la maquina.
    """
    try:
        cargar_datos()
    except FileNotFoundError:
        print(ERROR_NO_ENCUENTRA_ARCHIVO)
        sys.exit(0)
    except IndexError:
        print(ERROR_NO_INGRESO_ARCHIVO)
        sys.exit(0)
    except ValueError:
        print(ERROR_ARCHIVO_NO_SCEQL)
        sys.exit(0)

def cargar_datos():
    """
    Carga los datos de un archivo sceql en la maquina.
    """
    _archivo=sys.argv[1]
    if not es_archivo_sceql(_archivo):
        raise ValueError
    cinta=Cinta()
    with open(_archivo) as archivo:
        for linea in archivo:
            for caracter in linea:
                if caracter in TUPLA_CARACTERES_SCEQL:
                    cinta.cargar(caracter)
    if len(sys.argv)==3 and sys.argv[2]== DEBUG: #cambie
        maquina=Maquina(cinta,True)
    else:
        maquina=Maquina(cinta)
    while not maquina.cinta.esta_vacia():
        maquina.procesar()

def es_archivo_sceql(archivo):
    """
    Valida si el archivo recibido es un archivo valido para el interprete.
    Devuelve True si lo es o False si no lo es.
    """
    extension_archivo =archivo.split(".")[-1]

    return extension_archivo == EXTENSION_SCEQL

main()
