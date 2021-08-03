ecuacion="4*2-2/4*67^2"

def suma():
	print('suma')

def resta():
	print('resta')

def multiplicacion():
	print('multiplicacion')

def division():
	print('division')

def exponente():
	print('exponente')

def numero():
	print('numero')
 
valor = {
	"+": suma,
	"-": resta,
	"*": multiplicacion,
	"/": division,
	"^": exponente,
}

#print(len(ecuacion))
for i in range(len(ecuacion)):
    print (ecuacion[i])
    accion=valor.get(ecuacion[i], numero)()

    
    
    
    try:
        ecuacionfinal=accion
        
    except ValueError:
        print("Ecuacion incompleta")    
        
print("Ecuacion final: ",ecuacionfinal)    