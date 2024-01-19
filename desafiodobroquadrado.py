from math import pow


def double(n):
    return n * 2


def power(n):
    return pow(double(n), 2)


number = int(input('Informe um número: '))

print(f'O quadrado do dobro de {number} é {power(number)}')
