ecuacion="4*2-2/4*67^2"
x=[]
final=""
#print(len(ecuacion))
for i in range(len(ecuacion)):
    print (ecuacion[i])
    
    if(ecuacion[i]=="^"):
        print("potencia")
        final=ecuacion[i-1]
        x.append(final)
        print(x)
        print("Ecuacion ",final)
        print(type(final))
    

        
#print("Ecuacion final: ",ecuacionfinal)    