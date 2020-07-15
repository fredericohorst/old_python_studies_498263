__author__ = 'frederico'


# exercício 13

class tabuleiro:
    M = []
    f = open('battlefield.txt', 'w')


    def __init__(self, x, y, z):
        self.M = int(x) * [int(y) * [z]]
        self.f.write(str(self.M) + '\n')

    def marcar(self, x, y):
    #     x = linha
    #     y = coluna

        # self.M[x][y] delete?
        self.M[x][y] = 'X'
        z = 'X'
        self.f.write(str(self.M[x][y]) + '\n')  #????


    def posicao(self, a_in, a_fi, b_in, b_fi):
        self.marcar(a_in, a_fi)
        self.marcar(b_in, b_fi)
        d1 = b_fi - a_fi
        d2 = b_in - a_in
        if a_in == b_in:
            while d1 > 0:
                self.marcar(a_in, d1)
                d1 = d1 - 1
        elif a_fi == b_fi:
            while d2 > 0:
                self.marcar(a_fi, d2)
                d2 = d2 - 1


    # def jogada(self, x, y):
    #     # x = linha
    #     # y = coluna
    #     if self.M[x][y] == 'M':
    #         print('errou')
    #     else return print('z')