# Operadores logicos

"""
Operador|||ejemplo|||significado
not    ||| not x   ||| True if x is False
                        False if x is true

or     ||| x or y  ||| True if either x  or y is True
                        False otherwise
and    ||| x and y ||| True if both x and y are True
                        False otherwise
"""

# Ejemplos
# not
num = 5
num2 = 10
print(not num < 10)

# Or

print((num < 4) or (num2 > 5) or (num < 10))

# and

print(num < 5 and num2 > 5 )

