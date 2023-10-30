# Packing y unpacking
var = (1, 2, 3, 4, 5)

# las tuplas permiten utilizar la estructura empaquetada y desempaquetarla en varias variables

num1, num2, num3, num4, num5 = var
print(num1, num2, num3, num4, num5)
# nota: al hacer umpacking las variables deben coincidir con los elementos de la tupla

# Podemos devolver varios elementos en una funcion


def func():
    return 5, 6


ret1, ret2 = func()
print(ret1, ret2)


