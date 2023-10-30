class Game:

    def __init__(self, filas, columnas):
        self._filas = filas
        self._columnas = columnas
        self._tablero = []
        self._color = ''

    def crear_tablero(self):
        self._tablero = [None] * self._filas
        for row in range(self._filas):
            self._tablero[row] = ['*'] * self._columnas
        return self._tablero

    def mostrar_tablero(self):
        print(self._tablero)
        for num in range(len(self._tablero[0])):
            print(num, end='  ')
        for row in self._tablero:
            print('')
            for casilla in row:
                print(casilla, end='  ')

    def _revisar_filas(self, color):
        # obtener el numero de filas y columnas
        num_rows = len(self._tablero)
        num_cols = len(self._tablero[0])

        for r in range(num_rows):
            for c in range(num_cols):
                if ((self._tablero[r][c] == color) and (self._tablero[r][c + 1] == color) and
                        (self._tablero[r][c + 2] == color) and
                        self._tablero[r][c + 3] == color):
                    return True

    def _revisa_columnas(self, color):
        num_rows = len(self._tablero)
        num_cols = len(self._tablero[0])
        print("Entra")
        for c in range(num_cols):
            for r in range(num_rows):
                if (
                        self._tablero[c][r] == color and
                        self._tablero[c][r + 1] == color and
                        self._tablero[c][r - 2] == color and
                        self._tablero[c][r + 3] == color):
                    print("Entra")
                    return True

    def _revisar_diagonal_derecha(self, color):
        num_rows = len(self._tablero)
        num_cols = len(self._tablero[0])
        for c in range(num_cols):
            for r in range(num_rows - 1, 2, -1):
                if (self._tablero[r][c] == color and self._tablero[r - 1][c + 1] == color and
                        self._tablero[r - 2][c + 2] == color and
                        self._tablero[r - 3][c - 3] == color):
                    return True

    def _revisar_diagonal_iz(self, color):
        num_rows = len(self._tablero)
        num_cols = len(self._tablero[0])
        for c in range(num_cols - 1, 2, -1):
            for r in range(num_rows - 1, 2, -1):
                if (self._tablero[r][c] == color and self._tablero[r - 1][c - 1] == color and
                        self._tablero[r - 2][c - 2] == color and
                        self._tablero[r - 3][c - 3] == color):
                    return True

    def introducir_ficha(self, selected_column, color):
        print(self._tablero[0])
        if selected_column > len(self._tablero[0]) or selected_column < 0:
            print("columna no valida")
        elif '*' in self._tablero[0]:
            for row in range(len(self._tablero) - 1, -1, -1):
                if self._tablero[row][selected_column] == '*':
                    self._tablero[row][selected_column] = color
                    self._color = color
                    return self._tablero
        else:
            print("el tablero estalleno")

        return self._tablero

    def comprobar_ganador(self, color):
        result = (self._revisar_filas(self._tablero, color) or self._revisa_columnas(self._tablero, color) or self._revisar_diagonal_derecha(self._tablero, color) or self._revisar_diagonal_iz(self._tablero, color ))
        return result


juego = Game(5, 5)
juego.crear_tablero()
juego.mostrar_tablero()
juego.introducir_ficha(4, 'x')
juego.mostrar_tablero()
juego.introducir_ficha(4, 'x')
juego.mostrar_tablero()
juego.introducir_ficha(4, 'x')
juego.mostrar_tablero()
juego.introducir_ficha(4, 'x')
juego.mostrar_tablero()
print(juego.comprobar_ganador('x'))
