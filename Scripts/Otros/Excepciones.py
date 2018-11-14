#Es un error dentro del Script, al momento ejecutarlo
#Debemos manejarlo de la manera correcta, para evitar que el script colapse



####################################################################################

#Corre bien
print(2/10)
print("Se termino el Script")
print()
print()

#No corre bien
#print(2/0)
#print("Se termino el Script")
#print()

#Manejamos la Excepcion

try:
    print(2/0)
except ZeroDivisionError as ex:
    print(ex)
    print("No es posible dividir por 0")
    #Funciones, Clases, ect
print("Se termino el Script")
print()
print()
print()

####################################################################################
#Acceder a una posicion que no existe
try:
    lista = [1,2]
    print(lista[9])
except IndexError as ex:
    print(ex)
    print("No es posible acceder a la posicion 9")
print("Se termino el Script")
print()
print()
print()


####################################################################################
#Cuando no se el tipo de error uso Exception
#El bloque finally siempre se ejecuta sin importa si ocurre una excepcion o no
try:
    lista = [1,2]
    print(lista[9])
except Exception as ex: #Cuando Existe un error
    print(ex)
    print("No se que paso pero paso algo mal")
finally: #Siempre se ejecuta
    print("Se termino el Script")