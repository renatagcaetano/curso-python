from math import pow

number_list = [1, 2, 3, 4, 5, 6]

power = lambda x: int(pow(x, 2))

power_list = []
for i in number_list:
    power_list.append(power(i))

print(power_list)

