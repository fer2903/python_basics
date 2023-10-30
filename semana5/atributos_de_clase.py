# Atributos de clase

# Definir variables
# cuando se define una variable se denominara atributo
# atributos de clase y atributos de instancia

"""Atributos de clase:
Los atributos de clase son variables que pertenecen a la clase y van a estar compartidas entre todos los objetos
que se instancien apartir de esa clase

<nombre_objeto>.<nombre_atributo_clase>

"""


class Coche:
    atributo_clase = 150
    def velocidad_maxima(self):
        """Este metodo devuelve la velocidad maxima del coche"""
        print('velocidad maxima', self.atributo_clase)  # para llamar la variable se necesita especificar self


renault = Coche()
print(renault.velocidad_maxima())
print(renault.atributo_clase)

bmw = Coche()
print(bmw.atributo_clase)
