########################################################################
#Las variables dentro de la funcion se llaman locales, no pueden modiciar las globales
def palindromo(frase): 
	print(frase, "(Dentro - Antes)")
	frase = frase.replace(' ', '')
	print(frase, "(Dentro - Despues)")
	return frase == frase[::-1]

#Las variables fuera de la funcion se llaman globales
frase = 'anita lava la tina'
print(frase, "(Fuera - Antes)") #Antes de la funcion
resultado = palindromo(frase)
print(frase, "(Fuera - Despues)") #Despues de la funcion
print(resultado)	
print()
print()
print()
########################################################################






########################################################################
#Las funciones pueden acceder a variables globaes
def palindromo02(): 
	nuevaFrase = frase.replace(' ', '')
	return nuevaFrase == nuevaFrase[::-1]


frase = 'anita lava la tina'
resultado = palindromo02()
print(resultado)	
print()
print()
print()
########################################################################









#####################################################################
#No modifica el valor global
def valorGlobal():
	variableGlobal = "Cambiar Valor"

variableGlobal = "Esto es una funcion"
print(variableGlobal)	
valorGlobal()
print(variableGlobal)
print()
print()
print()
########################################################################








#####################################################################
#Modifica el valor global
def valorGlobal():
	global variableGlobal
	variableGlobal = "Cambiar Valor"

variableGlobal = "Esto es una funcion"
print(variableGlobal)	
valorGlobal()
print(variableGlobal)
print()
print()
print()
########################################################################






#####################################################################
#Para es facil, para editarlos una linea de mas
def valorGlobal():
	global variableGlobal
	variableGlobal = "Cambiar Valor"

def mostrarGlobal():
	print(variableGlobal)

variableGlobal = "Esto es una funcion"
mostrarGlobal()
valorGlobal()
mostrarGlobal()
print()
print()
print()
########################################################################






########################################################################
#Crear variables globales
def crearGlobal():
	global nuevaVariable
	nuevaVariable = "Es una nueva variable"


crearGlobal()
print(nuevaVariable)	

########################################################################