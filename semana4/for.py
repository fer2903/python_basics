# sentencia for


"""
for variable in iterable:
    sentencias


iterable = es una coleccion de elementos, por ejemplo: lista o tupla
variable = es una variable que recibira uno de los elementos del objeto iterable

"""

lista = ['azul', 'verde', 'rojo']

for color in lista:
    print(color)

# para saber si una variable es iterable usamos la funcion iter()

iter(lista)


# iteradores son objetos dentro de python que devolvera valores 1 por 1

lista_itr = iter(lista)
print(lista_itr)  # <list_iterator object at 0x102ffe410>

# al usar next()

print(next(lista_itr))  # azul
print(next(lista_itr))  # verde
print(next(lista_itr))  # rojo
#print(next(lista_itr))  # retorna una excepcion

# ####### or particularidades
# un bucle for tambien puede tener clausula else
lista2 = ['azul', 'verde', 'rojo']

for color in lista2:
    print(color)
else:
    print('el bucle ya no tiene elementos')

# metodo range()

for n in range(0, 5):
    print(n)

# range se puede castear

list_range = list(range(0, 5))
print(list_range)

# se puede definir un rango

comun = list(range(0))
with_range = list(range(0, 50))
with_stride = list(range(0, 50, 2))

"""
Recomendacion no se recomienda hacer cast con lista ya que usa mas recursos
lo ideal es usarlo directamente en las estructuras de flujo directamente
"""
