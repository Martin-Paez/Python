from Canto import Canto

class EnvidoFinalizado(Canto):

    def __init__(self, pts, mesa, portador, estado):
        if estado == None:
            estado = []
        else:
            estado = [estado]
        super().__init__([],pts,mesa,estado, portador)

    def cantar(self, j):
        raise TypeError("No hay mas nada que cantar respecto al envido")

    def _computarRta(self,r,j):
        raise TypeError("No hay mas nada que cantar respecto al envido")

    def _actualizarMenu(self, grito):
        raise TypeError("No hay mas nada que cantar respecto al envido")