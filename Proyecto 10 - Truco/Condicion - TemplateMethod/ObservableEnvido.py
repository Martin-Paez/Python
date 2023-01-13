from ObservadorEnvido import ObservadorEnvido
from Canto import Canto

class ObservableEnvido(Canto):

    def __init__(self,respuestas, puntos, mesa, cantos, portador):
        super().__init__(respuestas, puntos, mesa, cantos, portador)
        self._observador = None
    
    def _computarRta(self,r,j):
        self.notificar()
    
    def notificar(self):
        if self._observador is not None:
            self._observador.envidoCantado()

    def suscribir(self,o):
        if not isinstance(o,ObservadorEnvido):
            raise TypeError("Se esperaba un observador de envido")
        self._observador = (o)