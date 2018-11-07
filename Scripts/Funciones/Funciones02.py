####################################################
def suma(valor01, valor02, valor03):
	return valor01 + valor02 + valor03

def division(valor01, valor02):
	return valor01/valor02

def multiplicacion(valor01, valor02=1): #Valor por default
	return valor01*valor02

def multiplesValores(): #Esta funcion regresa varios valores, regresa una tupla
	return "String", 1, True, 23.6

def mostarResultado(funcion):
	print (funcion(6,8))


####################################################
print("Llamanos a la funcion suma")
resultado = suma(10, 20, 30)
print(resultado)
print()


####################################################
print("Llamanos a la funcion division")
resultado = division(valor02=10, valor01=100) #Diferente forma de pasar los parametros
print(resultado)
print()

####################################################
print("Llamanos a la funcion multiplicaion")
resultado = multiplicacion(6) #Valores por default 
print(resultado)
print()


####################################################
print("Llamanos a la funcion multiples valores")
resultado = multiplesValores()
print(resultado)
print()

####################################################
print("Llamanos a la funcion multiples valores #2")
string, entero, bol, floa = multiplesValores()
print(string)
print(entero)
print(bol)
print(floa)
print()



###################################################
print("Definir una variable a travez de una funcion")
miVariable = multiplicacion
resultado = miVariable(6,8)
print(resultado)
print()

###################################################
print("Llamanos a mostar resultado")
miVariable= multiplicacion
mostarResultado(miVariable)
