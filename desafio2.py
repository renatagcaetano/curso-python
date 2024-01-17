def total_latas(rendimento, altura, largura):
    return (altura * largura) / rendimento


rendimento = int(input('Informe o rendimento da lata: '))
altura = int(input('Informe a altura da parede: '))
largura = int(input('Informe a largura da parede: '))

print(
    f'Você precisa de {total_latas(rendimento, altura, largura)} latas de tinta'
)
