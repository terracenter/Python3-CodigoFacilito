#Un decorador permite añadir funcionalida a las funciones
#En si un decorador en una funcion que recibe como parametro una funcion y devuelve otra funcion

#A, B, C son funciones
#A recibe como parametro B para poder crear C


#################################################################
#Basico
def decorador(func):
    def nuevaFuncion():
        print("Vamos a ejecutar la funcion")
        #Agregar Codigo
        func()
        # Agregar Codigo
        print("Se ejecuto la funcion")

    return nuevaFuncion

@decorador #Nos indica para poder decorarla
def saluda():
    print("Hola mundo")

saluda()
print()
print()



##################################################################
#Para manejar argumentos tengo que realizar algunas modificaciones
def decoradorSuma(func):
    def nuevaFuncion(*args, **kwargs):
        print("Vamos a ejecutar la funcion")
        #Agregar Codigo
        func(*args, **kwargs)
        # Agregar Codigo
        print("Se ejecuto la funcion")

    return nuevaFuncion

@decoradorSuma #Nos indica para poder decorarla
def suma(num01, num02):
    print(num01 + num02)

suma(12,12)
print()
print()



#################################################################
#Trabajar con retorno de valores

def decoradorSuma02(func):
    def nuevaFuncion(*args, **kwargs):
        print("Vamos a ejecutar la funcion")
        resultado = func(*args, **kwargs)
        print("Se ejecuto la funcion")
        return resultado

    return nuevaFuncion

@decoradorSuma02 #Nos indica para poder decorarla
def suma02(num01, num02):
    return (num01 + num02)

resultado = suma02(2,232)
print(resultado)
print()
print()

#################################################################
#Los decoradores tambien reciben parametro
def decorador02(isValid):
    def decorador03(func):
        def beforeAction():
            print("Vamos a ejecutar la funcion")

        def afterAction():
            print("Se ejecuto la funcion")

        def nuevaFuncion(*args, **kwargs):
            if isValid:
                beforeAction()

            resultado = func(*args, **kwargs)
            afterAction()
            return resultado

        return nuevaFuncion

    return decorador03


@decorador02(isValid = False)
def multiplicacion(num01, num02):
    return num01 * num02

resultado = multiplicacion(98, 12)
print(resultado)
print()
print()