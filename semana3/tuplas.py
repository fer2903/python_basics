# tuplas
"""
las tuplas son objetos denticos a una lista
exepto que se encierran en parentesis
son tipos de datos inmutables
"""

tupla = (1, 2, 3, 4, 5)
print(type(tupla))
print(len(tupla))

# funcionamiento de las tupplas

tupla2 = (1, 2, 3, 't1', 't2', 't3')
# slicing
print(tupla2[0:3])

# cuando utilizar una tupla de una lista

"""
las tuplas son mas rapidas de ejecutar que una lista equivalente 
esto se da en datos grandes

Las tuplas son inmutables por lo que protegera a lo largo del programa por modificacion accidental

una tupla puede ser usada como clave en un diccionario

"""


# nota !!!!!
# se debe tener cuidado al definir una tupla con un solo tipo numerico
# ya que python puede interpretar los parentesis como notacion matematica
# tupla =  (5) resultara 5 como numero
# para definir una tupla con un solo elemento se definira
# tupla =  (5,)   resultara (5,)
