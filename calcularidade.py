from datetime import datetime


class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def calcular_idade(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


funcionario1 = Funcionarios('Helena', 'Cabral', 2009)
funcionario2 = Funcionarios('Carol', 'Silva', 2005)

print(Funcionarios.calcular_idade(funcionario1))
print(Funcionarios.calcular_idade(funcionario2))
