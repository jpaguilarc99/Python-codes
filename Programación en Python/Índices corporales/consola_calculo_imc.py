# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:52:42 2022

@author: jpagu
"""

import calculadora_indices as calc

def ejecutar_calcular_IMC(peso: float, altura: float)-> None:
    IMC = calc.calcular_IMC(peso, altura)
    IMC = round(IMC, 2)
    print('Su índice de masa corporal es: ', IMC)
    
def iniciar_aplicacion()-> None:
    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en metros: '))
    ejecutar_calcular_IMC(peso, altura)
    
iniciar_aplicacion()