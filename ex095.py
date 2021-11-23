'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamente de cada jogador.'''

jogador = dict()
jogadores = list()
gols = list()

while True:
    gols.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        gols.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols.copy()
    print(jogador)