# Funcion Sigmoid
from math import e
"""
viene determinada por la siguiente expresión matemática:

    f(x)= 1/(1 + e^-x)
"""

"""
 Crea una función en Python que calcule el resultado de aplicar la función Sigmoid sobre una entrada x.
 Ten en cuenta que x debe ser considerado un valor numérico.
"""


def sigmoid(x):
    s = 1/(1 + e**(-x))
    return s


s = sigmoid(10)
print(s)