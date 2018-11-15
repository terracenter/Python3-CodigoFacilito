#En el __init__ Tambien se puede poner logica, constantes
#__init__ animals
################################################################
from .felinos import Gato
from .felinos import Leon

################################################################
def creadorGatos(nombre):
    return Gato(nombre)