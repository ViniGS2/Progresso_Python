import time
from random import randint
import emoji
from time import sleep
import os
from ranking import ver_ranking, atualizar_ranking_crescente

# bomba = -1
# lugar sem nada = 0
# 100 passa a representar 0 apos o jogador o encontrar
# -10 passa a representar bomba apos o jogador encontrar
# os outros serão multiplicados por 200 para diferenciar
# número de bombas aleatório//a medida que a dificuldade aumenta é randomizada entre menos números

'''login'''
def menu_login():
    ########## login ##########
    print('o' + '~' * 81 + 'o')
    print(
        f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
    print('o' + '~' * 81 + 'o')
    print()
    nome_do_jogador = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(2)
    os.system('cls')
    return nome_do_jogador
    ########## login ##########

'''TABULEIRO FÁCIL'''

tabuleiro_facil = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]

# função que desenvolve o tabuleiro
def corpo_do_jogo_facil():

    tabuleiro_aleatorio_facil = [[0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0]]



    # aleatoriza as bombas do tabuleiro fácil
    for linha in range(0, 8):
        for quant in range(1):
            coluna = randint(0, 7)
            tabuleiro_aleatorio_facil[linha][coluna] = -1

    # transfere para o tabuleiro final fácil
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if tabuleiro_aleatorio_facil[linha][coluna] == 0:
                tabuleiro_facil[linha][coluna] = 0
            elif tabuleiro_aleatorio_facil[linha][coluna] == -1:
                tabuleiro_facil[linha][coluna] = -1

    # posiciona as dicas do tabuleiro fácil
    for linha in range(0, 8):
        for coluna in range(len(tabuleiro_facil)):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna + 1]
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna - 1]
                elif 0 < coluna < 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                        coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + tabuleiro_aleatorio_facil[linha][
                                coluna + 1]
            # linha de baixo
            elif linha == 7:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna + 1] + \
                            tabuleiro_aleatorio_facil[linha - 1][coluna]
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha - 1][coluna]
                elif 0 < coluna < 7:
                    soma = tabuleiro_aleatorio_facil[linha][coluna - 1] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha - 1][coluna] + \
                            tabuleiro_aleatorio_facil[linha - 1][coluna + 1] + tabuleiro_aleatorio_facil[linha][
                                coluna + 1]
            # linhas do meio
            elif 0 < linha < 7:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna + 1] + \
                            tabuleiro_aleatorio_facil[linha][coluna + 1] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + tabuleiro_aleatorio_facil[linha + 1][
                                coluna]
                # coluna da direita
                elif coluna == 7:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha][coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                                coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_facil[linha - 1][coluna] + tabuleiro_aleatorio_facil[linha - 1][
                        coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha][coluna - 1] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna - 1] + tabuleiro_aleatorio_facil[linha + 1][
                                coluna] + \
                            tabuleiro_aleatorio_facil[linha + 1][coluna + 1] + \
                            tabuleiro_aleatorio_facil[linha][coluna + 1] + tabuleiro_aleatorio_facil[linha - 1][
                                coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_facil[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_facil[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_facil[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_facil[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_facil[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_facil[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_facil[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_facil[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_facil[linha][coluna] = 8

def exibe_tabuleiro_facil():
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if linha == 0 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 8\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 8\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 8\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 8\033[m    -  ', end='')
            elif 0 < linha < 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_facil[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_facil():
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if linha == 0 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 8\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 8\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 8\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 8\033[m    -  ', end='')
            elif 0 < linha < 7 and coluna == 0:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_facil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_facil[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_facil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_facil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_facil():
    try:
        nick = menu_login()
        corpo_do_jogo_facil()
        game_over = 0
        tempo_inicial = time.time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                     \033[0;31; m 1    2    3    4    5    6    7    8\033[m')
            print()
            exibe_tabuleiro_facil()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                elif coluna == 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1]:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100

                elif coluna == 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                elif 0 < coluna < 7:
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 7:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 7:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_facil[linha - 1][coluna] == 0:
                        tabuleiro_facil[linha - 1][coluna] = 100
                    if tabuleiro_facil[linha - 1][coluna - 1] == 0:
                        tabuleiro_facil[linha - 1][coluna - 1] = 100
                    if tabuleiro_facil[linha][coluna - 1] == 0:
                        tabuleiro_facil[linha][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna - 1] == 0:
                        tabuleiro_facil[linha + 1][coluna - 1] = 100
                    if tabuleiro_facil[linha + 1][coluna] == 0:
                        tabuleiro_facil[linha + 1][coluna] = 100
                    if tabuleiro_facil[linha + 1][coluna + 1] == 0:
                        tabuleiro_facil[linha + 1][coluna + 1] = 100
                    if tabuleiro_facil[linha][coluna + 1] == 0:
                        tabuleiro_facil[linha][coluna + 1] = 100
                    if tabuleiro_facil[linha - 1][coluna + 1] == 0:
                        tabuleiro_facil[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_facil[linha][coluna] < 10:
                if tabuleiro_facil[linha][coluna] == 0:
                    tabuleiro_facil[linha][coluna] = 100
                elif tabuleiro_facil[linha][coluna] == -1:
                    tabuleiro_facil[linha][coluna] = -10
                else:
                    tabuleiro_facil[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_facil()
            if teste_gameover_facil() == 1:
                game_over = 1
            elif teste_gameover_facil() == 2:
                game_over = 2
        os.system('cls')
        print('o' + '~' * 81 + 'o')
        print(
            f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
        print('o' + '~' * 81 + 'o')
        print()
        print()
        print('                     \033[0;31; m 1    2    3    4    5    6    7    8\033[m')
        print()
        mostra_bomba_fim_facil()
        tempo_final = time.time()
        tempo_de_partida_facil = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_facil:.2f}s')
        print()
        pontos_partida_facil = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_facil = 25
        print()
        # sistema de pontuação
        if tempo_de_partida_facil < 60:
            pontos_totais_facil = pontos_partida_facil * 2
        elif 60 < tempo_de_partida_facil < 180:
            pontos_totais_facil = pontos_partida_facil * 1.5
        elif 180 < tempo_de_partida_facil < 300:
            pontos_totais_facil = pontos_partida_facil * 1.25
        else:
            pontos_totais_facil = pontos_partida_facil
        # atualiza o rank
        atualizar_ranking_crescente('C:/Users/vinic/PycharmProjects/pythonProject/Rank_campo_minado', nome=nick, pontuacao=pontos_totais_facil)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu()
        else:
            print('Saindo...')
            print()
            sleep(3)
        ###################################3####
    except:
        print('Error')
        os.system('cls')
        menu()
def teste_gameover_facil():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 8):
        for coluna in range(0, 8):
            if tabuleiro_facil[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_facil[linha][coluna] == -10:
                return 1
            if tabuleiro_facil[linha][coluna] >= 200 or tabuleiro_facil[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 64 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2


'''TABULEIRO MÉDIO'''

tabuleiro_medio = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def corpo_do_jogo_medio():
    tabuleiro_aleatorio_medio = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # aleatoriza as bombas do tabuleiro medio
    for linha in range(0, 9):
        for quant in range(2):
            coluna = randint(0, 8)
            tabuleiro_aleatorio_medio[linha][coluna] = -1

    # transfere as bombas para o tabuleiro final facil
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if tabuleiro_aleatorio_medio[linha][coluna] == 0:
                tabuleiro_medio[linha][coluna] = 0
            elif tabuleiro_aleatorio_medio[linha][coluna] == -1:
                tabuleiro_medio[linha][coluna] = -1

    # posiciona as dicas do tabuleiro facil
    for linha in range(0, 9):
        for coluna in range(len(tabuleiro_medio)):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1]
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1]
                elif 0 < coluna < 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + tabuleiro_aleatorio_medio[linha][
                               coluna + 1]
            # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna]
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna]
                elif 0 < coluna < 8:
                    soma = tabuleiro_aleatorio_medio[linha][coluna - 1] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna] + \
                           tabuleiro_aleatorio_medio[linha - 1][coluna + 1] + tabuleiro_aleatorio_medio[linha][
                               coluna + 1]
            # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna]
                # coluna da direita
                elif coluna == 8:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_medio[linha - 1][coluna] + tabuleiro_aleatorio_medio[linha - 1][
                        coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna - 1] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna - 1] + tabuleiro_aleatorio_medio[linha + 1][
                               coluna] + \
                           tabuleiro_aleatorio_medio[linha + 1][coluna + 1] + \
                           tabuleiro_aleatorio_medio[linha][coluna + 1] + tabuleiro_aleatorio_medio[linha - 1][
                               coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_medio[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_medio[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_medio[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_medio[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_medio[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_medio[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_medio[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_medio[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_medio[linha][coluna] = 8

def exibe_tabuleiro_medio():
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if linha == 0 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 9\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 9\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 9\033[m    -  ', end='')
            elif 0 < linha < 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_medio[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'  {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_medio():
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if linha == 0 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 1\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 1\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 1\033[m    -  ', end='')
            elif linha == 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 9\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 9\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 9\033[m    -  ', end='')
            elif 0 < linha < 8 and coluna == 0:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'\033[0;31; m                 {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m                 {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_medio[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_medio[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_medio[linha][coluna] >= 200:
                    print(f'  {tabuleiro_medio[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_medio():
    try:
        nick = menu_login()
        corpo_do_jogo_medio()
        game_over = 0
        tempo_inicial = time.time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                     \033[0;31; m 1    2    3    4    5    6    7    8    9\033[m')
            print()
            exibe_tabuleiro_medio()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                elif coluna == 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1]:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100

                elif coluna == 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 8:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_medio[linha - 1][coluna] == 0:
                        tabuleiro_medio[linha - 1][coluna] = 100
                    if tabuleiro_medio[linha - 1][coluna - 1] == 0:
                        tabuleiro_medio[linha - 1][coluna - 1] = 100
                    if tabuleiro_medio[linha][coluna - 1] == 0:
                        tabuleiro_medio[linha][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna - 1] == 0:
                        tabuleiro_medio[linha + 1][coluna - 1] = 100
                    if tabuleiro_medio[linha + 1][coluna] == 0:
                        tabuleiro_medio[linha + 1][coluna] = 100
                    if tabuleiro_medio[linha + 1][coluna + 1] == 0:
                        tabuleiro_medio[linha + 1][coluna + 1] = 100
                    if tabuleiro_medio[linha][coluna + 1] == 0:
                        tabuleiro_medio[linha][coluna + 1] = 100
                    if tabuleiro_medio[linha - 1][coluna + 1] == 0:
                        tabuleiro_medio[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_medio[linha][coluna] < 10:
                if tabuleiro_medio[linha][coluna] == 0:
                    tabuleiro_medio[linha][coluna] = 100
                elif tabuleiro_medio[linha][coluna] == -1:
                    tabuleiro_medio[linha][coluna] = -10
                else:
                    tabuleiro_medio[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_medio()
            if teste_gameover_medio() == 1:
                game_over = 1
            elif teste_gameover_medio() == 2:
                game_over = 2
        os.system('cls')
        print('                     \033[0;31; m 1    2    3    4    5    6    7    8    9\033[m')
        print()
        mostra_bomba_fim_medio()
        tempo_final = time.time()
        tempo_de_partida_medio = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_medio:.2f}s')
        print()
        pontos_partida_media = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_media = 50
        print()
        # sistema de pontuação
        if tempo_de_partida_medio < 60:
            pontos_totais_medio = pontos_partida_media * 2
        elif 60 < tempo_de_partida_medio < 180:
            pontos_totais_medio = pontos_partida_media * 1.5
        elif 180 < tempo_de_partida_medio < 300:
            pontos_totais_medio = pontos_partida_media * 1.25
        else:
            pontos_totais_medio = pontos_partida_media
        # atualiza o rank
        atualizar_ranking_crescente('C:/Users/vinic/PycharmProjects/pythonProject/Rank_campo_minado', nome=nick, pontuacao=pontos_totais_medio)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu()
        else:
            print('Saindo...')
            print()
            sleep(3)
        #######################################
    except:
        print('Error')
        os.system('cls')
        menu()
def teste_gameover_medio():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if tabuleiro_medio[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_medio[linha][coluna] == -10:
                return 1
            if tabuleiro_medio[linha][coluna] >= 200 or tabuleiro_medio[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 81 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2


'''TABULEIRO DIFICIL'''

tabuleiro_dificil = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def corpo_do_jogo_difícil():

    tabuleiro_aleatorio_dificil = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # aleatoriza o tabuleiro dificil
    for linha in range(0, 10):
        for quant in range(3):
            coluna = randint(0, 9)
            tabuleiro_aleatorio_dificil[linha][coluna] = -1

    # transfere para o tabuleiro dificil final
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if tabuleiro_aleatorio_dificil[linha][coluna] == 0:
                tabuleiro_dificil[linha][coluna] = 0
            elif tabuleiro_aleatorio_dificil[linha][coluna] == -1:
                tabuleiro_dificil[linha][coluna] = -1

    # posiciona as dicas do dificil
    for linha in range(0, 10):
        for coluna in range(0, 10):
            # teste de bombas
            soma = 0
            # linha de cima
            if linha == 0:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1]
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1]
                elif 0 < coluna < 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha][coluna + 1]
            # linha de baixo
            elif linha == 9:
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha - 1][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna]
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha - 1][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna]
                elif 0 < coluna < 9:
                    soma = tabuleiro_aleatorio_dificil[linha][coluna - 1] + tabuleiro_aleatorio_dificil[linha - 1][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha - 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha][coluna + 1]
            # linhas do meio
            elif 0 < linha < 9:
                # coluna da esquerda
                if coluna == 0:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna]
                # coluna da direita
                elif coluna == 9:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna]
                # meio do tabuleiro
                else:
                    soma = tabuleiro_aleatorio_dificil[linha - 1][coluna] + tabuleiro_aleatorio_dificil[linha - 1][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna - 1] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna - 1] + tabuleiro_aleatorio_dificil[linha + 1][coluna] + \
                           tabuleiro_aleatorio_dificil[linha + 1][coluna + 1] + \
                           tabuleiro_aleatorio_dificil[linha][coluna + 1] + tabuleiro_aleatorio_dificil[linha - 1][coluna + 1]
            # quantidade de bombas
            if soma != 0 and tabuleiro_aleatorio_dificil[linha][coluna] != -1:
                if soma == -1:
                    tabuleiro_dificil[linha][coluna] = 1
                elif soma == -2:
                    tabuleiro_dificil[linha][coluna] = 2
                elif soma == -3:
                    tabuleiro_dificil[linha][coluna] = 3
                elif soma == -4:
                    tabuleiro_dificil[linha][coluna] = 4
                elif soma == -5:
                    tabuleiro_dificil[linha][coluna] = 5
                elif soma == -6:
                    tabuleiro_dificil[linha][coluna] = 6
                elif soma == -7:
                    tabuleiro_dificil[linha][coluna] = 7
                elif soma == -8:
                    tabuleiro_dificil[linha][coluna] = 8

def teste_gameover_dificil():
    quant_bombs = 0
    quant_jogadas = 0
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if tabuleiro_dificil[linha][coluna] == -1:
                quant_bombs += 1
            if tabuleiro_dificil[linha][coluna] == -10:
                return 1
            if tabuleiro_dificil[linha][coluna] >= 200 or tabuleiro_dificil[linha][coluna] == 100:
                quant_jogadas += 1
    lugares_disponiveis = 100 - quant_bombs
    if lugares_disponiveis == quant_jogadas:
        return 2

# exibe o tabuleiro
def exibe_tabuleiro_dificil():
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if linha == 0 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            1\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            1\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            1\033[m    -  ', end='')
            elif linha == 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            10\033[m   0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            10\033[m{emoji.emojize('   :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            10\033[m   {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            10\033[m   -  ', end='')
            elif 0 < linha < 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'\033[0;31; m            {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            {linha + 1}\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_dificil[linha][coluna] == -10:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def mostra_bomba_fim_dificl():
    for linha in range(0, 10):
        for coluna in range(0, 10):
            if linha == 0 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            1\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            1\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            1\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            1\033[m    -  ', end='')
            elif linha == 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            9\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            9\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            9\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            9\033[m    -  ', end='')
            elif 0 < linha < 9 and coluna == 0:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'\033[0;31; m            {linha + 1}\033[m    0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'\033[0;31; m            {linha + 1}\033[m{emoji.emojize('    :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'\033[0;31; m            {linha + 1}\033[m    {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'\033[0;31; m            {linha + 1}\033[m    -  ', end='')
            else:
                if tabuleiro_dificil[linha][coluna] == 100:
                    print(f'  0  ', end='')
                elif tabuleiro_dificil[linha][coluna] < 0:
                    print(f'{emoji.emojize('  :bomb: ')}', end='')
                elif tabuleiro_dificil[linha][coluna] >= 200:
                    print(f'  {tabuleiro_dificil[linha][coluna] / 200:.0f}  ', end='')
                else:
                    print(f'  -  ', end='')

        print()
        print()


def jogo_dificil():
    try:
        nick = menu_login()
        corpo_do_jogo_difícil()
        game_over = 0
        tempo_inicial = time.time()
        while game_over == 0:
            os.system('cls')
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            print('                \033[0;31; m 1    2    3    4    5    6    7    8    9    10\033[m')
            print()
            exibe_tabuleiro_dificil()
            linha = int(input('Linha: ')) - 1
            coluna = int(input('Coluna: ')) - 1
            # revela zeros próximos
            if linha == 0:
                if coluna == 0:
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                elif coluna == 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1]:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                # linha de baixo
            elif linha == 8:
                if coluna == 0:
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100

                elif coluna == 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                elif 0 < coluna < 8:
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                # linhas do meio
            elif 0 < linha < 8:
                # coluna da esquerda
                if coluna == 0:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                # coluna da direita
                elif coluna == 8:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                # meio do tabuleiro
                else:
                    if tabuleiro_dificil[linha - 1][coluna] == 0:
                        tabuleiro_dificil[linha - 1][coluna] = 100
                    if tabuleiro_dificil[linha - 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha][coluna - 1] == 0:
                        tabuleiro_dificil[linha][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna - 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna - 1] = 100
                    if tabuleiro_dificil[linha + 1][coluna] == 0:
                        tabuleiro_dificil[linha + 1][coluna] = 100
                    if tabuleiro_dificil[linha + 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha + 1][coluna + 1] = 100
                    if tabuleiro_dificil[linha][coluna + 1] == 0:
                        tabuleiro_dificil[linha][coluna + 1] = 100
                    if tabuleiro_dificil[linha - 1][coluna + 1] == 0:
                        tabuleiro_dificil[linha - 1][coluna + 1] = 100
            if -2 < tabuleiro_dificil[linha][coluna] < 10:
                if tabuleiro_dificil[linha][coluna] == 0:
                    tabuleiro_dificil[linha][coluna] = 100
                elif tabuleiro_dificil[linha][coluna] == -1:
                    tabuleiro_dificil[linha][coluna] = -10
                else:
                    tabuleiro_dificil[linha][coluna] *= 200
            else:
                print(f'Você já jogou nessa posição.\nTente novamente!')
            teste_gameover_dificil()
            if teste_gameover_dificil() == 1:
                game_over = 1
            elif teste_gameover_dificil() == 2:
                game_over = 2
        os.system('cls')
        print('                \033[0;31; m 1    2    3    4    5    6    7    8    9    10\033[m')
        print()
        mostra_bomba_fim_dificl()
        tempo_final = time.time()
        tempo_de_partida_dificil = tempo_final - tempo_inicial
        print()
        print(f'TEMPO DE PARTIDA: {tempo_de_partida_dificil:.2f}s')
        print()
        pontos_partida_dificil = 0
        if game_over == 1:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_chorando:', language='pt')}Você perdeu!{emoji.emojize(':rosto_chorando:', language='pt')}')
        elif game_over == 2:
            print(f'{emoji.emojize(':fireworks:')}Fim do jogo!{emoji.emojize(':fireworks:')}\n\
{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}Você Ganhou!{emoji.emojize(':rosto_risonho_com_olhos_sorridentes:', language='pt')}')
            pontos_partida_dificil = 100
        print()
        # sistema de pontuação
        if tempo_de_partida_dificil < 60:
            pontos_totais_dificil = pontos_partida_dificil * 2
        elif 60 < tempo_de_partida_dificil < 180:
            pontos_totais_dificil = pontos_partida_dificil * 1.5
        elif 180 < tempo_de_partida_dificil < 300:
            pontos_totais_dificil = pontos_partida_dificil * 1.25
        else:
            pontos_totais_dificil = pontos_partida_dificil
        # atualiza o rank
        atualizar_ranking_crescente('C:/Users/vinic/PycharmProjects/pythonProject/Rank_campo_minado', nome=nick, pontuacao=pontos_totais_dificil)
        ########################################
        print('Voltar para o menu?')
        print()
        sim_nao = input('[S]Sim\n\n[N]Não\n\nDigite: ').upper()
        if sim_nao == 'S':
            os.system('cls')
            menu()
        else:
            print('Saindo...')
            print()
            sleep(3)
        #######################################
    except:
        print('Error')
        os.system('cls')
        menu()

'''MENU'''


def menu():
    cont = 1
    while cont == 1:
        print('o' + '~' * 81 + 'o')
        print(f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
        print('o' + '~' * 81 + 'o')
        print()
        print()
        print(' TUTORIAL          COMEÇAR A JOGAR          RANKING          VOLTAR PARA O INICIO')
        print('   [T]                   [J]                  [R]                    [I]')
        print()
        comecar = input('Digite: ').upper()
        os.system("cls")
        if comecar == 'J':
            print('o' + '~' * 81 + 'o')
            print(
                f'                             {emoji.emojize(':bomb:   ')}{'\033[0;31; mCAMPO MINADO\033[m'}{emoji.emojize('   :bomb:')}')
            print('o' + '~' * 81 + 'o')
            print()
            print()
            cont -= 1
            opcao = input('Qual a dificuldade em que você deseja jogar?\n\n[F]FÁCIL\n\n[M]MÉDIO\n\n[D]DIFÍCIL\n\n').upper()
            os.system('cls')
            if opcao == 'F':
                os.system('cls')
                jogo_facil()
            elif opcao == 'M':
                os.system('cls')
                jogo_medio()
            elif opcao == 'D':
                os.system("cls")
                jogo_dificil()
            else:
                os.system('cls')
                menu()
        elif comecar == 'T':
            os.system("cls")
            print('''O jogo é um campo minado simples, onde o seu objetivo é descobrir todas as posições sem bombas.

O número que lhe aparecer mostra a quantidade de bombas presentes ao redor dele.

Se o número que você revelar tiver zeros ao seu redor, ele os revelará.  

    Existem três dificuldades:
FÁCIL: Tabuleiro 8x8 e 1 bomba por linha
MÈDIO: Tabuleiro 9x9 e 2 bombas por linha
DIFÌCIL: Tabuleiro 10x10 e 3 bombas por linha

Vamos Jogar?
''')
            sim_nao = input('[S]Sim\n[N]Não\n\nDigite: ').upper()
            if sim_nao == 'S':
                os.system('cls')
            else:
                print('Saindo...')
        elif comecar == 'R':
            ver_ranking('C:/Users/vinic/PycharmProjects/pythonProject/Rank_campo_minado')
            print()
            voltar = input('Aperte enter para voltar')
            os.system('cls')
        elif comecar == 'I':
            cont -= 1
            print('Saindo...')
            sleep(3)
        else:
            print('Resposta inválida. Tente novamente!')


menu()