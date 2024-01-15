class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


funcionario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
funcionario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

print(funcionario1.nome + ' ' + funcionario1.sobrenome)
print(funcionario1.nome_completo())
print(Funcionarios.nome_completo(funcionario1))
