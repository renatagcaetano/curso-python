even_odd = lambda x: 'par' if x % 2 == 0 else 'ímpar'

number = int(input('Digite um número: '))

print(f'O número {number} é {even_odd(number)}')
