# que es el noneType
""""
La palabra clave None se utiliza para definir una variable nula o un objeto vacio
None es un objeto de la clase NoneType
"""


def func():
    return


print(func())
print(type(func()))

# se puede asignar

var = None
print(var)
print(type(var))

# funcionamiento None
"""
None no es lo mismo que False
None no es 0 
None no es un string vacio
Comparar None con cualquier cosa excepto con None
"""

var2 = None
print(var2 is False)
print(var2 is True)
print(var2 == False)
print(var2 == 0)
print(var2 == "")
print(var2 == None)

