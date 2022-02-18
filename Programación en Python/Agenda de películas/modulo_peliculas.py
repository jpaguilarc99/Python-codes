"""
Módulo de calculos logicos para proyecto M2 agenda de películas.
autor: jpaguilarc99
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    
    peliculas = {'nombre': nombre, 'genero': genero, 'duracion': duracion,
                 'anio': anio, 'clasificacion': clasificacion, 'hora': hora, 'dia': dia}
    return peliculas

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    
    encontrar = None
    
    if nombre_pelicula in p1['nombre']:
        encontrar = p1
    elif nombre_pelicula in p2['nombre']:
        encontrar = p2
    elif nombre_pelicula in p3['nombre']:
        encontrar = p3
    elif nombre_pelicula in p4['nombre']:
        encontrar = p4
    elif nombre_pelicula in p5['nombre']:
        encontrar = p5
        
    return encontrar

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    
    mayor_pelicula = p1
    mayor_duracion = p1['duracion']
    
    if p2['duracion'] > mayor_duracion:
        mayor_pelicula = p2
        mayor_duracion = p2['duracion']
    if p3['duracion'] > mayor_duracion:
        mayor_pelicula = p3
        mayor_duracion = p3['duracion']
    if p4['duracion'] > mayor_duracion:
        mayor_pelicula = p4
        mayor_duracion = p4['duracion']
    if p5['duracion'] > mayor_duracion:
        mayor_pelicula = p5
        mayor_duracion = p5['duracion']
        
    return mayor_pelicula

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    
    duracion = p1['duracion'] + p2['duracion'] + p3['duracion'] + p4['duracion'] + p5['duracion']
    promedio_duracion = duracion // 5
    
    formato_hora = promedio_duracion // 60
    formato_minutos = promedio_duracion % 60
    formato_entrega = '0' + str(formato_hora) + ':' + str(formato_minutos)
            
    return formato_entrega

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    
    estreno1 = ""
    estreno2 = ""
    estreno3 = ""
    estreno4 = ""
    estreno5 = ""
    estreno = "Ninguna"
    
    if p1['anio'] > anio:
        estreno1 = p1['nombre'] + ', '
        estreno = estreno1
        
    if p2['anio'] > anio:
        estreno2 = p2['nombre'] + ', '
        estreno = estreno1 + estreno2
                
    if p3['anio'] > anio:
        estreno3 = p3['nombre'] + ', '
        estreno = estreno1 + estreno2 + estreno3
        
    if p4['anio'] > anio:
        estreno4 = p4['nombre'] + ', '
        estreno = estreno1 + estreno2 + estreno3 +  estreno4
        
    if p5['anio'] > anio:
        estreno5 = p5['nombre'] + ', '
        estreno = estreno1 + estreno2 + estreno3 + estreno4 + estreno5
                
    return estreno

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto
    conteo_18_mas = 0
    
    if p1['clasificacion'] == '18+':
        conteo_18_mas += 1
    if p2['clasificacion'] == '18+':
        conteo_18_mas += 1
    if p3['clasificacion'] == '18+':
        conteo_18_mas += 1
    if p4['clasificacion'] == '18+':
        conteo_18_mas += 1
    if p5['clasificacion'] == '18+':
        conteo_18_mas += 1
        
    return conteo_18_mas

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
                    
    #Reagendar hora y día
    reagenda = True
    
    if (nueva_hora == p1['hora']) and (nuevo_dia == p1['dia']): 
        reagenda = False
    elif (nueva_hora == p2['hora']) and (nuevo_dia == p2['dia']):
        reagenda = False
    elif (nueva_hora == p3['hora']) and (nuevo_dia == p3['dia']):
        reagenda = False
    elif (nueva_hora == p4['hora']) and (nuevo_dia == p4['dia']):
        reagenda = False
    elif (nueva_hora == p5['hora']) and (nuevo_dia == p5['dia']):
        reagenda = False
    elif (control_horario == True) and (('Documental' in peli['genero']) and (nueva_hora > 2200)):
        reagenda = False
    elif (control_horario == True) and (('Drama' in peli['genero']) and (nuevo_dia == 'Viernes')):
        reagenda = False
                       
    return reagenda
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    
    if edad_invitado > 18:
        permiso = True
    else:
        if edad_invitado < 15 and "Terror" in peli.get("genero"):
            permiso = False
        elif edad_invitado <= 10 and "Familiar" not in peli.get("genero"):
            permiso = False
        elif (edad_invitado < 18 and "18+" in peli.get("clasificacion")) or (edad_invitado<13 and "13+" in peli.get("clasificacion")):
            if autorizacion_padres == "No":
                permiso = False
            else:
                permiso = True
        else:
            permiso = True
            
        return permiso
