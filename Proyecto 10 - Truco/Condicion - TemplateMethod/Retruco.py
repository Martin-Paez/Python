from ValeCuatro import ValeCuatro
from Canto import Canto

class Retruco(Canto):

    def __init__(self,mesa,portador):
        super().__init__(["Quiero vale cuatro!!"],2,mesa,["Retruco"],portador)

    def _computarRta(self,r,j):
        self._mesa.setStrategyTruco(ValeCuatro(self._mesa,self._portador))
        if r == "3":
            return self._mesa.cantarTruco(j,self._rta[0])
        return True

    def _actualizarMenu(self,grito): 
        pass