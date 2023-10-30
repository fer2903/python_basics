# funcion Tanh
from math import e
# por definicion la tangente es igual a sen / cos

"""
Sinh
 sinh(x) = ((e^x ) - (e^-x)) / 2
"""
"""
Cosh
 cosh(x) = ((e^x ) + (e^-x)) / 2
"""
"""
Tanh
    tanh(x)= sinh(x)/cosh(x)
"""
""" Crea una función en Python que calcule el resultado de aplicar la función
    Tanh sobre una entrada x.
    Ten en cuenta que x debe ser considerado un valor numérico."""

def cosh(x):
    cos = ((e**x) + (e**-x))/2
    return cos


def sinh(x):
    sin = ((e**x) - (e**-x))/2
    return sin


def tanh(x):
    cos = cosh(x)
    sin = sinh(x)
    tan = sin/cos
    return tan


tan = tanh(10)
print(tan)