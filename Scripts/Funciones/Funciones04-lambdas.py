#Funciones Anonimas en una sola linea de codigo
miFuncion = lambda num01, num02: num01 + num02
resultado = miFuncion(10, 20)
print(resultado)
print()

######################################################################
formato = lambda sentencia : '¿{}?'.format(sentencia)
resultado = formato('Puedes hacer esto una pregunta')
print(resultado)
print()

######################################################################
noValor = lambda : 10
resultado = noValor()
print(resultado)
print()