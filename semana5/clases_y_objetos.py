# definiendo una clase

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
        print(f'modelo: {self.modelo}')
        print(f'potencia: {self.potencia}')
        print(f'consumo: {self.consumo}')
        print(f'km actuales: {self.km_actuales}')


mercedes = Coche('mercedesc200', 180, 7)
print(mercedes.especificaciones())

# para modificar km actuales, pero es considerada una mala practica hacerlo de esta forma
#
mercedes._km_actuales = 200
print(mercedes.especificaciones())

# para ctualizar una variable por fuera es necesario agregar una funcion que actualice internamente
