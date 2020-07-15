__author__ = 'frederico'

# exercício 8
from random import randint
lista1 = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10']
# from revisao1 import lista1

# exercício 9
print(randint(0,9))

# exercício 10
lista2 = ['e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20']

# exercício 11

# print('balbala ' + str(lista2.__len__()))

while lista1.__len__() <= 19:
    y = randint(0,9)
    if lista2[y] not in lista1:
        lista1.append(lista2[y])


print(lista1)


