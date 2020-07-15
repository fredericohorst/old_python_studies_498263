class cronometro:
    hora = 0
    minuto = 0
    segundo = 0
    # f = open('results.txt', 'w')

    @staticmethod
    def inicio():
        f = open('results.txt', 'w')
        for hora in range(0, 24):
            for minuto in range(0, 59):
                for segundo in range(0, 59):
                    f.write(str(hora) + ':' + str(minuto) + ':' + str(segundo) + '\n')
