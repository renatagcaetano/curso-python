set1 = {1, 2, 3, 4, 5, 6}

print(set1)
print(type(set1))

set1.add(7)
print(set1)
set1.add(4)
print(set1)

set1.update([8, 9, 10])
print(set1)

set1.remove(10)
print(set1)

set1.discard(90)
print(set1)

set2 = {1, 2, 3, 4, 5, 6, 7, 2}
print(set2)
