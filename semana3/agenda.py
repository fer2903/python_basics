# Implementacion de una agenda

# Implementa la agenda digital y contactos

# seleccionar una estructura de datos
"""
Crea un diccionario que represente la agenda digital. Dentro de ese diccionario, crea otro diccionario por cada uno de los contactos que quieras almacenar en ella.
Los contactos deben tener, al menos, los siguientes atributos: Nombre, dirección, email y teléfono.
"""


agenda_digital_init = {
    'Fernando': {
        'direccion': 'madrid, 123',
        'email': 'ejemplo@ejemplo.com',
        'telefono': '55555555'
    },
    'juan': {
        'direccion': 'calle, 123',
        'email': 'ejemplo2@ejemplo.com',
        'telefono': '555555131255'
    }
}


def escribir_agenda(nombre_agenda, agenda_digital):
    """Escribe la agenda en un fichero de texto
        parametros posicionales
        nombre_agenda -- str que representa el nombre de la agendaen disco.
        agenda_digital -- dict que representa la agenda digital y los contactos
    """
    agenda_fichero = open(nombre_agenda, "w")
    # escibimos la agenda en el fichero
    agenda_fichero.write(str(agenda_digital))
    # cerramos fichero
    agenda_fichero.close()

# funcion que nos permita leer el fichero


def leer_fichero(nombre_agenda):
    """
    Lee la agenda en un fichero de texto
    :param nombre_agenda:
    :return:
    """
    # esta sentencia nos permite abrir el fichero deseado
    agenda_digital_lectura = open(nombre_agenda, 'r')
    # esta sentencia lee todos las lineas del fichero y las asigna a la variable  agenda digital
    agenda_digital_r = agenda_digital_lectura.readlines()
    # Esta sentencia cierra el fichero que has abierto con la funcion open()
    agenda_digital_lectura.close()
    return eval(agenda_digital_r[0])


def solicitar_contacto():
    """
    Esta funcion solicita los datos del nuevo contacto al usuario
    :return: contacto
    """
    nombre = input("Introduce el nombre completo del contacto: ")
    direccion = input('introduce la direccion del contacto: ')
    email = input('Introduce el email del contacto: ')
    telefono = input('Introduce el telefono del contacto: ')
    contacto = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'email': email
    }
    return contacto


def crear_contacto(agenda_digital, nuevo_contacto):
    """
    Introduce un nuevo contacto en la agenda existente
    agenda_digital -- dict que representa la agenda digital existente
    nuevo_contacto -- dict que representa un nuevo contacto
    :return:
    """
    agenda_digital[nuevo_contacto["nombre"]] = {
        'direccion': nuevo_contacto['direccion'],
        'telefono': nuevo_contacto['telefono'],
        'email': nuevo_contacto['email']
    }
    return agenda_digital



crear_contacto(agenda_digital_init, solicitar_contacto())