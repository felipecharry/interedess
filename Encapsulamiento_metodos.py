# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:08:52 2021

@author: felip
"""
#Encapsulaimento de métodos

#EVITAR QUE SE REALICE CHEQUEO CUANDO UN CARRO ESTÁ APAGADO

class Coche():#Crear clase
    def __init__(self):#CONSTRUCTOR
        #Propiedades
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False
    
    #comportamientos
    def arrancar(self,arrancamos): #Método
        self.__enMarcha=arrancamos
        
        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()
    
        if(self.__enMarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__enMarcha and chequeo==False) :
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche está en parado"
    def estado(self):
        print ("El coche tiene ",self.__ruedas," ruedas")
           
   
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        
        

miCoche=Coche()#crear instancia (objeto. Instanciar una clase)       

print(miCoche.arrancar(True))

miCoche.estado()

print ("Segundo objeto")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
