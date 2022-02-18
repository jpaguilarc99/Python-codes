# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:26:15 2022

@author: jpagu
"""

def calcular_IMC(peso: float, altura: float)-> float:
    """
    Calcula el indice de masa corporal (IMC) a partir del peso (kg) dividido entre el cuadrado de la altura (metros) 
    """
     
    return peso / (altura)**2

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)-> float:
    IMC = calcular_IMC(peso, altura)
    #par1 = 1.2 * IMC
    #par2 = 0.23 * edad
    #par3 = 5.4 - valor_genero
    return (1.2 * IMC) + (0.23 *edad) - (5.4) - valor_genero

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int)-> float:
    par1 = 10 * peso
    par2 = 6.25 * altura
    par3 = 5*edad
    return par1 + par2 - par3 + valor_genero

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float)-> float:
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    TMB_actividad = TMB * valor_actividad
    return TMB_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int)-> float:
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return print('Para adelgazar, se recomienda que consumas entre: ', TMB*0.80, 'y ', TMB*0.85, 'calorías al día. Siendo ', TMB*0.80,'el rango inferior, y ', TMB*0.85,' el rango superior.')

