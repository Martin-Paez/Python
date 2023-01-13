from CartaEsp import CartaEsp
import random

class MazoTruco:

    def __init__(self):
        self._palos = CartaEsp.palos()
        self._tope = 0
        self._cartas = []
        for p in range(4):
            for n in range(1,8):
                self._cartas.append(CartaEsp(self._palos[p],n))
            for n in range(10,13):
                self._cartas.append(CartaEsp(self._palos[p],n))

    def mezclar(self):
        if len(self._cartas) != 40:
            raise TypeError("Faltan cartas en el mazo antes de mezclar.")
        for c in range(40):
            sw = self._cartas[c]
            i = random.randrange(40)
            self._cartas[c] = self._cartas[i];
            self._cartas[i] = sw
    
    def repartir(self, cant):
        mano = []
        for c in range(cant):
            mano.append(self._cartas.pop())
        return mano

    def agregar(self, cartas):
        for carta in cartas:
            if isinstance(carta,CartaEsp):
                self._cartas.append(carta)
            else:
                raise Exception("Solo se permite agregar cartas espanolas al mazo")

    def mostrarCartas(self):
        s = " "
        for carta in self._cartas:
            s = s + str(carta) + " \n "
        return s

    def __str__(self):
        return "Mazo espanol de 48 cartas"