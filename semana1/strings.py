# String cadenas de texto
# sintaxys
var = 'esto es un string'

# indexacion
print(var[0])

# indexacion inversa se comienza por -1
print(var[-1])

# slicing
# desde el caracter 0 hasta el 8
print(var[0:8])

# lee desde el caracter -9 hasta el final del string
print(var[-9:])

# lee desde el 9 hasta el final
print(var[9:])

# ######### Stride
nombre = "Fernando Vargas"

# leera de 0 a 8 en saltos de 2 en 2
print(nombre[0:8:2])

# leer del 0 al 1  podemos dejar el primer valor vacio

print(nombre[:8:1])

# leer del 0 al 8 en saltos de 3
print(nombre[:8:3])

# #### modificacion en python

# los strings son inmutables no se pueden modificar los strings

# Strings multiples lineas

multilinea = """Fernando 
Vargas"""
print(multilinea)