# -*- coding: utf-8 -*-
"""
Modulo de funciones para proyecto Billboard Hot top 100 M3
autor: jpaguilarc99
"""
#Función 1
def leer_archivo_canciones(path)-> list:
    """
    Esta función carga el archivo en formato CSV del top 100 canciones Hot Billboard y guarda cada uno de sus datos
    en 5 diferentes diccionarios representados por las llaves posición, nombre_cancion, nombre_artista, anio y letra.
    """    
    lista_diccionarios = []
    
    
    archivo = open(path, "r")    
    
    linea = archivo.readline()
    
    while linea != "":
        datos = linea.split(",")
        
        posicion = datos[0]
        nombre_cancion = datos[1]
        nombre_artista = datos[2]
        anio = datos[3]
        letra = datos [4]
        
        
        diccionarios_canciones = {"posicion": posicion, "nombre_cancion": nombre_cancion,
                                  "nombre_artista": nombre_artista, "anio": anio, "letra": letra}
    
        lista_diccionarios.append(diccionarios_canciones)
        
        linea = archivo.readline()        
    
    return lista_diccionarios

path = "billboard.csv"
archivo_principal = leer_archivo_canciones(path)

#Función 2
def informacion_una_cancion(lista_canciones: list, nombre_cancion: str, año_ranking: str)-> dict:
    """
    Esta función recibe como parámetros la lista de diccionarios de canciones retornada por la función
    leer_archivo_canciones, el nombre de una canción y el año de ranking de dicha canción.
    La función retorna el diccionario con toda la información de la canción buscada.
    """
    for i in range(len(lista_canciones)):
        encontrar_cancion = None                
        if nombre_cancion == lista_canciones[i]['nombre_cancion']:
            if año_ranking == lista_canciones[i]['anio']:
                encontrar_cancion = lista_canciones[i]               
        
                return encontrar_cancion

info_por_cancion = informacion_una_cancion(archivo_principal, "get closer", "1976")
#print(info_por_cancion)

#Función 3
def canciones_por_año(lista_canciones: list, año_canciones: str)-> list:
    """
    Esta función recibe como parámetros la lista completa de canciones (diccionarios) y un año en el que se buscan
    todas las canciones del ranking de ese año.
    Retorna una nueva lista de diccionarios con la información de todas las canciones que pertenecen al año que entra
    por parámetro, exceptuando su letra.
    Si no hay ninguna canción en el año que se solicita, la función retorna una lista vacía.
    """
    canciones_por_año = []
    
    for i in range(len(lista_canciones)):
        if año_canciones == lista_canciones[i]['anio']:
            por_año = lista_canciones[i]
            del por_año['letra']            
            canciones_por_año.append(por_año)             
    
    return canciones_por_año

canciones_x_año = canciones_por_año(archivo_principal, "2015")
#print(canciones_x_año)

#Función 4
def canciones_artista_rango(lista_canciones: list, nombre_artista: str, año_inicial: int, año_final: int)-> list:
    """
    Función que recibe por parámetros la lista completa de canciones (diccionarios), el nombre de un artista y
    un rango de años (año_inicial y año_final).
    Retorna una nueva lista con la información de todas las canciones del artista en dicho rango de años, sin la
    letra de las canciones.
    """
    canciones_del_artista = []
    
    for i in range(len(lista_canciones)):
        if nombre_artista == lista_canciones[i]['nombre_artista']:
                rango_años = list(range(año_inicial, año_final + 1))                
                if int(lista_canciones[i]['anio']) in rango_años:
                    sin_letra = lista_canciones[i]
                    del sin_letra['letra']
                    canciones_del_artista.append(sin_letra)        
    
    return canciones_del_artista

rango_años_artista = canciones_artista_rango(archivo_principal, "tommy james and the shondells", 1960, 1980)
#print(rango_años_artista)

#Función 5
def canciones_por_artista(lista_canciones: list, nombre_artista: str)-> list:
    """
    Funcion que recibe por parámetros la lista completa de canciones (diccionarios) y el nombre del artista.
    Retorna una nueva lista con toda la información de todas las canciones del artista buscado a excepción de la letra.
    """
    canciones_artista = []
    
    for i in range(len(lista_canciones)):
        if nombre_artista == lista_canciones[i]['nombre_artista']:
            sin_letra = lista_canciones[i]
            del sin_letra['letra']
            canciones_artista.append(sin_letra)
        
    return canciones_artista 

