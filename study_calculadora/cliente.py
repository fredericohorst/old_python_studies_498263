from pilha_p import pilha

from calculadora_cientifica import calc_cientifica

x = calc_cientifica()
# print(x.soma(2, 3))
# print(x.parse_rpn('1 2 +'))

y = input('digite a expressão: ') # input expression

z = x.infixTopostfix(y)
print(z)
print(x.parse_rpn(z))


# print(x.infixTopostfix('A * ( B + C ) * D'))

# 3 / 2 + 4 * 2

# (3 / 2) + 4 * 2 -- erro

# ( 3 / 2 ) + 4 * 2 -- 8