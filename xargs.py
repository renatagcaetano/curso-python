# Vários arguentos (xargs)


def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


x = soma(2, 3, 4, 7)
print(x)

x = soma(2, 3, 4, 7, 4)
print(x)
