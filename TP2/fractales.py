def main():
	"""
    Crea al fractal a partir de los datos ingresados por el usuario.
    """
	fractal=pedir_fractal()
	tablero_inicial=pedir_coordenadas_monticulos_y_cantidad_de_arena_en_cada_uno()
	nombre_de_archivo=pedir_nombre_archivo_salida()
	celdas,colores,espejado=definir_parametros()
	tablero_inicial=recorrer_tableros(tablero_inicial,fractal)
	tablero_ampliado=aumentar_tablero(tablero_inicial,celdas)
	dimension=fractal[0]*celdas[0],fractal[1]*celdas[1]
	tablero_ampliado,dimension=construccion_final(tablero_ampliado,dimension,espejado)
	escribir_archivo(nombre_de_archivo,tablero_ampliado,dimension,colores)

#Parametros obligatorios para el usuario----------------------------------------
def pedir_fractal():
	"""
    Le pide al usuaio el tamaño del fractal. Las coordenadas del mismo son de
    forma horizontal y verical y tienen que ser numeros enteros.
    """
	ancho_fractal=pedir_datos("Ingrese el ancho del fractal: ",0,1000)
	alto_fractal=pedir_datos("Ingrese el alto del fractal: ",0,1000)
	return ancho_fractal,alto_fractal

def pedir_coordenadas_monticulos_y_cantidad_de_arena_en_cada_uno():
	"""
    Le pide al usuario las coorenadas de los monticulos de arena y la cantidad
    de granos de arena que hay en cada coordenada. Las coordenadas y la
    cantidad son numeros enteros y estan representados por un diccionario
    cuya clave es la coordenada definida por una tupla de numeros y su valor
    asociado la cantidad de granos de arena.
    """
	mensaje="Desea seguir ingresando granos de arena? No para dejar de ingresar: "
	continuar=" "
	posicion_granos_arena={}
	while continuar.lower()!="no":
		columna_monticulo_arena=pedir_datos("Ingrse la primera coordenada del monticulo de arena: ",0,1000)
		fila_monticulo_arena=pedir_datos("Ingrse la segunda coordenada del monticulo de arena: ",0,1000)
		cant_granos_arena=pedir_datos("Ingrese la cantidad de granos de arena a colocar: ",0,15000)
		posicion_granos_arena[columna_monticulo_arena,fila_monticulo_arena]=posicion_granos_arena.get((columna_monticulo_arena,fila_monticulo_arena),0)+cant_granos_arena
		continuar=input(mensaje)
	return posicion_granos_arena

def pedir_nombre_archivo_salida():
	"""
    Le pide al asuario el nombre del archivo de salida, el cual es de formato
    ppm y genera una imagen (fractal).
    """
	nombre_archivo=input("Ingrese el nombre deseado del archivo: ")+".ppm"
	return nombre_archivo

#Parametros opcionales para el usuario------------------------------------------
def pedir_celda():
	"""
    Le pide al usuario el tamaño de la celda horizontal y vertical, las cuales
    representan a los pixeles que va generar la imagen (fractal). Estos valores
    son de formato numeros enteros.
    """
	celda_horizontal=pedir_datos("ingrese el tamaño de la celda horizontal(pixel): ",1,100)#pixel horizontal
	celda_vertical=pedir_datos("ingrese el tamaño de la celda vertical(pixel): ",1,100)#pixel vertical
	if celda_horizontal<=0 or celda_vertical<=0:
		print("Ingrese numeros positivos.")
	return celda_horizontal,celda_vertical

def pedir_colores():
	"""
    Le pide al usuario que elija 4 colores de los disponibles que se le dan a
    elegir. Los colores estan representados por diccionarios cuyas claves son
    cadenas y representan al nombre del color y sus valores asociados la
    intensidad del color en formato rgb.
    """
	print("A continuacion debe elegir 4 colores distintos.")
	paleta_de_colores={}
	paleta_de_colores["rojo"]="255 000 000"
	paleta_de_colores["verde"]="000 255 000"
	paleta_de_colores["azul"]="000 000 255"
	paleta_de_colores["amarillo"]="255 255 000"
	paleta_de_colores["naranja"]="244 070 017"
	paleta_de_colores["negro"]="000 000 000"
	paleta_de_colores["bordo"]="117 021 030"
	colores=0
	lista_colores=list(paleta_de_colores.keys())
	colores_seleccionados={}
	lista_colores_seleccionados=[]
	while colores<= 3:
		print(lista_colores)
		color=input("Seleccione un color disponible de los colores mostrados: ")
		color=color.lower()
		if color in lista_colores:
			colores_seleccionados[color]=paleta_de_colores[color]
			lista_colores.remove(color)
			colores+=1
		else:
			print("El color que ha elegido es incorrecto, vuelva a elegir otro color.")
	color1,color2,color3,color4=list(colores_seleccionados.values())
	lista_colores_seleccionados.append(color1)
	lista_colores_seleccionados.append(color2)
	lista_colores_seleccionados.append(color3)
	lista_colores_seleccionados.append(color4)
	return lista_colores_seleccionados

