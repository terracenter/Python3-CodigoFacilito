def validacion(num01, num02):
    return num01>0 and num02>0

def divison(num01, num02):
    if validacion(num01, num02):
        return num01/num02

resultado = divison(10,0)
print(resultado)
print()
print()

#######################################################################
def divison02(num01, num02):
    def validacion02():
        return num01 > 0 and num02 > 0

    if validacion02():
        return num01/num02

resultado = divison02(10,0)
print(resultado)
print()
print()

#######################################################################
#Funciones que crean funciones - CLOUSERS
def crearFuncion(num01, num02):
    def validacion():
        print("Se ejecuta validacion")
        return num01 > 0 and num02 > 0
    return validacion

nuevaFuncion = crearFuncion(10, -5)
#Algoritmo
print(nuevaFuncion())
print()
print()


#######################################################################
#Recibe como parametro una funcion
def aplicarFuncion(func):
    resultado = func()
    print(resultado)

nuevaFuncion = crearFuncion(10, 9)
aplicarFuncion(nuevaFuncion)

