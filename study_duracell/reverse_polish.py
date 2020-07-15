import math
def parse_rpn(expression):

  Pilha = []

  for val in expression.split(' '):
      if val in ['-', '+', '*', '/']:
          op1 = Pilha.pop()
          op2 = Pilha.pop()
          if val=='-': result = op2 - op1
          if val=='+': result = op2 + op1
          if val=='*': result = op2 * op1
          if val=='/': result = op2 / op1
          Pilha.append(result)
      elif val in ['^', 'r']:
          op1 = Pilha.pop()
          if val=='^': result = op1 * op1
          if val=='r': result = math.sqrt(op1)
          Pilha.append(result)
      else:
          Pilha.append(float(val))
  return Pilha.pop()
