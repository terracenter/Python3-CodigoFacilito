##########################################################################################
class TinyIntError(Exception):
    def __init__(self):
        self.message = "El numero no cuenta con las caracteristicas de un TinyInt"

    def __str__(self):
        return self.message

##########################################################################################

def valideTinyInt(val):
    return (val>=0) and (val<=255)


def valideVal(val):
    try:
        return  isinstance(int(val), int)

    except ValueError as error:
        return False


def callBackFuntion():
    print("Esto se ejecuta cuando existe un error")


def tinyInt(val, callBack = None):
    try:
        if valideVal(val) and valideTinyInt(val):
            return True
        else:
            raise TinyIntError()

    except TinyIntError as error:
        if callBack is not None:
            callBack()
        else:
            print("Error")




##########################################################################################

print(tinyInt(40, callBackFuntion))