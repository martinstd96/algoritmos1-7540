import os, re, sys
from collections import OrderedDict as sin_repetir_elementos

def main():
    """
    Funcion principal del programa. Muestra la cantidad de archivos que se han
    indexado como tambien que debe se ingresar para salir del mismo.
    """
    indexador={}
    print()
    print("Ingrse * para salir del programa")
    print()
    print("Indexando archivos...")
    print(obtener_archivos_indexados(indexador))
    while True:
        consola(indexador)

#-------------------------------------------------------------------------------

def obtener_puntero():
    """
    Funcion que devuelve una representacion del puntero del programa el cual
    se le muesta al usario para que ingrese terminos de busqueda.
    """
    puntero=input("> ")
    while len(puntero)==0:
        print()
        puntero=input("> ")
    return puntero

def consola(indexador):
    """
    Funcion que se encarga de la interaccion con los datos que recibe el
    programa y sus modos de busqueda.
    Recibe indexador que es el diccionario donde estan almacenados los terminos
    de busqueda como claves y como valor asociado una lista con las rutas en
    donde aparecen los terminos.
    En caso de que se ingrese un '*' se corta la ejecucion del programa.
    """
    print()
    NOT="NOT:"
    AND="AND:"
    OR="OR:"
    puntero=obtener_puntero()
    lista_terminos=puntero.split()
    modo_de_busqueda=lista_terminos[0]
    if modo_de_busqueda=="*":
        sys.exit(0)
    if modo_de_busqueda not in [AND, NOT]:
        if OR in lista_terminos:
            lista_terminos=lista_terminos[1:]
        obtener_busqueda_OR(lista_terminos,indexador)
    if modo_de_busqueda==AND:
        lista_terminos=lista_terminos[1:]
        obtener_busqueda_AND(indexador,lista_terminos)
    if modo_de_busqueda==NOT:
        no_coincide=lista_terminos[1]
        obtener_busqueda_NOT(no_coincide,indexador)

def obtener_busqueda_OR(lista_terminos,indexador):
    """
    Funcion que crea el modo de busqueda OR: para devolver los datos
    correspondientes a este tipo de busqueda.
    Recibe una lista de terminos para buscar y el diccionario en donde estan
    almacenados los terminos como claves y una lista con las rutas de cada
    termino como valor asociado a las claves.
    Muestra los archivos asociadas a cada termino.
    """
    lista_rutas=[]
    for termino in lista_terminos:
        if termino in indexador:
            for ruta in indexador[termino]:
                lista_rutas.append(ruta)
        else:
            lista_rutas.append("No hay coincidencias.")
    lista_rutas_sin_repetir=list(sin_repetir_elementos.fromkeys(lista_rutas))
    imprimir_rutas(lista_rutas_sin_repetir)

def obtener_busqueda_AND(indexador,lista_terminos):
    """
    Funcion que crea el modo de busqueda AND: para devolver los datos
    correspondientes a este tipo de busqueda.
    Recibe un diccionario donde estan almacenados los terminos como claves y
    una lista con las rutas de cada termino como valor asociado a las claves.
    Muestra todos los archivos que coinciden con los elementos que se
    encuentran en lista_terminos.
    """
    try:
        lista_rutas=[]
        for termino in lista_terminos:
            for ruta in indexador[termino]:
                lista_rutas.append(ruta)
        _obtener_interseccion_rutas(lista_rutas,len(lista_terminos))
    except KeyError:
        print("No hay coincidencias.")
        return

def _obtener_interseccion_rutas(lista_rutas,longitud_lista_terminos):
    """
    Funcion que se encarga de resolver si todas las rutas que se encuentran en
    lista_rutas coinciden con la cantidad de repeticiones que debe ser igual a
    la longitud_lista_terminos. En este caso muestra la ruta que satisface esa
    condicion, caso contrario muestra que no hay coincidencias.
    Recibe una lista de rutas y un valor, el cual es igual a la longitud de la
    lista de terminos que recibe el modo de busqueda AND.
    """
    diccionario_rutas={}
    for ruta in lista_rutas:
        diccionario_rutas[ruta]=diccionario_rutas.get(ruta,0)+1
    for ruta in diccionario_rutas:
        if diccionario_rutas[ruta]==longitud_lista_terminos:
            print(ruta)
            return
    print("No hay coincidencias.")

