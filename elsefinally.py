try:
    valor = int(input('Informe o valor do seu produto: R$ '))
except ValueError:
    print('Informe um valor válido.')
else:
    print('Valor válido informado.')
    resultado = valor * 2
    print(f'O valor após o calculo é de R$ {resultado}')
finally:
    print('Código executado com sucesso.')

print('Fim do programa.')
