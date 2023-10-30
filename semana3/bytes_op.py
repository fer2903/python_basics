# bytes en python
"""
Un byte es una ubicacion de memoria con un tamaño de 8 bits
Un objeto inmutable de bytes conceptualmente similar a un string
"""
# estara representado por 2 digitos en hexadecimal

cadena_byte = b'\x02\x1f'  # 543

# verifiqcamos

binario = bin(543)  # "0b1000011111"
print(binario)

hexadecimaal = hex(543)
print(hexadecimaal)

print(int.from_bytes(cadena_byte, 'big'))


"""
Transformar tipos de datos diferentes a bytes
"""

texto = "hola mundo"
texto_bytes = b'hola mundo'
print(texto_bytes)

# nota: si lacadena de bytes puede interpretarlos como caracteres ascii imprimibles
# lo sacara por pantalla de esaforma

abc = b'\x41\x42\x43'
print(abc)  # b'ABC'


# acceso a los elementos de una cadena de bytes

cadena_bytes = b'\x20\x19\x61\x62\x39\x40'
print(cadena_bytes[0])

# slicing

print(cadena_bytes[2:5])  # b'ab9'

# stride

print(cadena_bytes[0:5:2])

# las cadenas son inmutables

# operaciones
cadena_bytes1 = b'\x20\x19\x61'
cadena_bytes2 = b'\x62\x39\x40'

suma = cadena_bytes1 + cadena_bytes2
print(suma)

multiplicacion = cadena_bytes1 * 2
print(multiplicacion)

print(cadena_bytes1 == cadena_bytes2)

print(cadena_bytes1 is cadena_bytes2)
