# numeros en python
# pythontiene 3 tipos de numeros: int, float y complejos

num = 10

# Casting : transformacion de un  tipo a otro tipo de dato

num_str = '10'
num_cast = int(num)

# Para anumero grandes  Python no puede agregar el caracter "." o "," pero se puede agregar _

large_number = 1000000

large_number_with_separator = 1_000_000

# en python no hay limite de tamaño de un numero

extra_large_numbre = 10000000000000000000000000000000000000000000000000

# numeros flotantes

float_number = 10.5

# Casting

str_float_number = '10.5'
cast_float_number = float(str_float_number)

# Practicidad
notacion_simple = 1_000_000.5

# notacion cientifica
cientific_number = 1e6

# los numeros flotantes si tienen limite el limite es 2e400

# ###############################
# Numeros complejos

complex_number = 1 + 2j
print(complex_number.real)
print(complex_number.imag)
