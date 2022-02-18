# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:22:19 2022

@author: jpagu
"""

import calculadora_indices as calc

def ejecutar_calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float)-> None:
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    calorias_actividad = round(calorias_actividad, 2)
    print('Sus calorias consumidas por actividad fisica son: ', calorias_actividad)
    
def iniciar_aplicacion()-> None:
    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    valor_genero = int(input('Ingrese 5 si es hombre y si es mujer ingrese -161: '))
    valor_actividad = float(input('Ingrese 1.2 si hace poco o ningún ejercicio, ingrese 1.375 si hace ejercicio ligero (1 a 3 días a la semana), ingrese 1.55 si hace ejercicio moderado (3 a 5 días a la semana), ingrese 1.72 si es deportista (6 a 7 días a la semana), ingrese 1.9 si es atleta (entrenamiento diario mañana y noche): '))
    ejecutar_calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    
iniciar_aplicacion()