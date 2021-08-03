"""Calcular los múltiplos de 4 comprendidos entre 4 y N , donde N es un valor
introducido por consola.
"""

numero = input('Digite el n�mero: ')
print("\nMúltiplos de 4: ")
for i in range(1, int(numero) + 1):
    if i % 4 == 0:
        print(i)   