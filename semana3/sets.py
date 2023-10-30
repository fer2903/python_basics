# que son los sets en python

""""
Son un tipo de datos que permite guardar
multiples elementos en una misma variable
A diferencia de las listas y las colecciones de los elementos
que forman un set
"""
"""
No se pueden indexar
No respeta orden
Mo puede contener valores duplicados
"""

mi_set = {'rojo', 'verde', 'azul'}
print(mi_set)

# funcionamiento
"""regularmente es utilizado para eliminar duplicados
implementar operaciones matematicas como la interseccion de dos conjuntos"""

mi_set = {'rojo', 'verde', 'azul'}

# caso comun

lista = ['rojo', 'verde', 'azul', 'rojo', 'rojo']

#casting

clean_set = set(lista)
print(clean_set)

lista_unicos = list(clean_set)
print(lista_unicos)

# frozenset

"""
    Al usar frozen set es similar a set pero en este caso es inmutable
"""
fset = frozenset({'rojo', 'verde', 'azul'})
print(fset)