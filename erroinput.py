try:
    valor = int(input('Informe o valor do seu produto: R$ '))
    print(valor)
except ValueError:
    print('Informe um valor válido.')

print('Fim do programa.')
