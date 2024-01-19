def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n *= i
        return n


number = int(input('Informe um valor para o cálculo de fatorial: '))

print(f'O fatoria de {number} é {factorial(number)}.')
