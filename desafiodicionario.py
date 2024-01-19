countries = {
    'Coreia': 'Seul',
    'Japão': 'Tóquio',
    'Estados Unidos': 'Washington',
    'Rússia': 'Moscou',
    'Alemanha': 'Berlim'
}

country = input('Digite o nome de um país: ')

if country in countries:
    print(f'A capital de {country} é {countries[country]}')
else:
    print('Não temos informações sobre a capital deste país.')
