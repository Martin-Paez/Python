class CartaEsp:
	
    def __init__(self, palo, n):
        self._palo = palo
        self._n = n
        if palo == CartaEsp.palos()[2] and n == 1:
            self._val=100
        elif palo == CartaEsp.palos()[1] and n == 1:
            self._val=90
        elif palo == CartaEsp.palos()[2] and n == 7:
            self._val=80
        elif palo == CartaEsp.palos()[3] and n == 7:
            self._val=70
        elif n == 3:
            self._val=60
        elif n == 2:
            self._val=50
        elif n == 1:
            self._val=40
        else:
            self._val=n

    def __str__(self):
        return "[" + str(self._n) + " de " + str(self._palo) + "]"

    def palos():
        return ["copa","palo","espada","oro"]

    def isMax(self):
        return self._palo == CartaEsp.palos()[2] and self._n == 1

    def comp(self,carta):
        if not isinstance(carta,CartaEsp):
            raise TypeError("Se esperaba una carta espanola para comparar")
        return self._val - carta._val

    def palo(self):
        return self._palo

    def num(self):
        return self._n

    def valEnvido(self):
        if self._n > 9:
            return 0
        return self._n