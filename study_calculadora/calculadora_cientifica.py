import tools
import math
from pilha_p import pilha
from calculadora import calc_basica


class calc_cientifica(calc_basica):

    p1 = {}
    data = {}
    op_mf = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}

    def __init__(self):
        self.p1[0] = ' '
        self.data[0] = ' '

    def parse_rpn(self, expression):

        Pilha = pilha()

        for val in expression.split(' '):
            if val in ['-', '+', '*', '/']:
                op1 = Pilha.desempilha()
                op2 = Pilha.desempilha()
                if val=='-': result = op2 - op1
                if val=='+': result = op2 + op1
                if val=='*': result = op2 * op1
                if val=='/': result = op2 / op1
                Pilha.empilha(result)
            elif val in ['^', 'r']:
              op1 = Pilha.desempilha()
              if val=='^': result = op1 * op1
              if val=='r': result = math.sqrt(op1)
              Pilha.empilha(result)
            else:
              Pilha.empilha(float(val))
        return Pilha.desempilha()

    def infixTopostfix(self, expression):

        listaRPN = []
        Opstack = pilha()
        tokenList = expression.split(' ')

        for token in tokenList:
            if tools.testnum(token) or tools.testpricaract(token):
                listaRPN.append(token)
            #elif token in '+-*/':
            elif tools.testop(token):
                if Opstack.tamanho() > 0:
                    if self.op_mf[Opstack.espia()] >= self.op_mf[token]:
                        listaRPN.append(Opstack.desempilha())
                Opstack.empilha(token)
            elif token == '(':
                Opstack.empilha(token)
            elif token == ')':
                t = Opstack.desempilha()
                while t != '(':
                    listaRPN.append(t)
                    t = Opstack.desempilha()

        while Opstack.tamanho() > 0:
            listaRPN.append(Opstack.desempilha())

        return ' '.join(listaRPN)
