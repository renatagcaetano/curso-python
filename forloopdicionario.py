aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 10.0, 'aprovação': True}

for i in aluno:  #mesma coisa que: for i in aluno.keys():
    print(i)

for i in aluno.values():
    print(i)

for i in aluno.items():
    print(i)

for key, value in aluno.items():
    print(key, value)
