#Los generadores permiten crear objetos sin necesidad de almacenarlos en la memoria RAM

##################################################
def generador(*args):
    for valor in args:
        yield valor*10

for valor in generador(1,2,3,4,5,6,7,8,9):
    print(valor)

print()
print()
##################################################
def generador02(*args):
    for valor in args:
        yield valor*10, True

for valor01, valor02 in generador02(1,2,3,4,5,6,7,8,9):
    print(valor01, valor02)
