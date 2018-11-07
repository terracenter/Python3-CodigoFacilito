#Opera sobre condicionales 

"""
Estructura

while condicion:
	codigo
else:
	codigo

"""

##############################################
print("Ejemplo #1 - Ciclo Basico ")
contador = 0

while contador<10:
	print(contador)
	contador +=1
else:
	print("El While ha terminado")	

print()
print()


##############################################
#continue -> nos dice que el ciclo se siga ejecutando
#break -> rompe el ciclo de forma abruta
##############################################


##############################################
print("Ejemplo #2 - Continue - Break ")
contador = 0

while contador<10:
	print(contador)
	contador +=1

	if contador==5:
		continue
	if contador==6:
		break		
else:
	print("El While ha terminado")	

print()
print()


##############################################
print("Ejemplo #3 - Usando Banderas")
contador = 0
bandera=True

while bandera:
	print(contador)
	contador +=1

	if contador==5:
		continue
	if contador==6:
		bandera=False #Un break elegante
else:
	print("El While ha terminado")	

print()
print()