# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:58:41 2022

"""
import random as rnd

print("\n")
print("|****************************|")
print("|**|      Bienvenidos     |**|")
print("|**|        Juego         |**|")
print("|****************************|")
print("")

print("El juego consiste en que se tiene un banco de 6 palabras de 5 letras, al iniciar el juego \n")
print("se selecciona automáticamente una de las 6 palabras al azar. El jugador debe conseguir \n")
print("adivinar la palabra secreta en menos de 6 intentos ingresando solo palabras de 5 letras. \n")
print("Si en el sexto intento no se ha adivinado la palabra, la palabra secreta cambia aleatoriamente \n")
print("y el juego vuelve a comenzar. \n")
print("Si en la pista de intento ves un simbolo '+' significa que la letra se encuentra en la misma posición, \n")
print("Si en la pista de intento ves un simbolo '*' significa que la letra está en la palabra pero no en la posición. \n")
print("--------------------------------------------------------------------- \n")

lista_palabras = ['apoya', 'asado', 'agoto', 'aguas', 'agria', 'afana'] #Banco de palabras
aleatorio = rnd.randint(0, 5) #Selecciona una palabra aleatoria del banco de palabras
palabra_secreta = lista_palabras[aleatorio] 
letras_palabra_secreta = list(palabra_secreta) 
lista_pistas = []

a = 0 #Controlador del ciclo while
intentos = 1 #Conteo de intentos

while a < 7:
    lista_pistas = []
    if intentos > 6: #Si se exceden los 6 intentos el ciclo se rompe.
        print(f"Agotaste tus intentos. La palabra era '{palabra_secreta}' \n")
        print("Cambiando la palabra secreta... \n")
        print("-----------------------------------------------------------------------------------------------------------")
        al_azar = rnd.randint(0, 5)
        palabra_secreta = lista_palabras[al_azar]
        intentos = 1
        a = 0
        continue
        
    print(f"Este es tu intento número {intentos} \n")
    palabra_intento = input("Ingrese una palabra de 5 letras: ")    
    palabra_intento = palabra_intento.lower() #Vuelve minusculas la palabra del usuario
    letras_intento = list(palabra_intento)  #Crea una lista con las letras de la palabra ingresada
    if len(letras_intento) > 5 or len(letras_intento) < 5:
        print("Debes ingresar una palabra de 5 letras. Por favor ingresa otra palabra. \n")
        continue
    
    if letras_palabra_secreta == letras_intento: #Si el jugador adivina la palabra se ejecuta el condicional
        print(f"Felicidades, ganaste!!! La palabra era '{palabra_secreta}'. \n")
        print("Cambiando la palabra secreta... \n")
        print("-----------------------------------------------------------------------------------------------------------")
        al_azar = rnd.randint(0, 5)
        palabra_secreta = lista_palabras[al_azar]
        intentos = 1
        a = 0
        continue
    
    for i in range(0, len(letras_intento)):    
        posicion_i = letras_intento.index(letras_intento[i])
        posicion_j = letras_palabra_secreta.index(letras_palabra_secreta[i])
        if letras_intento[i] not in letras_palabra_secreta:
            lista_pistas.append(" ")
            
            
        if letras_intento[i] in letras_palabra_secreta: 
            if posicion_i == posicion_j and letras_intento[i] == letras_palabra_secreta[i]: 
                lista_pistas.append("+")
                
                
            if posicion_i != posicion_j and letras_intento[i] != letras_palabra_secreta[i]: 
                lista_pistas.append("+")
                
                
            if posicion_i == posicion_j and letras_intento[i] != letras_palabra_secreta[i]:
                lista_pistas.append("*")
                
                
            if posicion_i != posicion_j and letras_intento[i] == letras_palabra_secreta[i]:
                lista_pistas.append("*")
                
        
    print("-----------------------------------------------------------------------------------------------------------")       
    print(f"PISTA: {letras_intento[0]}{lista_pistas[0]}-{letras_intento[1]}{lista_pistas[1]}-{letras_intento[2]}{lista_pistas[2]}-{letras_intento[3]}{lista_pistas[3]}-{letras_intento[4]}{lista_pistas[4]}")    
    
    a += 1
    intentos += 1