from MazoTruco import MazoTruco
from Jugador import Jugador
from MesaDeTruco import MesaTruco

flor = True
mesa = MesaTruco(Jugador("Juan"),MazoTruco(),flor)
ganador = None
while ganador is None:
    ganador = mesa.jugar()
    print("\n")

print("\nGanador: " + str(ganador) + "\n")

'''
import random

v = [*range(13)]
for i in range(13):
    loop = True
    while loop:
        a = random.randrange(1, 13-i)
        loop = a not in v
    print(str(a))
    v.remove(a)
    input()'''
    