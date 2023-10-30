# diccionarios
"""
los diccionarios son un tipo de dato complejo en python
contendra una coleccion de elementos clave, valor
asocia la clave con un valor determinado
"""

# se definniran como dict

diccionario = {
    'nombre': 'fernando',
    'apellido': 'vargas',
    'pais': 'mexico'
}

print(diccionario)

dic2 = dict(
    nombre="fernando",
    apellido="vargas",
    pais="mexico"
)
print(dic2)

# Accesar a los elementos
# los diciconarios acceden usando el nombre de la clave entre corchetes

print(diccionario["nombre"])
print(diccionario["pais"])

# se puede definir como clave una tupla por ejemplo

dic_tuple = {
    ("uno", 1): "one",
    ("dos", 2): "two",
    ("tres", 3): "three"
}
print(dic_tuple)
print(dic_tuple[("dos", 2)])


# son estructuras que pueden ser modificadas y no respetan el orden de los elementos
# ya que se accede a travez de las claves
# son objetos mutables

diccionario["nombre"] = "pedro"
diccionario["apellido"] = "ramos"
print(diccionario)

# se pueden añadir mas elementos

diccionario["edad"] = 29
print(diccionario)

# nota: no se pueden tener dos claves con el mismo nombre
# se quedara con la ultima clave repetida


# operaciones con diccionarios

dict_op = {
    "key1": "value1",
    'key2': 'value2'
}

dict_op2 = {
    'key3': 'value3',
    'key4': 'value4',
}
print(dict_op is dict_op2)
print(dict_op == dict_op2)
# no se pueden sumar
# no se pueden multiplicar
