# Namespace: es un mapeo entre nombres y objetos
# tienen diferentes tiempos de vida
# Acceso a namespaces

# Este namespace pordefecto nunca se borra y contendra las palabras reservadas de python
print(dir(__builtins__))

# El namespace global
# para unmodulo se crea cuando se lee la definicion del modulo y normalmente dura
# hasta el interprete se cierra

# al definir esta variable
var_modulo = 10
# puedo accesar
print(globals())  # al final aparecera nuestra variable 'var_modulo': 10}

# namespace local
# se va a crear para una funcion o estructura que contenga un bloque de codigo
# seborraran al terminar el bloque de codigo


def funcion():
    var_local = 5
    print((locals()))


funcion()  # {'var_local': 5}
