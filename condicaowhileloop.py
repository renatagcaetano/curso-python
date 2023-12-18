valor = float(input('Informe o valor do produto: R$ '))

while valor > 20:
    valor = (valor * 0.1) + valor
    print(f'O valor final do produto é R${(valor)}')
    break
