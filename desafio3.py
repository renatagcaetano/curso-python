funcionarios = [
    'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'
]
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Funcionários que tem carro e trabalham a noite

print(set(turno_noite).intersection(tem_carro))

# Funcionários que tem carro e trabalham de dia

print(set(turno_dia).intersection(tem_carro))

# Funcionários que não tem carro

print(set(funcionarios).difference(tem_carro))
