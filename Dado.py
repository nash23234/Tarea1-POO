from random import *

class Dado:
    caras = 10
    
    def __init__(self, caras):
        self.caras = caras
        
    def lanzar(self): # lanzar el dado y devolver el resultado que no se repita el mismo numero
        resultado = 0
        while resultado == 0:
            resultado = randint(1, self.caras)
        return resultado
     
    #Porque solo me tira de 1 a 6? Porque el dado tiene 6 caras y el random lo hace de 1 a 6
     
     