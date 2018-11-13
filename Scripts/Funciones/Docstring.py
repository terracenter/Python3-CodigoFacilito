#Documentar funciones
#Siempre se documenta en la primera linea dentro de la funcion
########################################################################################
def generador(*args):
    """ Recibe n cantidad de numeros y regresa el numero \n ademas de regresar true o false si el numero es mayor a 5
    """
    for valor in args:
        yield valor, True if valor > 5 else False


########################################################################################

nombre = generador.__name__
documentacion = generador.__doc__
print(nombre, ":")
print(documentacion)
print()
print()

########################################################################################


