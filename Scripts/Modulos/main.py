#Importamos el archivo que nos ayudara
import Calculadora

#Lo usamos
resultado = Calculadora.suma(30, 45)
print(resultado)
print()

###########################################################################
from Calculadora import suma
from Calculadora import resta as r1

resultado = suma(30, 45)
print(resultado)
resultado = r1(30, 45)
print(resultado)
print()
print()
print()
###########################################################################
#Importa los objetos de Calculadora
from Calculadora import *

###########################################################################
#Si es el script principal, es decir el que se esta ejecutando siempre se llamara __main__
from Calculadora import __name__ as __name__calculadora
print(__name__)
print(__name__calculadora)

