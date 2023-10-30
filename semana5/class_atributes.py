
"""
como bien sabemos todos los coches son distintos por lo que
la velocidad no aplica para todos
por lo que se necesita un atributo de instancia
estas variables se definiran en el metodo constructor
__init__()
nombre_objeto.nombre_atributo_instancia
"""
# Metodo __init__()
# python ejecuta automaticamente al instanciar una clase basada en esta clase
# asigna variables especificas del objeto


class Coche:
    def __init__(self, vel_max, consumo):
        self.velo_max = vel_max
        self.consumo = consumo

    def velocidad(self):
        print(self.velo_max)

    def consumo_medio(self):
        print(self.consumo)


bmw = Coche(200, 20)

print(bmw.velocidad())

print(bmw.consumo_medio())
