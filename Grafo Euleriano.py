# -*- coding: utf-8 -*-
from graphviz import Graph as gr

grafo = gr('G', filename='euleriano.gv', engine='circo')
aristas = int(input('Cantidad de aristas que tiene su grafo: '))

def euler(pdf):
  visitados = [] 
  cola = []
  ciclos = 0
  ContadorNodosAgregados = 0
  caminos = 0
  acumulador = 0
  nodos_pares = 0

  for nodoinicial in range(aristas):
    nodoinicial = input('Ingrese nombre para el nodo inicial: ')
    grafo.attr('node', shape='doublecircle')
    
    grafo.node(nodoinicial)
    
    nodo_llegada = input('Nombre un nodo para conectarlo con el anterior: ')
    grafo.edge(nodoinicial, nodo_llegada)

    if aristas >= 1:
      cola.append(nodoinicial)
      ContadorNodosAgregados += 1

  for indice in range(len(cola)):
    actual = cola[indice]
    for j in range(len(cola)):
      if actual == cola[j]:
        nodos_pares += 1
  if nodos_pares > len(cola):
    ciclos += 1

  for elementos in range(len(cola)):
    if (cola[elementos] == nodo_llegada or nodoinicial):
      acumulador += 1

  if acumulador >= len(cola):
    caminos += 1

  visitados.append(ContadorNodosAgregados)
  grafo.attr(label=r'\n\nGrafo Euleriano\n Juan Pablo prueba', fontsize= '10')
  grafo.view()

  print("Los elementos de la cola son los nodos: ", cola)
  print("La cantidad de nodos visitados es de: ", visitados)
  print("La cantidad de ciclos encontrados es de: ", ciclos)
  print("La cantidad de caminos encontrados es de: ", caminos)

print(euler(grafo))
