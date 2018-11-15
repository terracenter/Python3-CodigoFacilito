class TinyIntError(Exception):
    pass

##########################################################################################
def tinyInt(val):
    return (val>=0) and (val<=255)


##########################################################################################
try:
    numero = 400
    if tinyInt(numero):
        print("El numero es correcto")
    else:
        raise TinyIntError("Este es un mensaje para los numero que no son TinyInt")

except TinyIntError as error:
    print(error)
    print("No es posible completar la operacion")