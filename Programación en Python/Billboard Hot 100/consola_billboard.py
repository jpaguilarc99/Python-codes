#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Interfaz basada en consola para la interacción con el usuario. Billboard hot top 100 M3.

@author: Cupi2 & jpaguilarc99
"""

import billboard as bb

def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    las canciones y las carga.
    Retorno: list
        La lista de canciones con la información del archivo.
    """
    canciones = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.leer_archivo_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar las canciones del Ranking")
    else:
        print("Se cargaron", len(canciones), "canciones a partir del archivo.")
    return canciones


def ejecutar_buscar_cancion(canciones:list)->None:
    """ Ejecuta la opción de buscar una canción dado el nombre y el año del 
    ranking al cual pertenece 
    """
    cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = input("Por favor ingrese el año de la canción que desea buscar: ")
    info_cancion = bb.informacion_una_cancion(canciones, cancion, anio)  
    print(info_cancion)
    

def ejecutar_canciones_anio(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un año dado 
    """
    anio = input("Por favor ingrese el año que desea consultar: ")
    info_canciones_año = bb.canciones_por_año(canciones, anio)
    print(info_canciones_año)   
    
def ejecutar_canciones_artista_periodo(canciones:list)->None:
    """ Ejecuta la opción de consultar las canciones de un artista dado en 
    un periodo de tiempo definido 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial que desea buscar: "))
    anio_fin = int(input("Por favor ingrese el año final que desea buscar: "))
    
    info_artista_rangos = bb.canciones_artista_rango(canciones, artista, anio_inic, anio_fin)
    print(info_artista_rangos)

def ejecutar_todas_canciones_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar todas las canciones de un artista dado 
    """
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    
    info_canciones_un_artista = bb.canciones_por_artista(canciones, artista)
    print(info_canciones_un_artista)
    
def ejecutar_todos_artistas_cancion(canciones:list)->None:
    """ Ejecuta la opción de consultar todos los artistas que han interpretado 
    una canción dada 
    """
    nombre_cancion = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    
    info_artistas_una_cancion = bb.una_cancion(canciones, nombre_cancion)
    print(info_artistas_una_cancion)

def ejecutar_artistas_mas_populares(canciones:list)->None:
    """ Ejecuta la opción de consultar los artistas más populares 
    """
    minima = int(input("Por favor ingrese la cantidad mínima de canciones que desea buscar: "))
    
    info_minimo_canciones = bb.cantidad_minima_canciones(canciones, minima)
    print(info_minimo_canciones)
     
def ejecutar_artista_estrella(canciones:list)->None:
    """ Ejecuta la opción de consultar el artista estrella de todos los tiempos 
    """
    artista_estrella = bb.mayor_numero_canciones(canciones)
    print(artista_estrella)    

def ejecutar_artistas_y_sus_canciones(canciones:list)->None:
    """ Ejecuta la opción de consultar la lista completa de artistas del Billboard 
    junto con sus canciones 
    """
    artistas_y_sus_canciones = bb.lista_de_canciones_por_artista(canciones)
    print(artistas_y_sus_canciones)

def ejecutar_promedio_canciones_por_artista(canciones:list)->None:
    """ Ejecuta la opción de consultar la cantidad promedio de canciones que los 
    artistas tienen en el listado de Billboard 
    """
    promedio_canciones = bb.promedio_todas_canciones(canciones)
    print(f"El promedio general de canciones por artista en los ranking top 100 Hot Billboard es {promedio_canciones}")
    
    
def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de canciones")
    print("2. Buscar una canción")
    print("3. Consultar las canciones de un año")
    print("4. Consultar las canciones de un artista en un periodo")
    print("5. Consultar todas las canciones de un artista")
    print("6. Consultar todos los artistas que han interpretado una canción")
    print("7. Consultar los artistas más populares")
    print("8. Consultar el artista estrella de todos los tiempos")
    print("9. Consultar los artistas y sus canciones")    
    print("10. Consultar la cantidad promedio de canciones por artista")
    print("11. Salir.")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    canciones = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            canciones=ejecutar_cargar_canciones()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_cancion(canciones)
        elif opcion_seleccionada == 3:
            ejecutar_canciones_anio(canciones)
        elif opcion_seleccionada == 4:
            ejecutar_canciones_artista_periodo(canciones)
        elif opcion_seleccionada == 5:
            ejecutar_todas_canciones_artista(canciones)
        elif opcion_seleccionada == 6:
            ejecutar_todos_artistas_cancion(canciones)
        elif opcion_seleccionada == 7:
            ejecutar_artistas_mas_populares(canciones)
        elif opcion_seleccionada == 8:
            ejecutar_artista_estrella(canciones)
        elif opcion_seleccionada == 9:
            ejecutar_artistas_y_sus_canciones(canciones)
        elif opcion_seleccionada == 10:
            ejecutar_promedio_canciones_por_artista(canciones)            
        elif opcion_seleccionada == 11:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

