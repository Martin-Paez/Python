from Canto import Canto

class ValeCuatroQuerido(Canto):

    def __init__(self,mesa,portador):
        super().__init__([],4,mesa,[],portador)

    def cantar(self, j):
        raise TypeError("No se puede cantar nada al vale cuatro")

    def _computarRta(self,r,j):
        raise TypeError("No se puede cantar nada al vale cuatro")

    def _actualizarMenu(self,grito): 
        raise TypeError("No se puede cantar nada al vale cuatro")
    
