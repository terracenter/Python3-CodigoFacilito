#TEMA: OVERRIDE
#A LA HORA DE EJECUTAR UN METODO PRIMERO BUSCA
#EN LAS CLASES QUE ESTA HEREDANDO DE IZQUIERDA A DERECHA
####################################################################
class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):
    @property
    def garrasRetactiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    nombre = '' #Todas las mascotas necesitan un nombre

    def mostrarNombre(self):
        print(self.nombre)


class Gato(Felino, Mascota):
    #Sobre escritura de __init__
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.nombre = nombre

    def gatoCazador(self):
        self.cazar()

    # Sobre escritura de metodos
    def mostarNombre(self):
        Mascota.mostrarNombre(self)
        print("El nombre del gato es : {}".format(self.nombre))


####################################################################
gato = Gato("Patricio")
gato.mostrarNombre()
