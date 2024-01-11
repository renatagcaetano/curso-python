from sys import getsizeof

numeros = [i * 10 for i in range(100)]
print(type(numeros))
#print(numeros)
print(getsizeof(numeros))

numeros = (i * 10 for i in range(100))
print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))
