print('Loop com break: ')
for i in range(1, 11):
    print(i)
    if i == 5:
        break

print('Loop com continue:')
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
