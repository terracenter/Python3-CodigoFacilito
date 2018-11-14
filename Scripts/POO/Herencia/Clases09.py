#TEMA:CURIOSIDADES

#################################################################

class Usuario:
    def __new__(cls): #constructor
        print("Este metodo es el primero que se ejecuta")
        return super.__new__(cls)

    def __init__(self):
        print("Este metodo es el segundo que se ejecuta")
        self.__password = "Este es un secreto"

    def mostarPassword(self):
        print(self.__password)

    def __str__(self):
        return "Esto se imprime cuando inteto mostar el objeto"

    def __getattr__(self, nombre):
        print("Aqui mostramos que no se encontro el atributo")


#################################################################
#Metodos magicos __Metodo__
usuario = Usuario
print(usuario)
print(usuario.apellido)