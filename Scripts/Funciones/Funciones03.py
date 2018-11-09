#Podemos crear una funcion que puede recirbir n cantidad de argumentos
#Lo recibe en una tupla

def suma(*args):
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    return resultado

resultado = suma(12,12,324,21412)
print(type(resultado)) #Type me devuelve el tipo de la variable
print(resultado)
print()
print()

#################################################################
#Puede recibirlo en forma de diccionario
def mostrarDatos(**kwargs):
    print(kwargs)


print(mostrarDatos(valor="Camilo", edad=23))




