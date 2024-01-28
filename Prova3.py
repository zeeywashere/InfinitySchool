from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def quadrado(a):
    return a**2
def somatotal(a, b):
    return a+b
def pares(a):
    return a % 2 ==0

somatotal = reduce(somatotal, numeros)
quadrado =  list(map(quadrado, numeros))
pares = list(filter(pares, numeros))

print("valores ao quadrado", quadrado )
print("pares", pares)
print("soma", somatotal)


    

