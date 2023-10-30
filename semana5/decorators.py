# Decorators
"""
En convinacion con una clase puede ayudar a que el codigo sea mucho mas limpio

"""

# nos permite modificar el comportamiento
# realizando unacombinacion de todaslas propiedades que hemos visto anteriormente


def mi_funcion():
    print('hola mundo')


def mi_decorator(func):
    def wrapper():
        print("antes")
        func()
        print('despues')
    return wrapper()


#mi_decorator(mi_funcion)

# podemos utilizar decorators paramodificar el comportamiento
# por ejemplo , añadiendocondiciones que se evaluan antes de ejecutar la funcion ya existente

# syntactic sugar


@mi_decorator
def mi_function():
    print('hola mundo decorator')


mi_function()