def pedir_espejado():
	"""
    Le pide al usuario la cantidad de veces que quiere espejar horizontal y
    verticalmente al fractal. Estos valores son de formato numeros enteros.
    """
	espejado_vertical=pedir_datos("Ingrese espejado vertical: ",1,4)
	espejado_horizontal=pedir_datos("Ingrese espejado horizontal: ",1,4)
	return espejado_vertical,espejado_horizontal

def pedir_datos(mensaje,minimo,maximo):
	"""
	Le pide al usuario lo que se pase como mensaje, el cual es de formato str.
	Minimo y maximo son numeros de formato numeros enteros.
	Pre condicion: mensaje debe ser una frase que le pida al usuario que
	ingrese un valor. Este valor debe ser un numero y debe estar entre minimo y
	maximo, si no se le pide al usuario que ingrese dicho valor hasta que lo
	ingrese correctamente.
	Post condicion: devuelve el valor ingresado si paso la pre condicion.
	"""
	print("Ingrese un numero entre {} y {}".format(minimo,maximo))
	numero=input(mensaje)
	while not numero_valido(numero,minimo,maximo):
		print("Valor incorrecto, ingreselo otra vez.")
		numero=input(mensaje)
	return int(numero)

def numero_valido(numero,minimo,maximo):
	"""
	Valida un numero cuyo formato es str y este debe estar entre los valores
	minimo y maximo los cules son numeros de formato int. Devuelve True si es
	un numero valido.
	"""
	if numero.isdigit() and numero.isdigit()>=minimo and numero.isdigit()<=maximo:
		return True

#Configuracion------------------------------------------------------------------
def configuracion_por_defecto():
	"""
	Determina la configuracion por defecto del temaño de la celda (los pixeles),
	el espejado del fractal y los 4 colores (rojo, azul, negro y amarillo).
	"""
	tamaño_celdas=10,10
	espejado=1,1
	colores={}
	colores["negro"]="000 000 000"
	colores["amarillo"]="255 255 000"
	colores["rojo"]="255 000 000"
	colores["azul"]="000 000 255"
	lista_colores=[]
	lista_colores.append("000 000 000")
	lista_colores.append("255 255 000")
	lista_colores.append("255 000 000")
	lista_colores.append("000 000 255")
	return tamaño_celdas,lista_colores,espejado

def pedir_configuracion():
	"""
    Le pregunta al usuario si desea usar la configuracion por defecto.
    """
	while True:
		consulta=input("Desea utilizar la configuracion por defecto?(si-no): ")
		consulta=consulta.lower()
		if consulta=="si" or consulta=="no":
			return consulta
		print("Respuesta incorrecta, vuelva a responder por favor.")

def definir_parametros():
	"""
	Define si se usa la configuracion por defecto o no. Si no se usa la
	configuracion por defecto se usa la configuracion ingresada por el usuario.
	"""
	opcion=pedir_configuracion()
	if opcion=="no":
		celdas_elegidas=pedir_celda()
		colores_elegidos=pedir_colores()
		espejado_elegido=pedir_espejado()
		return celdas_elegidas,colores_elegidos,espejado_elegido
	celdas,colores,espejado=configuracion_por_defecto()
	return celdas,colores,espejado

#Construccion del Sandpile------------------------------------------------------
def validar_diccionario(diccionario):
	"""
    Valida que haya por lo menos cuatro o mas de cuatro granos de arena en las
    celdas del tablero.
    """
	valores=list(diccionario.values())
	for elemento in valores:
		if elemento>=4:
			return True
	return False

def distribuir_granos(dimension,tablero,posicion,cant):
	"""
    Distribuye los granos de arena del tablaro segun la dimension del
    mismo y la posicion en la que se encuntren los granos y su cantidad.
    """
	ancho,alto=dimension
	columna,fila=posicion
	distribucion=cant//4
	sobrante=cant%4
	for f in range(fila-1,fila+2):
		if (f>=0 and f<alto) and f!=fila:
			tablero[columna,f]=tablero.get((columna,f),0)+distribucion
	for c in range(columna-1,columna+2):
		if (c>= 0 and c<ancho) and c!=columna:
			tablero[c,fila]=tablero.get((c,fila),0)+distribucion
	tablero[columna,fila]=sobrante
	return tablero

def sumar_tableros(tablero1,tablero2):
	"""
    Suma dos tableros, los cuales son dos diccionarios distintos.
    """
	for clave in tablero2:
		tablero1[clave]=tablero1.get(clave,0)+tablero2[clave]
	return tablero1

