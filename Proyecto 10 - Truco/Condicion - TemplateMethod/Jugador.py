from Juego import Juego

class Jugador:

    def __init__(self, nom):
        if not isinstance(nom,str):
            raise TypeError("El nombre del jugador debe ser un string")
        self._nom = nom
        self._cartas = []
        self._initRonda()
        self._pts = 0
        
    def _initRonda(self):
        self._ronda = 0
        self._strategyMenu = self._menuPrimerMano
        self._flor = None
        self._tantos = 0

    def jugar(self):
        return self._strategyMenu()

    def _menuPrimerMano(self):
        self._strategyMenu = self._menu
        return self._menu(self._mesa.strategyEnvido().listaCantos(self))

    def _menu(self,masItems=[]):
        if len(self._cartas) <=0:
            raise TypeError("No puedo jugar una mano porque no tengo cartas que jugar")
        menu = "\n" + self.__str__() + ":\n"+\
               "  1) Irse al mazo"
        opts = ["1"]
        for c in range(2,len(self._cartas)+2):
            menu = menu + "\n  " + str(c)+ ") " + str(self._cartas[c-2])
            opts.append(str(c))
        me = ""
        e = c
        if masItems is not None:
            for it in masItems:
                e = e + 1
                me = me + "\n  " + str(e) +") " + it
                opts.append(str(e))
        truco = self._mesa.strategyTruco().listaCantos(self)
        mt = ""
        if len(truco) > 0:
            mt = mt + "\n  " + str(e+1) +") " + truco[0]
            opts.append(str(e+1))
        r = int(self.responder(menu+me+mt,opts, False))
        if r > c and r <= e: 
            self._mesa.cantarEnvido(self,masItems[r-c-1])
            r = int(self.responder(menu+mt,opts, False))
        if r == e+1: 
            if not self._mesa.cantarTruco(self,truco[0]):
                return None
            r = int(self.responder(menu,opts, False))
        if r==1:
            return self._cartas
        r = self._cartas[int(r)-2]
        self._cartas.remove(r)
        return r

    def responder(self, menu, optList, unicaRta):
        if not isinstance(menu,str):
            raise TypeError("Se esperaba un string con el menu")
        if not isinstance(optList,list):
            raise TypeError("Se esperaba la lista de opciones que debia ingresar el usuario")
        if not isinstance(unicaRta,bool):
            raise TypeError("Se esperaba un bool")
        if unicaRta:
            print(menu,end="")
        else:
            print(menu)
        o = -1
        while o not in optList:
            if not unicaRta:
                print("Opcion: ",end=" ")
            o = input()
        return o

    def cartas(self,cartas):
        if len(cartas)!=3:
            raise TypeError("Se esperaban 3 cartas")
        if len(self._cartas)!=0:
            raise TypeError("Todavia tengo cartas, no termine la ronda")
        self._cartas = cartas
        self._initRonda()

    def flor(self):
        if self._flor is not None:
            return self._flor
        if len(self._cartas) != 3:
            raise TypeError("No tengo cartas para determinar flor")
        c = self._cartas[2]
        v = []
        self._flor = False
        for i in range(2):
            if c.palo() == self._cartas[i].palo():
                v.append(self._cartas[i])
                v.append(c)
        if len(v) == 0:
            if self._cartas[0].palo() == self._cartas[1].palo():
                self._tantos = self._cartas[0].valEnvido() + self._cartas[1].valEnvido() + 20
            else:
                self._tantos = self._cartas[2].num()
                for i in range(2):
                    if self._tantos < self._cartas[i].num():
                        self._tantos = self._cartas[i].num()
        elif len(v) == 2:
            self._tantos = v[0].valEnvido() + v[1].valEnvido() + 20
        else:
            self._tantos = v[0].valEnvido() + v[1].valEnvido() + v[2].valEnvido() + 20
            self._flor = True
        return self._flor
    
    def __str__(self):
        return self._nom

    def strPuntaje(self):
        return " Ronda: " + str(self.ronda()) + " Partida: " + str(self.pts())

    def strCartas(self):
        s = ""
        if len(self._cartas) == 0:
           s = s + " sin cartas"
        else:
            s = s + " Cartas : "
            for carta in self._cartas:
                s = s + str(carta) + " "
        return s

    def pts(self,pts=None):
        if pts is None:
            return self._pts
        elif isinstance(pts,int):
            self._pts = pts
        else:
            raise TypeError("El puntaje debe ser un numero entero")
        
    def anotarPts(self,pts):
        if isinstance(pts,int):
            self._ronda = self._ronda + pts
            self._pts = self._pts + pts
        else:
            raise TypeError("El puntaje debe ser un numero entero")

    def nom(self):
        return self._nom

    def ronda(self):
        return self._ronda

    def mesa(self,mesa):
        if not isinstance(mesa,Juego):
            raise TypeError("Se esperaba una mesa de juego")
        self._mesa = mesa
        
    def irseAlMazo(self):
        cartas = self._cartas
        self._cartas = []
        return cartas

    def rival(self,rival):
        if not isinstance(rival,Jugador):
            raise TypeError("Se esperaba un jugador como oponente")
        self._rival = rival
        
    def equipo(self):
        return self._num

    def setNum(self,num):
        self._num = num

    def num(self):
        return self._num

    def esIgual(self, jug):
        if not isinstance(jug,Jugador):
            raise TypeError("Solo se puede comparar contra un jugador")
        return self._equipo == jug.equipo() 

    def tantos(self):
        return self._tantos