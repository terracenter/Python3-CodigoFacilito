#Las clases deben comenzar con mayuscula y  CamellCase

#################################################################

class Lapiz:
    #Atributos -> Variables
    color = 'Amarillo'
    contieneBorrador = False
    usaGrafito = True

    #Metodos -> Atributos
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
lapizGenrico = Lapiz()
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

lapizGenrico.contieneBorrador = True
lapizGenrico.borrar()


