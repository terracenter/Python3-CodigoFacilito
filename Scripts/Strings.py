#Una cadena es una lista de caracteres
#Solo se debe poner en dobles comillas el texto
myString = "Hola Mundo!" 
myString = 'Hola Mundo!'
print(myString)
print("\n")

myString = "Hola Mundo! 'Camilo' "
print(myString)
print("\n")

#Combinar Comillas Simples y Dobles
myString = 'Hola Mundo! "Camilo" '
print(myString)
print()

#Para el salto de linea 3 veces comillas simples o dobles

myString = """Hola Mundo! 
'Camilo' """
print(myString)
print()

# \n es el salto de linea
myString = """ \nHola Mundo! \n 'Camilo' \n"""
print(myString)
print()

course = "Python 3 " 
name = "Camilo"
finalMessage = course + name
print(finalMessage)
print()

#Forma 1° de Concatenar Cadenas
finalMessage = "Nuevo Curso de " + course + " por " + name
print(finalMessage)
print()

#Forma 2° de Concatenar Cadenas
finalMessage = "Nuevo Curso de %s por %s" %(course, name)
print(finalMessage)
print()

#Forma 3° de Concatenar Cadenas -> Es un metodo
finalMessage = "Nuevo curso de {} por {}".format(course, name)
print(finalMessage)
print()

print("Post Actualizacion")