#Hereda  los metodos publicos, los privados no

####################################################################
class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal): #Clase Padre
    @property
    def garrasRetactiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")


class Gato(Felino): #Clase Hija
    def gatoCazador(self):
        self.cazar()


class Jaguar(Felino): #Clase Hija
    pass

####################################################################
gato = Gato()
jaguar = Jaguar()

print(gato.garrasRetactiles)
print(jaguar.garrasRetactiles)
print()
print()
print()


gato.cazar()
jaguar.cazar()
print()
print()
print()


gato.gatoCazador()
print()
print()
print()


print(gato.terrestre)
print(jaguar.terrestre)