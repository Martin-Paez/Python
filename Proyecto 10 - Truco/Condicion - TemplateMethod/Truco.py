from Retruco import Retruco
from Canto import Canto
from EnvidoFinalizado import EnvidoFinalizado
from ObservadorEnvido import ObservadorEnvido

class Truco(Canto,ObservadorEnvido):

    def __init__(self, mesa):
        super().__init__(["Quiero Retruco!!","Quiero, pero el envido esta primero"]
                         ,1,mesa,["Truco"], None)
        self._mesa.strategyEnvido().suscribir(self)
        
    def _computarRta(self,r,j):
        if r == "4":
            self._mesa.cantarEnvido(j,"Envido !!")
        self._mesa.setStrategyTruco(Retruco(self._mesa,self._portador))
        pts = self._mesa.strategyEnvido().pts()
        self._mesa.setStrategyEnvido(EnvidoFinalizado(pts,self._mesa,self._portador,None))    
        if r == "3":
            return self._mesa.cantarTruco(j,self._rta[0])
        return True

    def envidoCantado(self):
        self._rta = self._rta[0:1]

    def _actualizarMenu(self,grito): 
        pass