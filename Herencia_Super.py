# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 04:16:56 2021

@author: felip
"""
class Persona():
    def __init__(self,nombre,edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ",self.edad, " Residencia:", self.residencia)
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, " Antiguedad: ",self.antiguedad)        
Antonio=Empleado(5,6,"Manuel",55,"Colombia")
Antonio.descripcion()


print(isinstance(Antonio,Persona))
        
        