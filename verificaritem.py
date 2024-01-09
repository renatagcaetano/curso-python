cores = ['amarelo', 'verde', 'azul', 'vermelho']

cor = input('Informe a cor desejada: ')

if cor.lower() in cores:
    print(f'A cor {cor} está disponível')
else:
    print(f'A cor {cor} não está disponível')
