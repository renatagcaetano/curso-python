aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 10.0, 'aprovação': True}
print(aluno)

aluno['nome'] = 'José'
print(aluno)

aluno.update({'nome': 'Bruno', 'nota_final': 8.0})
print(aluno)

aluno.update({'endereço': 'Rua A'})
print(aluno)

print(aluno.get('nascimento', 'Não existe'))

del aluno['idade']
print(aluno)
