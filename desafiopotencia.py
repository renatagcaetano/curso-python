from math import pow


def power(number1, number2 = 2):
    return pow(number1, number2)


number1 = float(input('Informe o valor da base: '))
number2 = input('Informe o valor do expoente: ')

if number2:
    print(f'A potência é {power(number1, int(number2))}')
else:
    print(f'A potência é {power(number1)}')