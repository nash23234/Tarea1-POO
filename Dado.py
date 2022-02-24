from random import *

class Dado:
    caras = 10 # definimos el atributo caras como un atributo de la clase Dado
    
    def __init__(self, caras):
        self.caras = caras
        
    def lanzar(self): # lanzar el dado y devolver el resultado que no se repita el mismo numero
        resultado = 0
        while resultado == 0:
            resultado = randint(1, self.caras)
        return resultado
     
