from EnvidoFinalizado import EnvidoFinalizado
from ObservableEnvido import ObservableEnvido
from Canto import Canto

class FaltaEnvido(ObservableEnvido):

    def __init__(self, pts, mesa, portador):
        super().__init__(["Falta envido !!"],pts,mesa,["Falta envido"], portador)

    def _computarRta(self,r,j):
        super()._computarRta(r,j)
        if r == "3":
            print("FALTA ENVIDO NO IMPLEMENTADO, suma 0")
            self._mesa.setStrategyEnvido(EnvidoFinalizado(self._pts,self._mesa,self._portador,None))
        return True

    def _actualizarMenu(self, grito):
        if grito == "Falta Envido":
            self._rta = []
        else:
            return 
        self._armarMenu()