lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

numero1 = set(lista1)
numero2 = set(lista2)

print(numero1 | numero2)
print(numero1 - numero2)
print(numero2 - numero1)
print(numero1 ^ numero2)
print(numero1 & numero2)

print(len(numero1))
#print(numero1[0])
