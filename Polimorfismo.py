# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 04:46:54 2021

@author: felip
"""
class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")   
class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientovehiculo(miVehiculo)        
