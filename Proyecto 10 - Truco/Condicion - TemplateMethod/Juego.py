from abc import ABCMeta, abstractmethod

class Juego (metaclass = ABCMeta):

    def __init__(self, mazo):
        self._mazo = mazo   

    def jugar(self):
        self.mezclar()
        self.repartir()
        self.jugarMano()
        return self.ganador()

    def jugarMano(self):
        self.tomarCarta()
        self.decidir()
        self.descartar()
        
    def mezclar(self):
        self.mazo().mezclar()
        
    @abstractmethod
    def repartir(self):
        pass

    @abstractmethod
    def tomarCarta(self):
        pass
    
    @abstractmethod
    def decidir(self):
        pass

    @abstractmethod
    def descartar(self):
        pass

    @abstractmethod
    def ganador(self):
        pass

    def mazo(self):
        return self._mazo

    def jug(self):
        return self._jug

    def pc(self):
        return self._pc
