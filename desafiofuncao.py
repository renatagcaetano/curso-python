from math import pow


def number_square(number):
    return pow(number, 2)


number = float(input('Informe um número:'))

print(f'O quadrado do número {number} é {number_square(number)}.')
