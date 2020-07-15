class pilha:

    __dados_internos = None
    __ult_pos = None

    def __init__(self):
        self.__dados_internos = []
        self.__ult_pos = 0

    def empilha(self, x):
        self.__dados_internos.insert(self.__ult_pos, x)
        self.__ult_pos = self.__ult_pos + 1

    def desempilha(self):
        z = self.__dados_internos[self.__ult_pos - 1]
        del self.__dados_internos[self.__ult_pos - 1]
        self.__ult_pos = self.__ult_pos - 1
        return z
        # print('voce tem certeza que deseja deletar ' + z + '?')

    def espia(self):
        z = self.__dados_internos[self.__ult_pos - 1]
        return z

    def tamanho(self):
        return self.__ult_pos