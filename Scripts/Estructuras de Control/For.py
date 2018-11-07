#Iteraciones determinadas
#Permite iterar objetos iterables (listas, tuplas, diccionario)

#############################
print("Ejemplo #1 - Recorre Listas")
lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
	print(valor)

print()
print()

################################
print("Ejemplo #2 - Funcion Range")
newRango = range(10) #Crea objeto iterable de 0 a 10

for valor in newRango:
	print(valor)

print()
print()


################################
print("Ejemplo #3 - Funcion Range #2")
newRango = range(5, 10) #Crea objeto iterable de 5 a 10

for valor in newRango:
	print(valor)

print()
print()	


################################
print("Ejemplo #4 - Funcion Range #3")
newRango = range(5, 25, 2) #Crea objeto iterable de 5 a 25, pero haciendo saltos de 2 en 2

for valor in newRango:
	print(valor)

print()
print()	


################################
print("Ejemplo #5 - Uso de indice")
lista = [1,2,3,4,5,6,7,8,9,10]

for indice, valor in enumerate(lista):  #Enumerate, regresa primero el indice y luego el valor
	print(valor, "tiene el indice", indice)

print()
print()	


################################
print("Ejemplo #6 - Uso de indice #2")
lista = [1,2,3,4,5,6,7,8,9,10]
#len regresa el tamaño de un objeto iterable en este caso la lista
for valor in range(0, len(lista)): #Un objeto iterable que nos regresa, los indices desde 0 hasta el tamaño de la lista
 	print(valor)

print()
print()	


################################
print("Ejemplo #7 - Recorrer String")

for valor in "Camilo Andres": #Imprimira cada elemento, es decir caracter por caracter
 	print(valor)

print()
print()	


################################
print("Ejemplo #7 - Recorrer diccionario")
diccionario = {'a':10, 'b':20, 'c':500}
for llave, valor in diccionario.items():
 	print("La llave", llave, "tiene el valor de",  valor)
print()
print()	



