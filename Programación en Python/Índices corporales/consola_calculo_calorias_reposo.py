# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:14:43 2022

@author: jpagu
"""

import calculadora_indices as calc

def ejecutar_calculo_calorias_reposo(peso: float, altura: float, edad: int, valor_genero: int)-> None:
    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_reposo = round(calorias_reposo, 2)
    print('Tus calorias consumidas en reposo son: ', calorias_reposo)
    
def iniciar_aplicacion()-> None:
    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    valor_genero = int(input('Ingrese 5 si es hombre y si es mujer ingrese -161: '))
    ejecutar_calculo_calorias_reposo(peso, altura, edad, valor_genero)
    
iniciar_aplicacion()