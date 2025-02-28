horas = input().split()
inicio = int(horas[0])
fim = int(horas[1])

if fim <= inicio or fim == 0:
    fim1 = fim + 24
    hrs1 = range(inicio, fim1)
    print(f'O JOGO DUROU {len(hrs1)} HORA(S)')

elif fim > inicio:
    hrs2 = range(inicio, fim)
    print(f'O JOGO DUROU {len(hrs2)} HORA(S)')
