from Canto import Canto
from ValeCuatroQuerido import ValeCuatroQuerido

class ValeCuatro(Canto):

    def __init__(self,mesa,portador):
        super().__init__([],3,mesa,["Vale Cuatro"],portador)

    def _computarRta(self,r,j):
        self._mesa.setStrategyTruco(ValeCuatroQuerido(self._mesa,self._portador))
        return True

    def _actualizarMenu(self,grito): 
        pass