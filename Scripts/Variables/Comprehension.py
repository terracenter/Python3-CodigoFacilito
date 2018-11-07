#Es un tipo de feature, permite crear listas, tuplas y diccionarios muy simples

"""
Estructura -> Se puede extender
lista = [ valor agregar  for]
"""

##########################################################################
print("Ejemplo #1 - Creacion de lista con los numeros del 0 al 101")
lista = [valor for valor in range(0,101)]
print(lista)
print()
print()


##########################################################################
print("Ejemplo #2 - Creacion de lista con los numeros pares del 0 al 101")
lista = [valor for valor in range(0,101) if valor % 2 == 0]
print(lista)
print()
print()

##########################################################################
print("Ejemplo #3 - Creacion de tupla con los numeros impares del 0 al 101")
tupla = tuple(valor for valor in range(0,101) if valor % 2 == 1)
print(tupla)
print()
print()

##########################################################################
print("Ejemplo #4 - Creacion de diccionario a partir de una lista")
diccionario = { indice:valor for indice, valor in enumerate(lista)}
print(diccionario)
print()
print()

