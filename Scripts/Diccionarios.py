#Permite almacenar diferentes tipos de datos
#El diccionario no accede a los datos por medio de un indice, para ello usa una clave


#Un diccionario
#La estructura es {'clave':valor}
print("Ejemplo #1")
myDiccionario = {'a':55}
print(myDiccionario)
print()
print()

#Las claves deben ser datos inmutable (string, entero o tuplas)
print("Ejemplo #2")
myDiccionario = {'a': True, 5:"Hola mundo", (1,4):False}
print(myDiccionario)
print()
print()

#Si hay dos claves iguales devuelve la que este de ultimas
print("Ejemplo #3")
myDiccionario = {'a': True, 5:"Hola mundo", (1,4):False, 'a':False}
print(myDiccionario)
print()
print()


#Los Diccionarios pueden crecer o decrecer
print("Ejemplo #4")
print(myDiccionario)
myDiccionario ['c'] = 'Nuevo String' #Añade una clave - valor
print(myDiccionario)
print()
print()


print("Ejemplo #5")
print(myDiccionario)
myDiccionario ['a'] = 34 #Modifica un valor
print(myDiccionario)
print()
print()

#En resumen si la clave no esta la agrega, si esta la modifica

#Acceder a los valores del diccionario
print("Ejemplo #6")
print(myDiccionario)
valor = myDiccionario['a']
print(valor)
print()
print()

#Si la clave no existe, arroja error, para evitar esto hacemos lo sigiente
print("Ejemplo #7")
print(myDiccionario)
valor = myDiccionario.get('z', False) #Regresara false si no esta la clave
print(valor)
print()
print()

#Eliminar los valores
print("Ejemplo #8")
print(myDiccionario)
del myDiccionario[5] #Eliminar la clave 5 y su valor
print(myDiccionario)
print()
print()

#Solo mirar las llaves
print("Ejemplo #9")
print(myDiccionario)
claves = myDiccionario.keys() #Regresa un objeto iterable todas las claves
print(claves)
print()
print()

print("Ejemplo #10")
print(myDiccionario)
claves =  list(myDiccionario.keys()) #Regresa un objeto iterable y lo convertimos alista
print(claves)
print()
print()

#Solo los valores
print("Ejemplo #11")
print(myDiccionario)
values = myDiccionario.values() #Regresa un objeto iterable todas las claves
print(values)
print()
print()

print("Ejemplo #12")
print(myDiccionario)
values =  tuple(myDiccionario.keys()) #Regresa un objeto iterable y lo convertimos a tupla
print(values)
print()
print()

#Unir diccionarios
print("Ejemplo #13")
myDiccionario02 = {'z':33, 'w':68}
print(myDiccionario)
print(myDiccionario02)
myDiccionario.update(myDiccionario02) #añade el diccionario 2 al 1
print(myDiccionario)
print()
print()