def recorrer_tableros(tablero,dimension):
	"""
    Se crea un tablero auxiliar el cual se va actualizando con la distribucion
    de granos de arena y se suma con el tablero que se esta generado para ir
    generando el fractal.
    """
	while validar_diccionario(tablero):
		tablero_aux={}
		for clave in tablero:
			if tablero[clave] < 4:
				continue
			tablero_aux=distribuir_granos(dimension,tablero_aux,clave,tablero[clave])
			tablero[clave]=0
		tablero=sumar_tableros(tablero,tablero_aux)
	return tablero

def aumentar_tablero(diccionario,celdas):
	"""
	Se encarga de aumentar la resolucion del fractal, a partir de aumentar el
	tamaño del tablero.
	"""
	tablero_nuevo={}
	for clave in diccionario:
		posicion=clave
		cant=diccionario[clave]
		principio_columnas=posicion[0]*celdas[0]
		final_columnas=(posicion[0]*celdas[0])+celdas[0]
		principio_filas=posicion[1]*celdas[1]
		final_filas=(posicion[1]*celdas[1])+celdas[1]
		for c in range(principio_columnas,final_columnas):
			for f in range(principio_filas,final_filas):
				tablero_nuevo[c,f]=cant
	return tablero_nuevo

#Espejados----------------------------------------------------------------------
def espejado_vertical(diccionario,dimension,veces_a_espejar):
	"""
    Espeja verticalmente al fractal de acuerdo a los monticulos de arena que
    haya ingresado el usuario, la dimension del fractal y la cantidad de veces
    que se desa espejar en esta direccion. Si el usuario desea usar la
	configuracion por defecto el espejado vertical va a ser una vez. Caso
	contrario lo que el usuario ingrese.
    """
	if veces_a_espejar==1:
		return diccionario,dimension
	espejado=1
	altura_inicial=dimension[1]
	while espejado<veces_a_espejar:
		diccionario_aux={}
		altura_final=altura_inicial*2
		for clave in diccionario:
			fila_a_espejar=clave[1]
			fila_espejada=altura_final-(1+fila_a_espejar)
			diccionario_aux[clave[0],fila_espejada]=diccionario[clave]
		diccionario=sumar_tableros(diccionario,diccionario_aux)
		altura_inicial=altura_final
		espejado+=1
	dimension_nueva=dimension[0],altura_final
	return diccionario,dimension_nueva

def espejado_horizontal(diccionario,dimension,veces_a_espejar):
	"""
    Espeja horizontalmente al fractal de acuerdo a los monticulos de arena que
    haya ingresado el usuario, la dimension del fractal y la cantidad de veces
    que se desa espejar en esta direccion. Si el usuario desea usar la
	configuracion por defecto el espejado horizontal va a ser una vez. Caso
	contrario lo que el usuario ingrese.
    """
	if veces_a_espejar==1:
		return diccionario,dimension
	espejado=1
	altura_inicial=dimension[0]
	while espejado<veces_a_espejar:
		diccionario_aux={}
		altura_final=altura_inicial*2
		for clave in diccionario:
			columna_a_espejar=clave[0]
			columna_espejada=altura_final-(1+columna_a_espejar)
			diccionario_aux[columna_espejada,clave[1]]=diccionario[clave]
		diccionario=sumar_tableros(diccionario,diccionario_aux)
		altura_inicial=altura_final
		espejado+=1
	dimension_nueva=altura_final,dimension[1]
	return diccionario,dimension_nueva

def construccion_final(diccionario,dimension,espejado):
	"""
    Crea el estado del frctal el cual esta espejado, con los granos de arena
    distribuidos en el tabelro segun la dimension del mismo.
    """
	diccionario,dimension=espejado_vertical(diccionario,dimension,espejado[0])
	diccionario,dimension=espejado_horizontal(diccionario,dimension,espejado[1])
	return diccionario,dimension

def escribir_archivo(nombre_archivo,diccionario,dimension,colores):
	"""
    A partir del archivo que se le pide al usuario que ingrese se crea un
    archivo cuyo formato es ppm el cual representa el fractal (una imagen)
    definitivo con todos los granos de arena distribuidos juntos con los
    colores por cada pixel de a cuerdo a la dimension del fractal.
    """
	with open(nombre_archivo,"w") as archivo:
		archivo.write("P3\n")
		archivo.write(str(dimension[0])+" "+str(dimension[1])+"\n")
		archivo.write("255\n")
		for fila in range(dimension[1]):
			for columna in range(dimension[0]):
				if ((columna,fila) not in diccionario) or diccionario[columna,fila]==0:
					archivo.write(colores[0]+"\n")
					continue
				if diccionario[columna,fila]==1:
					archivo.write(colores[1]+"\n")
					continue
				if diccionario[columna,fila]==2:
					archivo.write(colores[2]+"\n")
					continue
				if diccionario[columna,fila]==3:
					archivo.write(colores[3]+"\n")
					continue

main()
