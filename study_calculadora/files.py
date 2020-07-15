import csv

with open('tema1.txt', newline='') as filename:
    inputs = list(csv.reader(filename))

# print(inputs)


op = ' '
z = 0
f = open('results.txt', 'w')
# var1 = str(inputs[0])

# print(var1)

# x = var1[3:4]

# print(x)
# print(var1.split())
n = 0

while n < 5:
    var1 = str(inputs[n])
    print(var1)
    n = n + 1
print('bye')




#
# var1 = 'palavra1asd'
# var2 = 'palavra2'
# var3 = 3
# var4 = 1.334
#
# test1 = 'elefante'
# test2 = 2
# test3 = 3
#
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
#
# print(var1[0:var1.find('1',0)])

# print(var1[0:5])

# print(var3 + var4)
#
# #
# #
# # for chave,vlr in new_file2.var8.items():
# #     if test3 == vlr: print(chave)
#
#
# contl = {}
#
# for letra in 'onomatopeia':
#     if letra not in contl.keys():
#         contl[letra] = 1
#     else:
#         contl[letra] = contl[letra] + 1
#
# print(contl)

