#TEMA: METODOS DE CLASE

#Los Metodos de clase pueden acceder a los atributos
# o metodos de la clase que se estan usando

############################################################

class Animal:
    colador = True

class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre): #Metodo de clase
        return Cocodrilo(nombre)

###########################################################################
cocodrilo = Cocodrilo.new("coco")
print(cocodrilo.nombre)

