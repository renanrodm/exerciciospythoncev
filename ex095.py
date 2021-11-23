'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamente de cada jogador.'''

jogadores = dict()
time = list()
# estrutura de armazenamento dos dados

while True:
    tot_gols = 0
    jogadores['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))

    jogadores['gols'] = list()
    for c in range(0, partidas):
        gols = int(input(f'     Quantos gols na partida {c+1}? '))
        tot_gols += gols
        jogadores['gols'].append(gols)
    jogadores['total'] = tot_gols
    time.append(jogadores.copy())

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
    if resp in "N":
        break
print("-*"*30)

# estrutura de exibição

print("-"*30)
for i, j in enumerate(time):
    print(f'{i:<2} {j["nome"]:<15} {j["gols"]} {j["total"]:<5}')
print("-"*30)