#Parentisis cuadrados significa listas
#Soporta cualquier tipo de datos.
myList = ["String", 15, 15.6, True]
print(myList)
print()
print()

#Pueden crecer o decrecer
#Agregar
myList.append(6) #Lo colca en la parte final
print(myList)
print()
print()

myList.insert(1, "Insert") #Agrega un elemento en una posicion dada
print(myList)
print()
print()

print(myList[1]) #Acceder a un elemento
print()
print()

#Eliminar
myList.remove(6) #Elimina el 6
print(myList)
print()
print()

#Ultimo valor
lastValue = myList.pop()
print(myList)
print(lastValue)
print()
print()

#Ordenar solo entero
myListInteger = [1,5,4,2,4,5,6]
print(myListInteger)
myListInteger.sort()
print(myListInteger)
print()
print()

#Como unir dos listas
myList01 = [1, 2, 3, 5]
myList02 = [11, 21, 31, 51]
myList01.extend(myList02)
print(myList01)
print()

#Una lista puede almacenar otra lista.