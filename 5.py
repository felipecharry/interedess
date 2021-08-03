n=5
x=0.1

Ex=1+x
factorial=1
factoriales=[]

for j in range(1,n+1):   
    factorial*=j
    factoriales.append(factorial)
    
for i in range(2,n+1):          
        Ex+=((x**i)/factoriales[i-1])        
        factorial=1
#print("Factoriales",factoriales)        
print("Resultado Ex: ",str(Ex))
print("Resultado x^n/n: ", (x**n)/n)
        
        
while (n^n)>Ex: 
    
    x=1
    #Ex=1+x+(x^2/2)+(x^2/2)