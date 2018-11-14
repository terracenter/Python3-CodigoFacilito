#TEMA: CURIOSIDADES

#################################################################
class Usuario:
    def __init__(self):
        self.__password = "Este es un secreto"

    def mostarPassword(self):
        print(self.__password)



#################################################################
#Crear atributos por fuera
usuario = Usuario()
usuario.nombre = "Camilo"
usuario.apellido = "Gil"
print(usuario.nombre)
print(usuario.apellido)
print(usuario.__dict__)
print()
print()
print()

#################################################################
#Atributos con el mismo nombre, pero diferente privacidad
usuario = Usuario()
usuario.__password = "Ya no es un secreto"
print(usuario.__password)
usuario.mostarPassword()
print(usuario.__dict__)
print()
print()
print()

