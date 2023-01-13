class Mano():

    def __init__(self):
        self._rondas = []
        self._equipoGanador = None
        self._parda = 0
        self._pts = [0,0]

    def agregar(self,ronda):
        if len(self._rondas) >= 3:
            raise TypeError("Una mano no puede tener mas de tres rondas (sin parda)")
        if self._equipoGanador is not None:
            raise TypeError("La mano ya tiene un ganador")
        self._rondas.append(ronda)   
        mejores = ronda.mejoresJugadas()
        if len(mejores) > 1:
            self._parda = self._parda + 1
            sz = len(self._rondas)
            if (sz == 2 and sz != self._parda) or sz == 3:
                print("Si se parda la 2da gana quien tiene la primera, o en su defecto, se juega la 3era.\nSi se parda la 3era, gana quien hizo primera, o en su defecto, quien halla empezado como mano")
                self._equipoGanador = self._rondas[0].mejoresJugadas()[0].equipo()
            return
        if self._parda >= 1:
            self._equipoGanador = mejores[0].equipo()
        else:
            equipo = mejores[0].equipo()
            self._pts[equipo] = self._pts[equipo] + 1
            for i in range(2):
                if self._pts[i] == 2:
                    self._equipoGanador = i

    def equipoGanador(self):
        return self._equipoGanador