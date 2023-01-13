from Jugador import Jugador
from abc import ABCMeta, abstractmethod

class Canto (metaclass = ABCMeta):

    def __init__(self,respuestas, puntos, mesa, cantos, portador):
        self._rta = respuestas
        self._pts = puntos
        self._mesa = mesa
        self._armarMenu()
        self._portador = portador
        self._cantos = cantos

    @abstractmethod
    def listaCantos(self,j): 
        pass
    
    @abstractmethod
    def _computarRta(self,r,j): 
        pass

    @abstractmethod
    def _actualizarMenu(self,grito): 
        pass

    def cantar(self,j,canto): 
        if not isinstance(j,Jugador):
            raise TypeError("Se esperaba el jugador que debe responder")
        if not isinstance(canto,str):
            raise TypeError("Se esperaba un string para el canto")
        self._actualizarMenu(canto)
        self._menu = "Cantaron "+canto+"\n"+\
                     str(j) + ":\n" + self._menu
        r = j.responder(self._menu, self._opts, False)
        self._portador = j.equipo()
        if r == "2":
            return False
        return self._computarRta(r,j)

    def _armarMenu(self):
        self._menu = "  1) Quiero\n"+\
                     "  2) No quiero"
        self._opts = ["1","2"]
        if self._rta is None:
            return
        for i in range(len(self._rta)):
            self._menu = self._menu + "\n  " + str(i+3) + ") " + self._rta[i]
            self._opts.append(str(i+3))
    
    def listaCantos(self,jug):
        if self._portador is None or jug.equipo() == self._portador:
            return self._cantos
        return []

    def respuestas(self):
        return self._rta

    def pts(self):
        return self._pts

    def portador(self):
        return self._portador