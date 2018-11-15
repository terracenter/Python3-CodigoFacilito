#En el __init__ Tambien se puede poner logica, constantes
################################################################
from .gato import Gato


################################################################
def creadorGatos(nombre):
    return Gato(nombre)