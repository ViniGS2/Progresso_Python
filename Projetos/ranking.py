
import os


def atualizar_ranking_decrescente(nome_arquivo, nome, pontuacao):
    registro = {}

    # armazena
    if not os.path.exists(f'{nome_arquivo}.txt'):
        criar_arquivo(f'{nome_arquivo}.txt', nome, pontuacao)
    else:
        with open(f'{nome_arquivo}.txt', 'r+') as arquivo:
            for i in arquivo:
                if not i == '1':
                    registro.update({i.strip().split(':')[0]:i.strip().split(':')[1]})
            registro.update({nome: pontuacao})
        # organiza

        ordenado = sorted(registro.items(), key=lambda x: float(x[1]))

        # registra

        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            for k, v in ordenado:
                arquivo.write(f'{k}:{float(v):.1f}\n')


def atualizar_ranking_crescente(nome_arquivo, nome, pontuacao):
    registro = {}

    # armazena
    if not os.path.exists(f'{nome_arquivo}.txt'):
        criar_arquivo(f'{nome_arquivo}.txt', nome, pontuacao)
    else:
        with open(f'{nome_arquivo}.txt', 'r+') as arquivo:
            for i in arquivo:
                if not i == '1':
                    registro.update({i.strip().split(':')[0]:i.strip().split(':')[1]})
            registro.update({nome: pontuacao})
        # organiza

        ordenado = sorted(registro.items(), key=lambda x: float(x[1]), reverse=True)

        # registra

        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            for k, v in ordenado:
                arquivo.write(f'{k}:{float(v):.1f}\n')



def criar_arquivo(nome_arquivo, nome, pontuacao):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f'{nome}:{pontuacao}\n')
        pass


def ver_ranking(nome_arquivo):
    registro = {}
    with open(f'{nome_arquivo}.txt', 'r') as arquivo:
        for i in arquivo:
            registro.update({i.strip().split(':')[0]:i.strip().split(':')[1]})

    lugar = 0
    print(f'{"Lugar":<4} | {"Nome do Jogador":^20} | {"Pontuação":>4}')
    for k, v in registro.items():
        pont = f'{float(v)}'
        lugar += 1
        print(f'{f"{lugar}°":<5} | {k:^20} | {pont:>4}')


def ver_ranking_tentativas(nome_arquivo):
    registro = {}
    with open(f'{nome_arquivo}.txt', 'r') as arquivo:
        for i in arquivo:
            registro.update({i.strip().split(':')[0]:i.strip().split(':')[1]})

    lugar = 0
    print(f'{"Lugar":<4} | {"Nome do Jogador":^20} | {"Tentativas ":>4}')
    for k, v in registro.items():
        pont = f'{float(v):.0f}'
        lugar += 1
        print(f'{f"{lugar}°":<5} | {k:^20} | {pont:>4}')
