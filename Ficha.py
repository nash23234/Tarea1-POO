from Dado import *
import random as rnd

class Ficha:
    color = ""
    posicion = 0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(10) #instanciamos un dado de 6 caras y lo lanzamos 10 veces y mostramos los resultados

    def __init__(self, color):  # constructor
        self.color = color
        self.posicion = 0
    
    def avanzar(self): # avanzar la ficha
        self.posicion = self.dado.lanzar()
        print("La ficha "+self.color+" avanzó "+str(self.posicion)+" casillas")
        return self.posicion
     
        
    


 
    