canciones_por_art = canciones_por_artista(archivo_principal, "the yardbirds")
#print(canciones_por_art)

#Función 6
def una_cancion(lista_canciones: list, nombre_cancion: str)-> list:
    """
    Función que recibe por parámetro la lista completa de canciones (diccionarios) y
    el nombre de una canción en específico.
    Retorna una nueva lista de strings con el nombre de los artistas que han interpretado
    aquella canción.
    """
    lista_strings_artistas = []
    
    for i in range(len(lista_canciones)):        
        if nombre_cancion == lista_canciones[i]['nombre_cancion']:
            artistas_cancion = lista_canciones[i]['nombre_artista']
            lista_strings_artistas.append(artistas_cancion)
            
        
    return lista_strings_artistas

artistas_cancion = una_cancion(archivo_principal, "baby im yours")
#print(artistas_cancion)

#Función 7 
def cantidad_minima_canciones(lista_canciones: list, minima: int)-> dict:
    """
    Función que recibe por parámetro la lista completa de canciones (diccionarios) y 
    una cantidad mínima de apariciones en el top 100 hot billboard.
    Retorna un diccionario con el nombre de los artistas que han aparecido un número
    mayor de veces al indicado y la cantidad de veces que han aparecido.
    """
    aparicion_por_artista = {}
    artistas_minima = {}
    
    for i in lista_canciones:
        artista = i["nombre_artista"]
        if artista in aparicion_por_artista:
            aparicion_por_artista[artista] += 1
        else:
            aparicion_por_artista[artista] = 1
            
    for j in aparicion_por_artista:
        if aparicion_por_artista[j] > minima:
            artistas_minima[j] = aparicion_por_artista[j]
     
    return artistas_minima

minima = cantidad_minima_canciones(archivo_principal, 30)
#print(minima)

#Función 8
def mayor_numero_canciones(lista_canciones: list)-> dict:
    """
    Función que recibe como parámetro la lista completa de canciones (diccionarios).
    Retorna un diccionario con el artista que ha aparecido más veces en el top 100 rank
    de hot billboard y la cantidad de veces que lo ha hecho.
    """
    mayor_canciones = {}
    diccionario_artistas = cantidad_minima_canciones(lista_canciones, 30)
    mas = 0
    
    for i in diccionario_artistas:
        if diccionario_artistas[i] > mas:
            mas = diccionario_artistas[i]   
            
    mayor_canciones[i] = mas            
        
    return mayor_canciones

mayor_num_canciones = mayor_numero_canciones(archivo_principal)
#print(mayor_num_canciones)

#Función 9
def lista_de_canciones_por_artista(lista_canciones: list)-> dict:
    artistas_canciones = {}
    for i in lista_canciones:
        artista = i["nombre_artista"]
        lista_canciones = [i["nombre_cancion"]]
        if artista in artistas_canciones:
            obtener = artistas_canciones.get(artista)
            if i["nombre_cancion"] not in obtener:
                obtener.append(i["nombre_cancion"])
                artistas_canciones[artista] = obtener
        else:
            obtener = artistas_canciones.get(artista, lista_canciones)
            artistas_canciones[artista] = obtener
            
    return artistas_canciones            
    

canciones_de_un_artista = lista_de_canciones_por_artista(archivo_principal)
#print(canciones_de_un_artista)

#Función 10
def promedio_todas_canciones(lista_canciones: list) -> float:
    artistas_canciones = {}
    for i in lista_canciones:
        artista = i["nombre_artista"]
        new = [i["nombre_cancion"]]
        if artista in artistas_canciones:
            obtener = artistas_canciones.get(artista)
            if i["nombre_cancion"] not in obtener:
                obtener.append(i["nombre_cancion"])
                artistas_canciones[artista] = obtener
        else:
            obtener = artistas_canciones.get(artista, new)
            artistas_canciones[artista] = obtener
    cantidad_artistas = len(artistas_canciones)
    numero_canciones = 0
    for b in artistas_canciones:
        numero_canciones += len(artistas_canciones[b])
    promedio_canciones = round((numero_canciones / cantidad_artistas) , 2)
    return promedio_canciones

promedio_canciones = promedio_todas_canciones(archivo_principal)









