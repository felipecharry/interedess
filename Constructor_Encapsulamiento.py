# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:08:52 2021

@author: felip
"""


class Coche():#Crear clase
    def __init__(self):#CONSTRUCTOR
        #Propiedades
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4
        self.enMarcha=False
    
    #comportamientos
    def arrancar(self,arrancamos): #Método
        self.enMarcha=arrancamos
        self.enMarcha=True
    def estado(self):
        print("El coche tiene ",self.__ruedas)
        

miCoche=Coche()#crear instancia (objeto. Instanciar una clase)       
print(miCoche.largoChasis)
miCoche.arrancar(True)
print(miCoche.estado())
miCoche.ruedas=2
print(miCoche.estado())
    
miCoche2=Coche()#Segundo objeto        
    