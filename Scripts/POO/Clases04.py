########################################################
class Circulo:
    _pi = 3.1416 #Es una variable de clase -> No hay nesecidad de crear instancias

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * Circulo._pi

########################################################
print(Circulo._pi)
print()
print()
#Puedo modificar la Variable de clase
#_Variable -> Indica que no se debe cambiar el valor de esa Variable

#Instanciando la clase circulo
circulo01= Circulo(3)
circulo02= Circulo(4)
print(circulo01.radio)
print(circulo02.radio)
print()
print()

#print(circulo01.__dict__) #->Retorna diccionario con los atributos de circulo01

#Metodo usando la variable de clase
print(circulo01.area())