
import calculadora
import tools
import csv

with open('tema1.txt', newline='') as filename:
    inputs = list(csv.reader(filename))

# print(inputs)


op = ' '
z = 0
f = open('results.txt', 'w')
n = 0

while n < 5:
    var1 = str(inputs[n])
    n = n + 1
    x = float(var1[2:3])
    op = str(var1[3:4])
    y = float(var1[4:5])
    if tools.teststring(op) == 0:
        if op == '+':
            z = calculadora.soma(x, y)
            f.write(str(z) + '\n')
        if op == '-':
            z = calculadora.subtracao(x, y)
            f.write(str(z) + '\n')
        if op == '*':
            z = calculadora.multiplicacao(x, y)
            f.write(str(z) + '\n')
        if op == '/':
            z = calculadora.divisao(x, y)
            f.write(str(z) + '\n')
        if op == 'e':
            z = calculadora.exponecial(x, y)
            f.write(str(z) + '\n')
f.close()
print('resultados gravados com sucesso')



