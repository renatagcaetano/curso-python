from math import pow


def imc(peso, altura):
    imc = peso / pow(altura, 2)

    if imc < 18.5:
        indice = 'peso baixo'
    elif imc < 25:
        indice = 'peso normal'
    elif imc < 30:
        indice = 'sobrepeso'
    elif imc < 40:
        indice = 'obesidade'
    else:
        indice = 'obesidade grave'

    return indice


altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

print(f"Seu IMC é de {imc(peso, altura)}")
