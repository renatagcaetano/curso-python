temperatura = int(input('Informe a temperatura de cozimento da carne: '))

if temperatura < 48:
    print('Cozinhe por mais alguns minutos.')
elif temperatura < 54:
    print('Carne selada.')
elif temperatura < 60:
    print('Carne ao ponto para mal.')
elif temperatura < 65:
    print('Carne ao ponto.')
elif temperatura < 71:
    print('Carne ao ponto para bem.')
else:
    print('Carne bem passada.')
    