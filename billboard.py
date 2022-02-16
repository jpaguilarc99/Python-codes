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



