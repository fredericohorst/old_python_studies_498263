__author__ = 'frederico'

from tabuleiro import tabuleiro

# Type of ship               | Size | Legenda
# Aircraft carrier      	    5       ac
# Battleship        	        4       b
# Submarine                     3       s
# Destroyer (or Cruiser)	    3       d
# Patrol boat (or destroyer)	2       pb
barcos = {'ac': 5, 'b': 4, 's': 3, 'd': 3, 'pb': 2}


x = input('digite a quantidade de linhas: ')
y = input('digite a quantidade de colunas: ')
z = 'M'

t = tabuleiro(x, y, z)
print(t.M)
print(t.M[0])


print('tabuleiro criado com sucesso. vc tem direito a 5 navios (um de cada tipo)')
m = 0
a = []
b = []
while m < 5:
    a = input('digite a coordenadas iniciais: ')
    b = input('digite a coordenadas finais: ')
    c = input('tipo: ')
    # marcando a
    a_in = int(a[0:1])
    a_fi = int(a[3:4])
    # marcando b
    b_in = int(b[0:1])
    b_fi = int(b[3:4])

    t.posicao(a_in, a_fi, b_in, b_fi)

    m = m + 1







# tabuleiro.m(a, b, 'x')

#

# '\n'