def obtener_busqueda_NOT(termino_no_coincide,indexador):
    """
    Funcion que crea el modo de busqueda NOT: para devolver los datos
    correspondientes a este tipo de busqueda.
    Recibe el termino con el que se quieren obtener los archivos que no
    coinciden con dicho termino y un diccionario donde estan almacenados los
    terminos como claves y una lista con las rutas de cada termino como valor
    asociado a las claves.
    Muestra todos los archivos que no coinciden con termino_no_coincide.
    """
    lista_rutas=[]
    for termino in indexador:
        for ruta in indexador[termino]:
            if termino_no_coincide in indexador:
                if ruta in indexador[termino_no_coincide]:
                    continue
            elif termino==termino_no_coincide:
                    continue
            lista_rutas.append(ruta)
    lista_rutas_sin_repetir=list(sin_repetir_elementos.fromkeys(lista_rutas))
    imprimir_rutas(lista_rutas_sin_repetir)

def imprimir_rutas(lista_rutas):
    """
    Funcion que muestra las rutas de la lista recibida.
    Recibe una lista de rutas.
    """
    for rutas in lista_rutas:
        print(rutas)
    return

#-------------------------------------------------------------------------------

def obtener_archivos_indexados(indexador):
    """
    Funcion que se encarga de recorrer un directorio con todo su contenido y
    los subdirectorios que se encuentran en dicho subdirectorio.
    Recibe un  diccionario donde estan almacenados los terminos como claves y
    una lista con las rutas de cada termino como valor asociado a las claves.
    Devuelve la cantidad de archivos que se han encontrado a partir del
    directorio actual en adelante.
    """
    archivos_indexados=0
    for ruta,carpetas,archivos in os.walk("."):
        for nombre in archivos:
            agregar_archivos(indexador,ruta.lower(),nombre.lower())
            comprobar_archivos_de_texto(indexador,ruta.lower(),nombre.lower())
        for nombre in carpetas:
            agregar_carpetas(indexador,ruta,nombre)
        archivos_indexados+=len(archivos)
    return "Listo! Se han indexado {} archivos.".format(archivos_indexados)

def agregar_archivos(indexador,ruta,nombre_archivo):
    """
    Funcion que agrega archivos al indexador recibido y las rutas de cada uno.
    Recibe un diccionario, una ruta y el nombre de un archivo y los agrega al
    diccionario.
    """
    separacion_de_terminos=re.split('\W+',nombre_archivo)
    ruta_concatenada=os.path.join(ruta,nombre_archivo)
    agregar_contenido(indexador,separacion_de_terminos,ruta_concatenada)

def agregar_carpetas(indexador,ruta,nombre_carpeta):
    """
    Funcion que agrega el nombre de una carpeta y la ruta a la cual pertenece
    junto con su contenido al indexador recibido, el cual es un diccionario.
    Recibe un diccionario, una ruta y el nombre de una carpeta y hace lo ya
    nombrado antes.
    """
    if nombre_carpeta:
        lista_archivos_carpeta=os.listdir(nombre_carpeta)
        for archivo in lista_archivos_carpeta:
            ruta_carpeta_archivo=os.path.join(ruta,nombre_carpeta.lower(),archivo.lower())
            agregar_contenido(indexador,[nombre_carpeta.lower()],ruta_carpeta_archivo)

def comprobar_archivos_de_texto(indexador,ruta,nombre_archivo):
    """
    Funcion que comprueba si el archivo es de texto o no. En el caso de que lo
    sea se agrega su contenido al indexador.
    Recibe un diccionario, la ruta del archivo y su nombre.
    """
    lista_extensiones_archivos_de_texto=["txt","py","c","md"]
    lista_nombre_del_archivo=nombre_archivo.split(".")
    if lista_nombre_del_archivo[len(lista_nombre_del_archivo)-1] in lista_extensiones_archivos_de_texto:
        agregar_contenido_archivo(indexador,ruta,nombre_archivo)

def agregar_contenido_archivo(indexador,ruta,nombre_archivo):
    """
    Funcion que agrega al indexador el contenido de un archivo detexto y la
    ruta correspondiente a dicho archivo.
    Recibe un diccionario, una ruta y el nommbre de un archivo y agrega el
    contenido del archivo y la ruta del mismo al diccionario.
    """
    ruta_concatenada=os.path.join(ruta,nombre_archivo)
    with open(ruta_concatenada) as archivo_entrada:
        for linea in archivo_entrada:
            linea_sin_fin_de_linea=linea.rstrip("\n")
            separacion_de_terminos=re.split('\W+',linea_sin_fin_de_linea)
            agregar_contenido(indexador,separacion_de_terminos,ruta_concatenada)

def agregar_contenido(indexador,lista_terminos,ruta):
    """
    Funcion que agrega al diccionario cada termino que esta en lista_terminos y
    la ruta asociada a cada termino.
    Recibe un diccionario, una lista de terminos y una ruta.
    """
    for termino in lista_terminos:
        if termino in indexador and ruta not in indexador[termino]:
            indexador[termino.lower()].append(ruta)
        else:
            indexador[termino.lower()]=[ruta]

#-------------------------------------------------------------------------------

main()
