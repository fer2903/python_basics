"""
Uno de los mecanismos más utilizados para verificar la integridad de la información son las funciones **hash**. Una función hash recibe como argumento un objeto, en este caso, una cadena de texto de longitud variable, y nos devuelve un número entero de longitud fija que identifica de manera unívoca el contenido de la cadena de texto. En el caso de que cambie cualquier carácter de la cadena de texto, el valor que proporcionará la función hash será completamente distinto.

Cuando nosotros mandamos un mensaje de texto a otra persona, podemos garantizar que el mensaje no ha sido modificado en tránsito si añadimos junto con el mensaje el resultado de una función hash. De esta manera, cuando el mensaje sea recibido por el receptor, puede utilizar la misma función hash para comprobar que el resultado que le proporciona es el mismo que el que nosotros hemos añadido. En caso contrario, el mensaje habrá sido modificado en tránsito.

**En este ejercicio práctico se propone la creación de una sencilla aplicación en Python que nos ayude a verificar la integridad de un mensaje calculando la función hash de una cadena de texto que el usuario le proporcione.**

¡Completa todos los apartados que se muestran a continuación para conseguir construir la aplicación!
"""


def cabecera():
    print("""
     ___  ___   ________   ________   ___  ___   ________   ___    ___ 
    |\  \|\  \ |\   __  \ |\   ____\ |\  \|\  \ |\   __  \ |\  \  /  /|
    \ \  \\\  \\ \  \|\  \\ \  \___|_\ \  \\\  \\ \  \|\  \\ \  \/  / /
     \ \   __  \\ \   __  \\ \_____  \\ \   __  \\ \   ____\\ \    / / 
      \ \  \ \  \\ \  \ \  \\|____|\  \\ \  \ \  \\ \  \___| \/  /  /  
       \ \__\ \__\\ \__\ \__\ ____\_\  \\ \__\ \__\\ \__\  __/  / /    
        \|__|\|__| \|__|\|__||\_________\\|__|\|__| \|__| |\___/ /     
                             \|_________|                 \|___|/      


    """)


def hash_text(string):
    return hash(string)


def solicita_string():
    string = input("Ingresa un string para hash: ")
    return string


cabecera()
input_string = solicita_string()
input_hash = hash_text(input_string)
print(input_hash)
