#Calcular la suma de los cuadrados de los 100 primeros números naturales.

contador = 0
for i in range(1,101):
    contador+= i * i
print("Suma de cuadrados primeros 100 números naturales: ",contador)