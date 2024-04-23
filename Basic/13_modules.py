## MÓDULOS (librerias) ##

"""
import my_module
#import 10_functions #no se puede acceder porque no es válida la nomenclatura para los módulos

my_module.sumValue(3, 5, 7)
my_module.printValue('Hola Py')


from my_module import sumValue, printValue

sumValue(5, 6, 1)
printValue("Hola Py")
"""

# Modulos creados por el sistema

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE #le estamos dando un alias 

print(PI_VALUE)

