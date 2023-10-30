# Funciones
# def nombre_de_la_funcion(parametros):
#     sentencias

def mi_funcion(arg1, arg2):
    print(arg1)
    print(arg2)


mi_funcion("Hola mundo", "Adios mundo")
# las funciones no necesariamente requieren de argumentos pero si es necesario que lleve los parenntesis vacios

# tipos de argumentos en las funciones

# argumentos pocicionales


def args_pocicionales(arg1, arg2):
    print(arg1)
    print(arg2)

# arguentos palabra clave


def args_clave(arg1, arg2):
    print(arg1)
    print(arg2)


args_clave(arg2="hola", arg1="adios")

# parametros por defecto u opcionales


def valor_por_defecto(arg1, arg2="hola"):
    print(arg1)
    print(arg2)

# la palabre return

# al ejecutar return python termina el proceso de la funcion


####### Ver biblioteca de funciones default para python

# ejemplo
var = "print('hola mundo')"
exec(var)
