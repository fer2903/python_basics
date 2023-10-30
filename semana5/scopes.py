# scope
# El scope es una region de un programa de python donde un Namespace es directamente accesible
# En python existen diferentes scopes desde los que se pueden acceder a los namespaces
# con algunas particularidades


# El scope local o de funcion

def func():
    var_local = 10
    print(var_local)


func()

# Scope no local
# solo para funciones anidadas


def funcnl():
    var_no_local = 10
    print('Namespae func', locals())

    def funcnl2():
        var_no_local_2 = 5
        print('Namespae func', locals())
    funcnl2()


funcnl()
# La variable var_no_local es visible desde el codigo funcnl2
# pero la variable var_no_local_2 no es accesible desde funcnl


# Scope global
# es el ambito superior de un programa

var_global = 15


def func3():
    print(var_global)


func3()


# Scope por defecto es accesible desde cualquier parte del programa
# el scope global es superior a todos los demas ambitos

# ejemplo: True

print(True)


# importante: Los nombres que se encuentran en un scope determinado
# puede ser accedido desde un scope externo pero no pueden ser actualizados o modificados
# a menos que se usen las siguientes sentencias

# global y nonlocal
# utilizando global y nonlocal podremos modificarlo solo si lo necesitamos

contador = 0


def actualizar_contador():
    global contador
    contador +=1


actualizar_contador()
print(contador)  # contador sera  = 1


# nonlocal

def funcion():
    coontador = 0

    def actualizar():
        nonlocal coontador
        coontador += 1
    actualizar()
    print(coontador)


funcion()
