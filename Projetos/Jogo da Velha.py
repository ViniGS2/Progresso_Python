from random import randint
from time import sleep, time
import os
from ranking import atualizar_ranking_crescente, ver_ranking
'''login'''
def menu_login_jogador1():
    ########## login ##########
    nome_do_jogador1 = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(1)
    os.system('cls')
    return nome_do_jogador1
    ########## login ##########

def menu_login_jogador2():
    ########## login ##########
    nome_do_jogador2 = input('Digite o seu nickname: ').upper().strip()
    print()
    print('Carregando', end='')
    print('.', end='')
    print('.', end='')
    print('.')
    sleep(1)
    os.system('cls')
    return nome_do_jogador2
    ########## login ##########


def menu_inicio_jogo_da_velha():
    try:
        cont = 1
        while cont == 1:
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            print('           TUTORIAL            JOGAR         RANKING       SAIR PARA O MENU')
            print('             [T]                [J]            [R]               [S]')
            print()
            comecar = input('DIGITE: ').upper().strip()
            if comecar == 'J':
                trava = 0
                while trava == 0:
                    os.system('cls')
                    print(f'X{'O JOGO DA VELHA X':=^80}O')
                    print()
                    opcao = input('Escolha um modo de jogo:\n\nPVP[A]\n\nPVE[B]\n\nDIGITE: ').upper().strip()
                    if opcao == 'A':
                        cont -= 1
                        trava = 1
                        Jogo_da_velha()
                    elif opcao == 'B':
                        cont -= 1
                        trava = 1
                        jogo_da_velha_maquina()
                    else:
                        print('Opção invalida!')
            elif comecar == 'T':
                os.system('cls')
                print('''Este é um jogo da velha comum onde seu objetivo é vencer, completando uma coluna, linha ou diagonal com a figura que lhe representa.
                
Você pode jogar contra um amigo ou contra o próprio computador.
                
Você jogará informando uma linha e uma coluna referente à posição que quer jogar.
                
Vamos jogar?[S/N]
                ''')
                resposta = input('DIGITE: ').upper().strip()
                os.system('cls')
                if resposta == 'N':
                    cont -= 1
                    # voltar para o menu principal
                    print('Saindo...')
                    sleep(2)
            elif comecar == 'S':
                cont -= 1
                # volta para o menu principal
                print('Saindo...')
                sleep(2)
            elif comecar == 'R':
                os.system('cls')
                ver_ranking('Rank Jogo da Velha')
                print()
                voltar = input('Aperte enter para voltar')
                os.system('cls')
            else:
                print('Resposta inválida. Tente novamente!')
    except:
        if not KeyboardInterrupt:
            print('ERROR')
            menu_inicio_jogo_da_velha()


def Jogo_da_velha():
    try:

        tabuleiro = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        print('Jogador 1')
        print()
        nick_jogador1 = menu_login_jogador1()
        print('Jogador 2')
        print()
        nick_jogador2 = menu_login_jogador2()
        jogada_geral = 0
        jogada_jogador1 = 0
        jogada_jogador2 = 0
        pontos_jogador1 = 0
        pontos_jogador2 = 0
        while ganhou(tabuleiro) == 0:
            os.system('cls')
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            jogador = jogada_geral % 2 + 1
            print(f'Vez do jogador {jogador}')
            print()
            exibe(tabuleiro)
            print()
            jogada_linha = int(input('Linha: ')) - 1
            inicio = time()
            jogada_coluna = int(input('Coluna: ')) - 1
            if jogador == 1:
                jogada_jogador1 += 1
            elif jogador == 2:
                jogada_jogador2 += 1
            if tabuleiro[jogada_linha][jogada_coluna] == 0:
                if jogador == 1:
                    tabuleiro[jogada_linha][jogada_coluna] = 1
                else:
                    tabuleiro[jogada_linha][jogada_coluna] = -1
            else:
                print('Já foi ocupado!')
                jogada_geral -= 1
            if ganhou(tabuleiro) == 1:
                fim = time()
                tempo_partida = fim - inicio
                if jogador == 1:
                    if jogada_jogador1 <= 3:
                        pontos_jogador1 = 90
                    elif jogada_jogador1 > 3:
                        pontos_jogador1 = 30
                    if tempo_partida < 60:
                        pontos_jogador1 = pontos_jogador1 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador1 = pontos_jogador1 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador1 = pontos_jogador1 * 1.25
                    else:
                        pontos_jogador1 = pontos_jogador1
                elif jogador == 2:
                    if jogada_jogador2 <= 3:
                        pontos_jogador2 = 90
                    elif jogada_jogador2 > 3:
                        pontos_jogador2 = 30
                    if tempo_partida < 60:
                        pontos_jogador2 = pontos_jogador2 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador2 = pontos_jogador2 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador2 = pontos_jogador2 * 1.25
                    else:
                        pontos_jogador2 = pontos_jogador2
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador2, pontos_jogador2)
                exibe(tabuleiro)
                print(f'Parabéns Jogador {jogador}! Você ganhou após {jogada_geral + 1} rodadas.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            elif ganhou(tabuleiro) == 2:
                fim = time()
                pontos_jogador1 = 10
                pontos_jogador2 = 10
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador2, pontos_jogador2)
                exibe(tabuleiro)
                print(f'Velha! Ótima partida, pessoal.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            jogada_geral += 1
    except:
        if not KeyboardInterrupt:
            print('Error')
            print('Reiniciando...')
            menu_inicio_jogo_da_velha()
def ganhou(tabuleiro):
    #linhas
    if tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][2] == 3 or tabuleiro[0][0] + tabuleiro[0][1] + tabuleiro[0][
        2] == -3:
        return 1
    if tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][2] == 3 or tabuleiro[1][0] + tabuleiro[1][1] + tabuleiro[1][
        2] == -3:
        return 1
    if tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][2] == 3 or tabuleiro[2][0] + tabuleiro[2][1] + tabuleiro[2][
        2] == -3:
        return 1
    #colunas
    if tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][0] == 3 or tabuleiro[0][0] + tabuleiro[1][0] + tabuleiro[2][
        0] == -3:
        return 1
    if tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][1] == 3 or tabuleiro[0][1] + tabuleiro[1][1] + tabuleiro[2][
        1] == -3:
        return 1
    if tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][2] == 3 or tabuleiro[0][2] + tabuleiro[1][2] + tabuleiro[2][
        2] == -3:
        return 1
    #diagonais
    if tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2] == 3 or tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][
        2] == -3:
        return 1
    if tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0] == 3 or tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][
        0] == -3:
        return 1
    #empate
    cont = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != 0:
                cont += 1
    if cont == 9:
        return 2

    return 0


