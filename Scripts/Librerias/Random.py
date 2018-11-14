#Python tiene 3 librerias incluidas que son
import random

#Obtener numero al azar
valor = random.randint(0,10)
print(valor)
print()

#Selecionar elemento al azar de una lista
lista = [True, "Strings", 23, False]
valor = random.choice(lista)
print(valor)
print()

#Desordenar una lista
print(lista)
random.shuffle(lista)
print(lista)
print()
