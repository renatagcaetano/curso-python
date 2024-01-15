def somar():
    print('Esta função somará valores.')


def multiplicar():
    print('Esta função multiplicará valores.')


def encontrar_index(lista, item):
    for i, valor in enumerate(lista):
        if valor == item:
            return i
    return -1
