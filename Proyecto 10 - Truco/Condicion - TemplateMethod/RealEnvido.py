from FaltaEnvido import FaltaEnvido
from EnvidoFinalizado import EnvidoFinalizado
from ObservableEnvido import ObservableEnvido
from Canto import Canto

class RealEnvido(ObservableEnvido):

    def __init__(self, pts, mesa, portador):
        super().__init__(["Real envido !!", "Falta Envido !!"]
                         ,pts,mesa,["Real envido","Falta Envido"], portador)

    def _computarRta(self,r,j):
        super()._computarRta(r,j)
        if r == "4":
            self._mesa.setStrategyEnvido(EnvidoFinalizado(self._pts,self._mesa,self._portador,"El falta envido fue querido"))
        elif r == "3":
            self._pts = self._pts + 3
            self._mesa.setStrategyEnvido(FaltaEnvido(self._pts,self._mesa,self._portador))
            return self._mesa.cantarEnvidoRec(j,self._rta[0])
        return True

    def _actualizarMenu(self,grito): 
        if grito == "Real Envido":
            self._rta = ["Falta Envido !!"]
        elif grito == "Falta Envido":
            self._rta = []
        else:
            return 
        self._armarMenu()
