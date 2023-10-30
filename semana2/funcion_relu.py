# Funcion de activacion ReLu

"""Crea una funcion en python que calcule el resultado de aplicar la funcion ReLu
sobre una entrada x , ten en cuenta que x debe ser considerado un valor numerico

    f(x)= max(0,x)
"""


def relu(x):
    return max(0, x)


re = relu(1000)
print(re)
