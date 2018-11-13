#!/usr/bin/python3
"""
Aqui va lo que hace el modulo
"""

__author__ = "Camilo Andres Gil Ballen"
__copyright__ = "Copyright 2018, Camilo S.A."
__credits__ = "Camilo S.A."

__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Camilo Andres Gil Ballen"
__email__ = "cgilb@unal.edu.co"
__status__ = "Developer"

def suma(num01, num02):
    return num01 + num02

def resta(num01, num02):
    return num01 - num02

def multiplicacion(num01, num02):
    return num01 * num02

def division(num01, num02):
    return num01 / num02

#Si un archivo se usa como modulo, no debe tener llamadas
#En la linea numero 1, debe ir el interprete correspontiente
#Luego ira la documentacion del modulo
#Por ultimo usamos metadatos

def saluda():
    print(__name__)

#Esta condicional me permite determinar si un Script se esta ejecutando como
#Documento principal o como un Script importado


if __name__ == '__main__':
    saluda()