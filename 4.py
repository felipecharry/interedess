#Leer un archivo que solo contiene números y sumar los números pares y primos
def primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            #print (i)
            if num % i == 0:
                return False
        return True      

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
    resultado = primo(i)
    if resultado==True:
        #print(i, "Es primo")
        primos+=i
    if i%2==0:
        pares+=i
print("La suma de los nùmeros pares es: ",pares)     
print("La suma de los nùmeros primos es: ",primos)     