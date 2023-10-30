# Operadores de comparacion

"""
Operador|||ejemplo|||significado
   ==       a == b      Igual a
   !=       a != b      no igual a
    <       a < b       a menor que
   <=       a <= b      Menor que o igual a
   >        a > b       a mayor que
   >=       a >= b      Mayor que o igual a

"""

"""
 Al usar los operadores con strings
 caso <= o  >= se calcula por la representacion unicode
 verificamos con la funcion ord(caracter) devolvera el valor unicode 
 ejemplo: ord("a") devolvera 97
 para revertir chr(97)
 pero si usamos la funcion len(string) validara el tamaño de la cadena

 """


# operadores de identidad
"""
Operador|||ejemplo|||significado
 is        x is y     True si las dos variables son el mismo objeto
 is not    x is not y  True si las dos variables no son el mismo objeto
 

"""

# ejemplos
text1 = "Hola mundo"
text2 = "Hola mundo"

print(id(text1))
print(id(text2))

print(text1 is text2)  # este operador compara el contenido identificado mas no el contenido del string


# operadores de pertenencia
"""Los operadores de pertenencia se utilizan para evaluar si una secuencia se encuentra presente en un objeto 
Operador|||ejemplo|||significado
in          x in y     True si la secuencua x se encuentra presente en y 
not in     x not in y  True si la secuencia x no se encuentra presente en y  
"""

# ejemplo
texto = "Cadena de texto"
print(("texto" in texto))

print("b" in texto)