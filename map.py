lista1 = [1, 2, 3, 4]


def multiplicar(x):
    return x * 2


lista2 = map(multiplicar, lista1)

print(list(lista2))
