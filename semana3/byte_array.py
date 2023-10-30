# byte array
"""
Tipo de dato de python
estos tipos de datos si son mutables

"""

cadena_bytes = bytearray(b'\x20\x19\x61\x62\x39\x40')
print(type(cadena_bytes))

print(cadena_bytes[3])

# en byte array si es posible modificar elementos
# para acceder a la modificacion requerimos usar slicing

cadena_bytes[0:1] = b'8'
print(cadena_bytes)

# ord() nos representara el valor entero que representa el valor unicode

unicode_to = ord('8')
print(unicode_to)

cadena_bytes[2] = ord('h')  # de esta forma si se podra asignar sin slicing
print(cadena_bytes)


# chr devolvera de un entero a unicode

print(chr(56))

# operaciones
cadena_bytes1 = bytearray(b'\x20\x19\x61')
cadena_bytes2 = bytearray(b'\x62\x39\x40')

suma = cadena_bytes1 + cadena_bytes2
print(suma)

multiplicacion = cadena_bytes1 * 2

# se pueden usar los mismos operadores que en bytes