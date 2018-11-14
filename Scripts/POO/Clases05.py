#TEMA: PROPERTIES

###########################################################################

class Usuario:
    def __init__(self, usermane, password, email):
        self.username = usermane
        self.__password = self.__generarPassword(password) #Atributo Privado
        self.email = email

    def __generarPassword(self, password): #Metodo Priavdo
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__generarPassword(valor)

###########################################################################

camilo = Usuario('Camilo', 'Camilo123', 'cgil@unal.edu.co')
print(camilo.password)
camilo.password = "Nueva Contraseña"
print(camilo.password)