def exibe(tabuleiro):
    for i in range(3):
        for j in range(3):
            if j == 0:
                if tabuleiro[i][j] == 0:
                    print('                                  _  ', end=' ')
                elif tabuleiro[i][j] == 1:
                    print('                                  X  ', end=' ')
                elif tabuleiro[i][j] == -1:
                    print('                                  O  ', end=' ')
            else:
                if tabuleiro[i][j] == 0:
                    print('  _  ', end=' ')
                elif tabuleiro[i][j] == 1:
                    print('  X  ', end=' ')
                elif tabuleiro[i][j] == -1:
                    print('  O  ', end=' ')
        print()
        print()



def jogo_da_velha_maquina():

    tabuleiro = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    try:
        print('Jogador 1')
        print()
        nick_jogador1 = menu_login_jogador1()
        jogada_jogador1 = 0
        pontos_jogador1 = 0
        jogada_geral = 0
        while ganhou(tabuleiro) == 0:
            os.system('cls')
            print(f'X{'O JOGO DA VELHA X':=^80}O')
            print()
            jogador = jogada_geral % 2 + 1
            print(f'Vez do jogador {jogador}')
            exibe(tabuleiro)
            if jogador == 2:
                print('Pensando.', end='')
                sleep(1)
                print('.', end='')
                sleep(1)
                print('.')
                jogada_linha = randint(1, 3) - 1
                jogada_coluna = randint(1, 3) - 1
            else:
                if jogador == 1:
                    jogada_jogador1 += 1
                jogada_linha = int(input('Linha: ')) - 1
                inicio = time()
                jogada_coluna = int(input('Coluna: ')) - 1
            if tabuleiro[jogada_linha][jogada_coluna] == 0:
                if jogador == 1:
                    tabuleiro[jogada_linha][jogada_coluna] = 1
                else:
                    tabuleiro[jogada_linha][jogada_coluna] = -1
            else:
                print('Já foi ocupado!')
                jogada_geral -= 1
            if ganhou(tabuleiro) == 1:
                fim = time()
                tempo_partida = fim - inicio
                if jogador == 1:
                    if jogada_jogador1 <= 3:
                        pontos_jogador1 = 90
                    elif jogada_jogador1 > 3:
                        pontos_jogador1 = 30
                    if tempo_partida < 60:
                        pontos_jogador1 = pontos_jogador1 * 2
                    elif 60 < tempo_partida < 180:
                        pontos_jogador1 = pontos_jogador1 * 1.5
                    elif 180 < tempo_partida < 300:
                        pontos_jogador1 = pontos_jogador1 * 1.25
                    else:
                        pontos_jogador1 = pontos_jogador1
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                exibe(tabuleiro)
                print(f'Parabéns Jogador {jogador}! Você ganhou após {jogada_geral + 1} rodadas.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            elif ganhou(tabuleiro) == 2:
                fim = time()
                atualizar_ranking_crescente('Rank Jogo da Velha', nick_jogador1, pontos_jogador1)
                pontos_jogador1 = 10
                pontos_jogador2 = 10
                exibe(tabuleiro)
                print(f'Velha! Ótima partida, pessoal.')
                print()
                print('Voltar para o menu?')
                print()
                print('[S]Sim\n\n[N]Não')
                print()
                resposta = input('Digite: ').upper().strip()
                if resposta == 'S':
                    os.system('cls')
                    menu_inicio_jogo_da_velha()
                elif resposta == 'N':
                    os.system('cls')
                    # voltar para o menu geral
                    print('Saindo...')
                    sleep(2)
            jogada_geral += 1
    except:
        if not KeyboardInterrupt:
            print('Error')
            print('Reiniciando...')
            menu_inicio_jogo_da_velha()





menu_inicio_jogo_da_velha()