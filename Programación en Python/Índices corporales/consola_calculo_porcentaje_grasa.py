# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:04:36 2022

@author: jpagu
"""

import calculadora_indices as calc

def ejecutar_calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)-> None:
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    porcentaje_grasa = round(porcentaje_grasa, 2)
    print('Su porcentaje de grasa corporal es: ', porcentaje_grasa, '%')
    
def iniciar_aplicacion()-> None:
    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en metros: '))
    edad = int(input('Ingrese su edad en años: '))
    valor_genero = float(input('En caso de ser hombre digite 10.8 y en caso de ser mujer digite 0: '))
    ejecutar_calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    
iniciar_aplicacion()