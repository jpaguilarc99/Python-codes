# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 19:31:15 2022

@author: jpagu
"""

import calculadora_indices as calc

def ejecutar_calculo_calorias_adelgazar(peso: float, altura: float, edad: int, valor_genero: int)-> None:
    calorias_adelgazar = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(calorias_adelgazar)
    
def iniciar_aplicacion()-> None:
    peso = float(input('Ingrese su peso en kilogramos: '))
    altura = float(input('Ingrese su altura en centimetros: '))
    edad = int(input('Ingrese su edad en años: '))
    valor_genero = int(input('Ingrese 5 si es hombre y si es mujer ingrese -161: '))
    ejecutar_calculo_calorias_adelgazar(peso, altura, edad, valor_genero)
    
iniciar_aplicacion()