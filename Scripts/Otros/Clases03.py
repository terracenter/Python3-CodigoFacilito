# __atributo, indica que el atributo es privado
# __metodo, indica que el metodo es privado

###########################################################################

class Usuario:
    def __init__(self, usermane, password, email):
        self.username = usermane
        self.__password = self.__generarPassword(password) #Atributo Privado
        self.email = email

    def __generarPassword(self, password): #Metodo Priavdo
        return password.upper()

    def getPassword(self):
        return  self.__password
###########################################################################

camilo = Usuario('Camilo', 'Camilo123', 'cgil@unal.edu.co')
print(camilo.username)
print(camilo.email)
print(camilo.getPassword())