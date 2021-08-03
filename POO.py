# -*- coding: utf-8 -*-
"""
@author: felip
"""

"""
Objeto: Tiene propiedades (atributos) y comportamientos (métodos)

Clase: Modelo donde se redactan las características comunes de un grupo de objetos
Instancia: Ejemplar perteneciente a una clase
Modularización: Generar varias clases de acuerdo al tamaño del proyecto
"""
class Coche():#Crear clase
    
#Propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False
    
    #comportamientos
    def arrancar(self): #Método
        self.enMarcha=True
    def estado(self):
        if(self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche está en parado"
            

miCoche=Coche()#crear instancia (objeto. Instanciar una clase)       
print(miCoche.largoChasis)
miCoche.arrancar()
print(miCoche.estado())
    
miCoche2=Coche()#Segundo objeto