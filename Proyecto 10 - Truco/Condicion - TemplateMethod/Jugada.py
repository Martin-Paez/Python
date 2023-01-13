class Jugada():

    def __init__(self,carta,jug):
        self._carta = carta
        self._jug = jug

    def carta(self):
        return self._carta

    def jugador(self):
        return self._jug

    def equipo(self):
        return self._jug.equipo()
