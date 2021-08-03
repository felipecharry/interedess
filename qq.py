#Leer un archivo que solo contiene números y sumar los números pares y primos
numeros=[]
pares=0
primos=0
with open('nùmeros.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':        
        if linea!="\n":
            numeros.append(int(linea))
        linea = fichero.readline()
print("Nùmeros del documentos:", numeros)
for i in numeros:
    if i%2==0:
        pares+=i
print("La suma de los nùmeros pares es: ",pares)     
