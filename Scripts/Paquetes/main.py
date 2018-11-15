#TEMA:PAQUETES

########################################################################
#from animals.gato import Gato -> Incorrecto sin editar el __init__

from animals import Gato #->Con el __init_ ya editado
from animals import creadorGatos
########################################################################
gato01 = Gato("Nuevo gato por paquete")
print(gato01.nombre)
print()
print()
print()

gato02 = creadorGatos("Dante")
print(gato02.nombre)
print()
print()
print()