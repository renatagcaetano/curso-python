cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores, strict=True)

print(list(duas_listas))
