"""
Estructura if -> es importante la tabulacion
if condicion:
	bloque a ejecutarse #Debe tener una tabulacion
else:
	bloque a ejecutarse #Debe tener una tabulacion
"""	
fruta = 'kiwi'

##############################################################
print("Ejemplo #1 - If Basico")

if fruta=='kiwi':
	print("El valor es kiwi")
else:
	print("No son iguales")

print()
print()



##############################################################
print("Ejemplo #2 - If Reducido")	
mensaje = 'El valor de kiwi' if fruta == 'kiwi' else 'No son iguales'
print(mensaje)
print()
print()



##############################################################
#Entre el if y el else, podemos poner una infinidad de elif
print("Ejemplo #3 - Elif") 
fruta = 'manzana'

if fruta=='kiwi':
	print("El valor es kiwi")
elif fruta == 'manzana':
	print("El valor es manzana")
else:
	print("No es ni kiwi, ni manzana")	
print()
print()

##############################################################
#Pass nos permite que una condicion no haga nada
print("Ejemplo #4 - Pass") 
fruta = 'limon'

if fruta=='kiwi':
	print("El valor es kiwi")

elif fruta == 'manzana':
	print("El valor es manzana")

elif fruta =='limon':
	pass

else:
	print("No es ni kiwi, ni manzana")	

print()
print()

##############################################################
"""
Podemos usas >, <, <=, >=, ==, !=
True = 1 
False = 0
	-En python todas las variables tiene un "valor" boleano
		-Todas las variables vacias o nulas, tendran un valor de False
			-[], (), {}, 0, None -> Son False
			-valor = None -> Permite determinar	que una variable no tiene valor
		-Todas las variables con alguin tipo de valor, seran True.
"""
##############################################################

##############################################################
print("Ejemplo #5 - Condiciones anidadas")
valor01 = 1
valor02 = 21

print("Usando and")
if valor01 > 5 and valor02 > 20:
	print("Es verdad")
else:
	print("No es verdad")	
print()

print("Usando or")
if valor01 > 5 or valor02 > 20:
	print("Es verdad")
else:
	print("No es verdad")	
print()





