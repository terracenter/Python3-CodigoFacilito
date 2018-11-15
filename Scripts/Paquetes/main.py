#TEMA:PAQUETES

########################################################################
#Incorrecto sin editar el __init__
#from animals.gato import Gato


#Con el __init_ ya editado
from animals import Gato
from animals import Leon
from animals import creadorGatos

########################################################################
gato01 = Gato("Nuevo gato por paquete")
print(gato01.nombre)
print(gato01.comer())
print()
print()

gato02 = creadorGatos("Dante")
print(gato02.nombre)
print()
print()
print()

leon01 = Leon("Alex")
print(leon01.nombre)
print()
print()
print()