#String como array de caracteres
#Las listas comienzan en la posicion 0
myString = 'Curso de Codigo Facilito!'
print(myString)
print()

#Imprimir por caracteres
print(myString[0]) #Retorma C
print(myString[1]) #Retorma u
print(myString[16]) #Retorma F
print(myString[5]) #Los espacios cuentan como caracteres
print()

#Imprimir Cadena al Reves
print(myString[-1]) #Retorma !
print(myString[-2]) #Retorma o
print(myString[-10]) #Retorma _ Un espacio
print()


#Mostrar una Subcadena
print(myString[0:10]) #Imprime desde el caracter 0 hasta el 10
print(myString[5:12]) #Imprime desde el caracter 5 hasta el 12
print(myString[-2:-1]) #Imprime desde el caracter -2 hasta el -1
print()

#Saltos 
print(myString[0:10:2]) #Imprime desde el caracter 0 hasta el 10, Haciendo Saltos de 2
print()

#Cadena al Reves
print(myString[::-1]) #Imprime la cadena al reves :v