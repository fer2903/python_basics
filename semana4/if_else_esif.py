# sentencia if, else, elif

"""
 if expresion:
    sentencia
 elif expresion2:
    sentencia
 else:
    expresion
"""

lista = ["azul", 'amarillo', 'verde']
if 'azul' in lista:
    print("entra al if")

tupla = (1, 2, 3, 4)
if 4 in tupla:
    print('entra a la tupla')


if 6 in tupla:
    print('entra a la tupla')
else:
    print('no esta en la tupla')


if 6 in tupla:
    print('entra al if')
elif 4 in tupla:
    print('entra a elif')
else:
    print('entra a else')

# en una sola linea

if 6 > 5: print('se encuentra en tupla'); print('sentencia2')

print('entra al if') if 6 > 5 else print('entra en else')
