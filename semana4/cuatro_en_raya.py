
# crear el juego 4 en raya

# generar el tablero
def crear_tablero(filas, columnas):
    """
    :param filas: numero de filas en el tablero
    :param columnas: numero de columnas enel tablero
    :return: tablero: con las filas y columans introducidas
    """
    tab = [None]*filas
    for row in range(filas):
        tab[row] = ['*']*columnas
    return tab


# imprimir el tablero
def mostrar_tablero(tablero):
    print(tablero)
    for num in range(len(tablero[0])):
        print(num, end='  ')
    for row in tablero:
        print('')
        for casilla in row:
            print(casilla, end='  ')


# introducir fichas en el tablero
# implementar funcion para introducir una ficha


def introducir_ficha(tab, color, colum):
    print(tab[0])
    if colum > len(tab[0]) or colum < 0:
        print("columna no valida")
    elif '*' in tab[0]:
        for row in range(len(tab)-1, -1, -1):
            if tab[row][colum] == '*':
                tab[row][colum] = color
                return tab
    else:
        print("el tablero estalleno")

    return tab


def revisar_filas(tab, color):
    # obtener el numero de filas y columnas
    num_rows = len(tab)
    num_cols = len(tab[0])

    for r in range(num_rows):
        for c in range(num_cols):
            if (tab[r][c] == color) and (tab[r][c + 1] == color) and (tab[r][c + 2] == color) and tab[r][c + 3] == color:
                return True


def revisa_columnas(tab, color):
    num_rows = len(tab)
    num_cols = len(tab[0])

    for c in range(num_cols):
        for r in range(num_rows):
            if tab[c][r] == color and tab[c][r+1] == color and tab[c][r -2] == color and tab[c][r +3]:
                return True


def revisar_diagonal_derecha(tab, color):
    num_rows = len(tab)
    num_cols = len(tab[0])
    for c in range(num_cols):
        for r in range(num_rows-1, 2, -1):
            if tab[r][c] == color and tab[r -1][c +1] == color and tab[r -2][c +2] == color and tab[r -3][c-3] == color:
                return True


def revisar_diagonal_iz(tab, color):
    num_rows = len(tab)
    num_cols = len(tab[0])
    for c in range(num_cols - 1, 2, -1):
        for r in range(num_rows-1, 2, -1):
            if tab[r][c] == color and tab[r-1][c-1] == color and tab[r-2][c - 2] == color and tab[r-3][c-3] == color:
                return True


def comprobar_ganador(tab, color):
    return (revisar_filas(tab, color) or revisa_columnas(tab, color) or revisar_diagonal_derecha(tab, color)
            or revisar_diagonal_iz(tab, color))


def iniciar_juego():
    tablero = crear_tablero(6, 7)
    sig_turno = 'A'
    while True:
        turno = sig_turno
        mostrar_tablero(tablero)
        col = None
        if turno == 'R':
            col = int(input("Turno del rojo: "))
            sig_turno = 'A'
        elif turno == 'A':
            col = int(input("Turno del amarillo: "))
            sig_turno = 'R'
        introducir_ficha(tablero, turno, col)
        if comprobar_ganador(tablero, turno):
            print("Ganador el jugador ", turno, "\n\n")
            mostrar_tablero(tablero)
            break


iniciar_juego()
