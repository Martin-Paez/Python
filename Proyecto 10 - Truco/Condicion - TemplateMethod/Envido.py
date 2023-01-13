from RealEnvido import RealEnvido
from FaltaEnvido import FaltaEnvido
from EnvidoFinalizado import EnvidoFinalizado
from ObservadorEnvido import ObservadorEnvido
from ObservableEnvido import ObservableEnvido
from Canto import Canto

class Envido(ObservableEnvido):

    def __init__(self, mesa):
        super().__init__(["Envido!!","Real Envido!!","Falta Envido!!"]
                         ,1,mesa,["Envido","Real Envido","Falta Envido"], None)
        self._envidos = 0

    def _computarRta(self,r,j):
        super()._computarRta(r,j)
        if r == "1":
            self._envidos = self._envidos + 1
            if self._pts == 1:
                self._pts = 2
            else:
                self._pts = 4
            if self._envidos > 2:
                raise   TypeError("No se puede cantar el envido tres veces")
            elif self._envidos == 2:
                self._mesa.setStrategyEnvido(RealEnvido(self._pts,self._mesa,self._portador))
        elif r == "3":
            self._envidos = 2
            self._pts = 4
            self._mesa.setStrategyEnvido(RealEnvido(self._pts,self._mesa,self._portador))
            return self._mesa.cantarEnvidoRec(j,self._rta[0])
        elif r == "4" :
            self._pts = 2
            self._mesa.setStrategyEnvido(FaltaEnvido(self._pts,self._mesa,self._portador))
            return self._mesa.cantarEnvidoRec(j,self._rta[1])
        elif r == "5":
            self._pts = 2
            self._mesa.setStrategyEnvido(EnvidoFinalizado(self._pts,self._mesa,self._portador,"El falta envido fue querido"))
        return True

    def _actualizarMenu(self,grito): 
        if grito == "Envido":
            self._rta = ["Envido!!","Real Envido!!","Falta Envido!!"]
        elif grito == "Real Envido":
            self._rta = ["Falta Envido!!"]
        elif grito == "Falta Envido":
            self._rta = []
        else:
            return 
        self._armarMenu()
