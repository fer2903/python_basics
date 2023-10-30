# sentencias break, continue y pass

# break es una palabra resetvada
# se usa para terminar de manera inmediata la ejecucion de una estructura de control de flujo
# rompera laejecucion incluyendo el metodo else

lista = ['rojo', 'verde', 'morado']
for color in lista:
    print(color)
    break
print("salio del for")

num = 5
while num > 0:
    print(num)
    num -= 1
    break
print('salio del while')


# Continue
# la palabra continue es una palabra resetvada
# a diferencia de break esta no termina con la ejecucion de la iteracion
# unicamente termina con la ejecucion de la iteracion actual

colores = ['rojo', 'verde', 'morado']
for color in colores:
    if color == 'rojo':
        continue
    print(color)


# Pass
# nos permite definir el esqueleto
# de diferentes estructuras de diferentes tipos de funciones
# (funciones, if, while,for, etc...)
# omite la sentencia

def funcion():
    pass


for color in colores:
    # aqui voy a hacer algo que aun no se
    pass