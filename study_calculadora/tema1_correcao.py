#
# import tools
#
# x = input('digite alguma coisa - ')
#
# print('teste string - ', bool(tools.teststring(x)))
#
# print('teste expressao - ', bool(tools.testexpress(x)))
#
# print('teste numeral - ', bool(tools.testnum(x)))
#
# print('teste operacao - ', bool(tools.testop(x)))
#
# print('teste primeiro caractere - ', bool(tools.testpricaract(x)))
#


import knu
resultado = knu.receitaCNPJ("00000000000191")
print("Situacao cadastral: ",resultado.situacao_cadastral,"\n")