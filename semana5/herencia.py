# que es la herencia en python
# la herencia se utiliza para crear jerarquia de clases relacionadas


"""
Tomando como base nuestra clase Coche

"""
# que pasaria si es un auto electrico


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
        self._combustible = '1/100km'

    def especificaciones(self):
        """Muestra las especificaciones del coche"""
        print(f'modelo: {self._modelo}')
        print(f'potencia: {self._potencia}')
        print(f'consumo: {self._consumo} {self._combustible}')
        print(f'km actuales: {self._km_actuales}')

    @property
    def kilometros(self):
        return self._km_actuales

    @kilometros.setter
    def kilometros(self, kilometros):
        """Esta metodo actualiza los kilometros del coche"""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:

            print(f'No se puede establecer un valor menor a kilometros actuales { self._km_actuales}')

    # extension de funcionalidad de nuestra clase
    def consumo_total(self):
        """Muestra el consumo total desde el km 0 """
        consumo_total = (self._km_actuales / 100) * self._consumo
        print(f'{consumo_total} {self._combustible}')
        return consumo_total

# definimos una clase Coche electrico al que heredaremos Coche


class CocheElectrico(Coche):
    """Esta clase representa un coche electrico """

    def __init__(self, modelo, potencia, consumo, bateria):
        """Inicializa los atributos de la clase padre"""
        super().__init__(modelo, potencia, consumo)
        self._combustible = "kwh/100km"
        # agregamos atributos propios
        self._bateria = bateria  # importamos el objeto

    def detalles_bateria(self):
        """Esta clase muestra los detalles de la bateria """
        self._bateria.especificaciones()

    # copiamos la funcion de la clase padre y la pegamos ya que tendra prioridad
    def consumo_total(self):
        """Muestra el consumo total desde el km 0 """
        consumo_total = (self._km_actuales / 100) * self._consumo
        print(f'{consumo_total} {self._combustible} kwh')


#tesla = CocheElectrico('model3', 300, 15, 50)
#print(tesla.especificaciones())
#print(tesla.detalles_bateria())

# sobreescribir metodos de la clase padre

#print(tesla.consumo_total())  # nos mostrara 0.0 kwh/100km kwh

# Objetos dentro de una clase


class Bateria:
    """Esta clase va a representar una bateria de un coche electrico"""
    def __init__(self, capacidad, tipo_pila, num_pilas, peso):
        self._capacidad = capacidad
        self._tipo_pila = tipo_pila
        self._num_pilas = num_pilas
        self._peso = peso

    def especificaciones(self):
        print(f'Capacidad {self._capacidad} kwh')
        print(f'Tipo de pilas {self._tipo_pila} ')
        print(f'Numero de pilas {self._num_pilas} ')
        print(f'Peso {self._peso} kg')


bateria_tesla = Bateria(80, 2170, 203_136, 480)
vocho = CocheElectrico('beettle', 450, 20, bateria_tesla)
print(vocho.detalles_bateria())