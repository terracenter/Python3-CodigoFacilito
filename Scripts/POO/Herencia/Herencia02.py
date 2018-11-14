#TEMA: HERENCIA MULTIPLE

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
    nombre = '' #Todas las mascotas necesitan un nombre

    def mostrarNombre(self):
        print(self.nombre)

class Gato(Felino, Mascota):
    def gatoCazador(self):
        self.cazar()



####################################################################
gato = Gato()
gato.nombre = "Gato con Nombre"
gato.mostrarNombre()
