import math


def fatorial(valor):
    for i in range(1, valor):
        valor *= i
    return valor


print(fatorial(4))

print(math.factorial(4))
print(math.floor(2.7))
print(math.ceil(2.7))
