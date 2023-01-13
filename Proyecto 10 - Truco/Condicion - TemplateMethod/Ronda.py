class Ronda():

    def __init__(self):
        self._mejores = []
        self._jugadas = []

    def agregar(self,jugada):
        self._jugadas.append(jugada)
        if len(self._mejores) == 0:
            self._mejores.append(jugada)
        else:
            comp = jugada.carta().comp(self._mejores[0].carta())
            if comp > 0:
                self._mejores = [jugada]
            elif comp == 0:
                if len(self._mejores) == 1:
                    if self._mejores[0].equipo() != jugada.equipo():
                        self._mejores.append(jugada)

    def mejoresJugadas(self):
        return self._mejores

    def jugadas(self):
        return self._jugadas
