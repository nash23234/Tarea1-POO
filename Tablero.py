from Dado import *
from Ficha import *
from random import *
from random import shuffle
 


class Tablero:
    casillas = []
    casillasTotales = 0
    fichas = []
    jugadores = 0
    orden = []
     
    def __init__(self, numCasillas, numFichas, numJugadores):
         
        self.casillasTotales = numCasillas
        self.jugadores = numJugadores
        self.fichas = []
        self.orden = []
        
        # generar las casillas 
        for i in range(numFichas): # generar las fichas
            self.fichas.append(Ficha("rojo"))
            self.fichas.append(Ficha("azul"))
            self.fichas.append(Ficha("verde"))
            self.fichas.append(Ficha("amarillo"))
            break
        shuffle(self.fichas)# barajar las fichas
        
        print("\nFichas:\n")  # mostrar las fichas
        for ficha in self.fichas:
            print(ficha.color)
        shuffle(self.fichas)
      
         
    
        #agregar jugadores
        for i in range(numJugadores):
            self.orden.append("jugador"+str(i))
        shuffle(self.orden)
        print("\nJugadores\n")
        for i in self.orden:
            print(i)
        print("\n")
        
        
        #mostrar la casilla en forma de lista ejemplo [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.casillas = []
        for i in range(numCasillas):
            self.casillas.append(i)
        print("\nCasillas\n")
        print(self.casillas)
        print("\n")

        #asignar fichas a jugadores con orden aleatorio y mostrar la ficha asignada a cada jugador
        print("\nAsignación de ficha\n")
        for i in range(numFichas):
            self.fichas[i].jugador = self.orden[i]
            print("Ficha "+self.fichas[i].color+" asignada al "+self.fichas[i].jugador) 
        print("\n")
    
         
    def avanzar(self):
        for ficha in self.fichas:
            ficha.avanzar()
        return self.fichas
     
         
        
    def mostrar(self): # mostrar el tablero
        print("\nTablero\n")
        for ficha in self.fichas:
            print(ficha.jugador+" en casilla "+str(ficha.posicion))
        print("\n")
        
        
    def ganador(self): # determinar el ganador de la partida y mostrarlo en pantall
        for ficha in self.fichas:
            if ficha.posicion == 10:
                return ficha.jugador
        return "No hay ganador"
     
         
         
    def jugar(self): # jugar una partida de dados y mostrar el resultad
        print("\nJugando...\n")
        self.avanzar()
        self.mostrar()
        print("\nGanador: "+self.ganador())
        print("\n")  
         
         





 

 
 

    
  

