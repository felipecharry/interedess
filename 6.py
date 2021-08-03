n = int(input('Digite el nùmero: '))

def fibonacci(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(n)
print("El valor de fibonacci es: ",fibonacci(n))