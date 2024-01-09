cores_lista = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(cores_lista)
print(cores_tuple)

print(type(cores_lista))
print(type(cores_tuple))

duas_listas = cores_lista * 2
print(duas_listas)

duas_tuples = cores_tuple * 2
print(duas_tuples)

cores_lista.append('roxo')
print(cores_lista)

#cores_tuple.append('roxo')