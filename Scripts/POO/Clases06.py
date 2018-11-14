#TEMA: METODOS ESTATICOS

########################################################
class Circulo:
    @staticmethod
    def pi(): #Metodo Estatico -> Le pertenece a la clase
        return 3.1416

    def __init__(self, radio):
        self.radio = radio

    def area(self): #Metodos de Instancia
        return self.radio * self.radio * self.pi()


########################################################
print(Circulo.pi())
print()

circulo01 = Circulo(7)
print(circulo01.area())
