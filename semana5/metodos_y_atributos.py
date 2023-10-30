# Metodos y atributos
# que son los metodos
# cuando una funcion forma parte de una clase se le denomina "Metodo"

class Coche:

    def velocidad_maxima(self):
        """Este metodo devuelve la velocidad maxima del coche"""
        print("valocidad maxima")


coche1 = Coche()  # al instanciar la variableself toma todo lo relacionado a coche1
print(coche1.velocidad_maxima())  # imprimira la sentencia
