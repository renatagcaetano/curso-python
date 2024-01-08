produtos = [
    'arroz', 'feijão', 'laranja', 'banana', 'maçã', 'tomate', 'cebola',
    'cenoura', 'beterraba'
]
'''

item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

print(item1)
print(item2)
print(item3)
print(item4)

item1, item2, item3, item4 = produtos

print(item1)
print(item2)
print(item3)
print(item4)

'''

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)

item1, item2, *outros, item8 = produtos

print(item1)
print(item2)
print(outros)
print(item8)
