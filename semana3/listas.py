# listas
# las listas respetan el orden

lista1 = ["t1", 't2', 't3']
print(lista1)

# podemos utilizar los operadores en las listas

lista2 = ['t1', 't2', 't3']
print(lista1 == lista2)

print('t1' in lista2)

print(lista1 is lista2)

# las listas comparten propiedades con el string
# indexing
lista3 = ['texto1', 'texto2', 'texto3', 'texto4']
print(lista3[1])
print(lista3[-1])

# slicing

print(lista3[2:3])
print(lista3[:3])
print(lista3[2:])

# stride

print(lista3[0:3:2])
print(lista3[::-1])  # este metodo revierte la lista


# operaciones con listas

# suma

lista4 = [1, 2, 3]
lista5 = [4, 5 , 6]
suma = lista4 + lista5
print(suma)

# multiplicacion
multi = lista4 * 2
print(multi)

# tamaño

tamano = len(lista4)
print(tamano)

# min

minimo = min(lista4)
print(minimo)

# max

maximo = max(lista4)
print(maximo)

# las listas son mutables
###########################################

# modificacion simultanea

lista_simultanea = ["texto1", "texto2", 'texto3']
lista_simultanea[0:3] = [1, 2, 3]
print(lista_simultanea)  # [1, 2, 3]
