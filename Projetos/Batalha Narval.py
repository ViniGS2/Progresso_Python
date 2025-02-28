tabuleirojogador1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

tabuleirojogador2 = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                     [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]


def exibe_jgr1():
    for i in range(10):
        for j in range(10):
            if tabuleirojogador2[i][j] == 9:
                print(' _ ', end=' ')
            elif tabuleirojogador2[i][j] == 1:
                print(' P ', end=' ')
        print()
def exibe_jgr2():
    for i in range(10):
        for j in range(10):
            if tabuleirojogador1[i][j] == 0:
                print(' _ ', end=' ')
            elif tabuleirojogador1[i][j] == -1:
                print(' S ', end=' ')
        print()
'''def exibe():
    for i in range(10):
        for j in range(10):
            if tabuleirojogador1[i][j] and tabuleirojogador2 == 0:
                print(' _ ', end=' ')
            elif tabuleirojogador2[i][j] == 1 and tabuleirojogador1[i][j] == -1:
                print(' _ ', end=' ')
            elif tabuleirojogador2[i][j] == 1:
                print(' _ ', end=' ')
            elif tabuleirojogador1[i][j] == -1:
                print(' _ ', end=' ')
            elif tabuleirojogador1[i][j] == 5:
                print(' P ', end=' ')
            elif tabuleirojogador2[i][j] == 5:
                print(' S ', end=' ')
'''
def jogo_posicionamento1():
    print('Fase de posicionamento.')
    print('Onde você gostaria de posicionar seus navios?')
    for i in range(9):
        exibe_jgr1()
        tipo_barco = int(input('Quantas casas o seu barco vai ocupar?[2][3][4][5]\n'))
        direcao = input('Você vai colocar o barco na horizontal[A] ou na vertical[B]?\n').upper()
        if direcao == 'A':
            jogada_linha = int(input('Linha: ')) - 1
            jogada_coluna = int(input('Coluna: ')) - 1
            tabuleirojogador2[jogada_linha][jogada_coluna] = 1
            for j in range(tipo_barco - 1):
                jogada_coluna = int(input('Coluna: ')) - 1
                tabuleirojogador2[jogada_linha][jogada_coluna] = 1
        elif direcao == 'B':
            jogada_linha = int(input('Linha: ')) - 1
            jogada_coluna = int(input('Coluna: ')) - 1
            tabuleirojogador2[jogada_linha][jogada_coluna] = 1
            for j in range(tipo_barco - 1):
                jogada_linha = int(input('Linha: ')) - 1
                tabuleirojogador2[jogada_linha][jogada_coluna] = 1
def jogo_posicionamento2():
    print('Fase de posicionamento.')
    print('Onde você gostaria de posicionar seus navios?')
    for i in range(9):
        exibe_jgr2()
        tipo_barco = int(input('Quantas casa o seu barco vai ocupar?[2][3][4][5]\n'))
        direcao = input('Você vai colocar o barco na horizontal[A] ou na vertical[B]?\n').upper()
        if direcao == 'A':
            jogada_linha = int(input('Linha: ')) - 1
            jogada_coluna = int(input('Coluna: ')) - 1
            tabuleirojogador1[jogada_linha][jogada_coluna] = -1
            for j in range(tipo_barco - 1):
                jogada_coluna = int(input('Coluna: ')) - 1
                tabuleirojogador1[jogada_linha][jogada_coluna] = -1
        elif direcao == 'B':
            jogada_linha = int(input('Linha: ')) - 1
            jogada_coluna = int(input('Coluna: ')) - 1
            tabuleirojogador1[jogada_linha][jogada_coluna] = -1
            for j in range(tipo_barco - 1):
                jogada_linha = int(input('Linha: ')) - 1
                tabuleirojogador1[jogada_linha][jogada_coluna] = -1

def game():
    try:
        jogada = 0
        while True:
            jogador = jogada % 2 + 1
            print(f'Vez do jogador {jogador}')
            print('Onde você quer atirar?\n')
            jogada_linha1 = int(input('Linha: '))
            jogada_coluna1 = int(input('Coluna: '))
            if jogador == 1:
                if tabuleirojogador1[jogada_linha1][jogada_coluna1] == 0:
                    print('Água!!')
                else:
                    print('Návio acertado.')
                    tabuleirojogador1[jogada_linha1][jogada_coluna1] = 5
            elif jogador == 2:
                if tabuleirojogador2[jogada_linha1][jogada_coluna1] == 0:
                    print('Água!!')
                else:
                    print('Návio acertado.')
                    tabuleirojogador2[jogada_linha1][jogada_coluna1] = 5
    except EOFError:
        print('Error')

jogo_posicionamento1()
jogo_posicionamento2()
game()