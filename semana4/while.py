# sentencia while

"""

la sintaxis utilizada es la siguiente
while expresion:
    sentencias

El bucle while nos permite repetir infinitamente un bloque de codigo
sentencias = el bloque de codigo a ejecutar
expresion = el resultado de esta evaluacion debe ser true o false para salir

Al igual que en for se puede utilizar la sentencia else
"""
num = 10
while num > 0:
    num -= 1
    print(num)
else:
    print(' salio del bucle')

# nota: debemos considerar verificar que las condiciones secumplan para que pueda salir

# se pueden usar palabras clave para poder cortar un bucle

# while en una sola linea
num2 = 10
while num2 > 0: num2 -=1; print(num2)
