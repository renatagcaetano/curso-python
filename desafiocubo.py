from math import pow

power = lambda n: pow(n, 3)

number = int(input('Informe um número: '))

print(f'O cubo de {number} é {int(power(number))}.')
