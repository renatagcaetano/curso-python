class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


funcionario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
funcionario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

print(funcionario1.nome)
print(funcionario2.nome)
