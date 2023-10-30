# Como vimos en el archivo clases y objetos
# es posible modificar las variables de instancia
# pero es considerado una mala practica
# debemos agregar dentro dela clase geters y seters

class Coche:
    """Esta clase representa un coche"""
    def __init__(self, modelo, potencia, consumo):
        """
        Inicializa los atributos de instancia
        Argumentos posicionales
        :param modelo: string que representa el modelo
        :param potencia: int que representa la potenciaen cv
        :param consumo: int que representa el consumo 1/100 km
        """
        # por convencion se debe agregar un quion bajo antes de la variable
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0

    def especificaciones(self):
        """Muestra las especificaciones del coche"""
        print(f'modelo: {self._modelo}')
        print(f'potencia: {self._potencia}')
        print(f'consumo: {self._consumo}')
        print(f'km actuales: {self._km_actuales}')

    def actualizar_kilometros(self, kilometros):
        """Esta metodo actualiza los kilometros del coche"""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:

            print(f'No se puede establecer un valor menor a kilometros actuales { self._km_actuales}')

    # extension de funcionalidad de nuestra clase
    def consumo_total(self):
        """Muestra el consumo total desde el km 0 """
        consumo_total = (self._km_actuales / 100) * self._consumo
        print(f'{consumo_total}')
        return consumo_total


mercedes = Coche('mercedes', '180', 7)
print(mercedes.especificaciones())
# actualizar a 1000 km
mercedes.actualizar_kilometros(1000)
print(mercedes.especificaciones())

# extension de funcionalidad de nuestra clase
mercedes.consumo_total()
