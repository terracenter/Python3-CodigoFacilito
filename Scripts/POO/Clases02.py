#Las clases deben comenzar con mayuscula y  CamellCase
#El metodo init es nuestro constructor
#################################################################

class Lapiz:
    #Atributos -> Variables

    #Metodos -> Atributos
    def __init__(self, color, contieneBorrador, usaGrafito):
        self.color = color
        self.contieneBorrador = contieneBorrador
        self.usaGrafito = usaGrafito

    def dibujar(self):
        print("El lapiz esta dibujando.")

    def borrar(self):
        if self.esValidoParaBorrar():
            print("El lapiz esta borrando.")
        else:
            print("No es posible borrar.")

    def esValidoParaBorrar(self):
        return self.contieneBorrador


#################################################################

#OBJETO = INSTANCIA
lapizGenrico = Lapiz('Azul', True, True)
print(lapizGenrico.color)
print(lapizGenrico.contieneBorrador)
print(lapizGenrico.usaGrafito)
print()
print()
print()


lapizGenrico.dibujar()
lapizGenrico.borrar()
print()
print()
print()





