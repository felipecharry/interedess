# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 03:16:11 2021

@author: felip
"""
#Herencia:Trasladar características y comportamientos de objetos a otros
#Reutilizar código en caso de crear objetos similares

#Características y comportamientos en común se crean en clase padre
class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca; ", self.marca, "\n Modelo: ",self.modelo, "\n En marcha: ",self.enmarcha, "\n Acelerando: ",self.acelera, "\n Frenando: ",self.frena)
        
class Moto(Vehiculos):#ESCRIBIR DENTRO DE PARENTESIS LA CLASE QUE SE HEREDA
     hcaballito=""
     def caballito(self):
         self.hcaballito="Voy hacuendo el caballito"
     def estado(self):
        print("Marca; ", self.marca, "\n Modelo: ",self.modelo, "\n En marcha: ",self.enmarcha, "\n Acelerando: ",self.acelera, "\n Frenando: ",self.frena, "\n ",self.hcaballito)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"             
        else:
            return "La furgoneta NO esta cargada"             
class VElectricos():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True
class BicicletaElectrica(Vehiculos,VElectricos):
    pass
miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
miBici=BicicletaElectrica("Orbea","aa")
miBici.arrancar()
miBici.estado()


    