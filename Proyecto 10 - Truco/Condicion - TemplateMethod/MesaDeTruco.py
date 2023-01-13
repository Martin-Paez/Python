from Juego import Juego
from Jugador import Jugador
from Jugada import Jugada
from MazoTruco import MazoTruco
from ValeCuatro import ValeCuatro
from Truco import Truco
from Retruco import Retruco
from Ronda import Ronda
from Mano import Mano
from Canto import Canto
from abc import ABCMeta, abstractmethod
from Envido import Envido
from EnvidoFinalizado import EnvidoFinalizado

class MesaTruco(Juego):

    def __init__(self,jug,mazo,conFlor):
        super().__init__(mazo)
        '''if not isinstance(jugs, list):
            raise TypeError("Se esperaba una lista de jugadores")
        for j in jugs:'''
        if not isinstance(jug, Jugador):
            raise TypeError("Se esperaba un jugador de truco")
        if not isinstance(conFlor,bool):
            raise TypeError("Se esperaba un booleano para determinar si se juega con flor o no")
        if not isinstance(mazo,MazoTruco):
            raise TypeError("Se esperaba un mazo de truco")
        self._jugs=[jug]
        self._jugs.append(Jugador("PC"))
        '''sz = len(self._jugs)
        for i in range(sz):
            self._jugs[i].rival(self._jugs[(i+1)%sz])'''
        for i in range(len(self._jugs)):
            self._jugs[i].mesa(self)
            self._jugs[i].setNum(i)
        self._conFlor = conFlor
        self._turno = 0

    def repartir(self):
        print("Nueva Ronda:")
        print(str(self._jugs[self._turno]) + " es mano")
        for j in self._jugs:
            j.cartas(self.mazo().repartir(3))
            print(str(j) + " -" + j.strCartas() + "- Equipo: " + str(j.equipo()))
        if self._conFlor:
            v = []
            j = self._jugs[self._turno]
            for i in range(len(self._jugs)):
                if j.flor():
                    v.append(j)
                j = self.oponente(j)
            if len(v) == 0:
                return
            j = v[len(v)-1]
            if len(v) > 1:
                for i in range(len(v)-1):
                    if self._jugs[i].tantos() > j.tantos():
                        j = self._jugs[i]
            self.setStrategyEnvido(EnvidoFinalizado(3,self,j.equipo(),None))    

    def tomarCarta(self):
        pass
    
    def oponente(self,jug):
        if not isinstance(jug,Jugador):
            raise TypeError("Se esperaba un jugador")
        return self._jugs[(jug.num()+1)%len(self._jugs)]

    def integrantes(self,equipo):
        return range(equipo % 2,len(self._jugs),2)

    def decidir(self):
        equipoG = None
        repartidas = []
        self._strategyEnvido = Envido(self)
        self._strategyTruco = Truco(self)
        mano = Mano()
        jug = self._jugs[self._turno]
        r = 0
        while equipoG == None:
            ronda = Ronda()
            for j in range(len(self._jugs)):
                carta = jug.jugar()
                if isinstance(carta,list):
                    print(str(jug) + " se fue al mazo")
                    equipoG = self.oponente(jug).equipo()
                    break   
                if carta is None:
                    jug = self._strategyTruco.portador()
                    print("El equipo " + str(jug) +" no quizo continuar")
                    equipoG = (jug+1)%2
                    break
                print(str(jug)+" jugo: "+str(carta))
                ronda.agregar(Jugada(carta,jug))
                repartidas.append(carta)
                jug = self.oponente(jug)
            if equipoG is None:
                mano.agregar(ronda)
                equipoG = mano.equipoGanador()
                print("\n--------------------------------")
                print("\nRonda: " + str(r+1))
                r = r + 1
                for ro in ronda.jugadas():
                    print(str(ro.jugador())+": "+str(ro.carta()))
                m = ronda.mejoresJugadas()
                if len(m) > 1:
                    print("La ronda termino en parda")
                else:
                    print("La ronda la gano " + str(m[0].jugador()))
                print("Premio acumulado del truco: " + str(self._strategyTruco.pts()))
                if r == 1:
                    print("Premio de envido/flor: " + str(self._strategyEnvido.pts()))
                jug = ronda.mejoresJugadas()[0].jugador()
        for j in self.integrantes(equipoG):
            self._jugs[j].anotarPts(self._strategyTruco.pts())
        self._turno = (self._turno + 1) % len(self._jugs)
        self._mazo.agregar(repartidas)
        
    def cantarTruco(self,jug,canto):
        if not isinstance(jug,Jugador):
            raise TypeError("Solo un jugador puede cantar truco")
        if not isinstance(canto,str):
            raise TypeError("El canto debe ser un string")
        e = self.oponente(jug).equipo()
        for i in self.integrantes(e):
            quiere = self._strategyTruco.cantar(self._jugs[i],canto)    
            if quiere:
                break
        return quiere

    def cantarEnvido(self,jug,canto):
        if not self.cantarEnvidoRec(jug,canto):
            print("\n******************************")
            equipoG = (self._strategyEnvido.portador()+1)%2
            self.anotarEnvido(equipoG)
            self._strategyEnvido = EnvidoFinalizado(0,self,equipoG,None)

    def cantarEnvidoRec(self,jug,canto):
        if not isinstance(jug,Jugador):
            raise TypeError("Solo un jugador puede cantar truco")
        if not isinstance(canto,str):
            raise TypeError("El canto debe ser un string")
        e = self.oponente(jug).equipo()
        for i in self.integrantes(e):
            quiere = self._strategyEnvido.cantar(self._jugs[i],canto)    
            if quiere:
                self.calcEnvido()
                return True
        return False

    def calcEnvido(self):
        g = self._jugs[self._turno]
        if len(self._jugs) > 2:
            j = (j+2)%2
            if g.tantos() < self._jugs[j].tantos():
                g = self._jugs[j]
        print("\n******************************")
        print("\n" + str(g) + " tiene " + str(g.tantos()))
        for i in self.integrantes(self.oponente(g).equipo()):
            j = self._jugs[i]
            if j.tantos() > g.tantos():
                g = j
                print(str(j) + ": " + str(j.tantos()))
                break
            else:
                print(str(j) + ": 'son buenas'")
        self.anotarEnvido(g.equipo())
        self._strategyEnvido = EnvidoFinalizado(0,self,g.equipo(),None)
        
    def anotarEnvido(self,equipoG):
        for j in self.integrantes(equipoG):
            self._jugs[j].anotarPts(self._strategyEnvido.pts())
        print("El equipo " + str(equipoG) + " se anoto " + str(self._strategyEnvido.pts()) + " puntos")
        

    def retrucar(self,jug):
        self._strategyTruco.cantar(jug)   

    def setStrategyTruco(self,strategy):
        self._strategyTruco = strategy
        
    def strategyTruco(self):
        return self._strategyTruco

    def setStrategyEnvido(self,strategy):
        self._strategyEnvido = strategy
        
    def strategyEnvido(self):
        return self._strategyEnvido

    def descartar(self):
        for j in self._jugs:
            self.mazo().agregar(j.irseAlMazo())

    def ganador(self):
        print("\n----------------------------")
        print("\n  Resultado:")
        print("\n----------------------------")
        empate = 0
        jug = self._jugs[0]
        for j in self._jugs:
            print(str(j) + " -" + j.strPuntaje())
            if j.ronda() == jug.ronda():
                empate = empate + 1
            elif j.ronda() > jug.ronda():
                jug = j
        if empate == len(self._jugs):
            return None
        return jug

    def ptsTruco(self):
        return self._ptsTruco

    '''def conFlor(self):
        return self._conFlor'''