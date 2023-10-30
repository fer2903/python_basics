# impelemntando la busqueda binaria

# Sea min = 0 y max = n-1.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def do_search(list_array, target_value):
    minimum = 0
    maximum = len(list_array) - 1
    count = 0
    # Si max < min, entonces detente: target no está en array. Regresa -1.
    while minimum <= maximum:
        count +=1
        # Calcula guess como el promedio de max y min, redondeado hacia abajo (para que sea un entero).
        guess = (minimum + maximum)//2
        if list_array[guess] == target_value:
            return guess, count
        elif list_array[guess] < target_value:
            minimum = guess + 1
        else:
            maximum = guess - 1
    return -1


print(do_search(primes, 97))