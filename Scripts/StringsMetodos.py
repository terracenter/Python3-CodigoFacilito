#Un String puede realizar ciertas cosas
course = 'Curso'
myString = 'Codigo Facilito!'

""" Metodos de Formato """

#Concatenar a traves de format
result = '{} de {}'.format(course, myString)
print(result)
print()

result = '{a} de {b}'.format(a=course, b=myString)
print(result)
print()


#Todo el String en minusculas
result=result.lower()
print(result)
print()

#Todo el String en Mayusculas
result=result.upper()
print(result)
print()

#Pone el String como un Titulo
result=result.title()
print(result)
print()


""" Metodos de Busqueda """

#Busca la posicion de una subcadena en un cadena, si no esta regrsa -1
result=result.lower()
pos = result.find('codigo')
print(result)
print(pos)
print()

#Cuantas veces se repite una subcadena
count = result.count('c')
print(count)
print()


""" Metodos de Remplazo """

#Remplaza una subcadena por otra
newString = result.replace('c', 'x')
print(newString)
print()

#Split divide las cadenas, de acuerdo un parametro, en este caso un espacio
newString = result.split(' ')
print(newString)