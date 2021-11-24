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
print("-="*30)

# estrutura de exibição dos dados de todos os jogadores

print(f'{"Cód.":>2}{"Nome":<10} {"Gols"} {"Total":>15}')

print("-"*30)
for i, j in enumerate(time):
    print(f'{i:>4}{j["nome"]:<10}{j["gols"]}{j["total"]:<}')
print("-"*30)

# estrutura de exibição dos dados individuais

while True:
    while True:
        opc = int(input('Mostrar dados de qual jogador? (999 para parar): '))
        if 0 <= opc < len(time) or opc == 999:
            break
        print(f'Não existe jogador com o código {opc}.')
    if opc == 999:
        break

    print(f' -- Levantamento de dados do jogador {time[opc]["nome"]}')
    for i, g in enumerate(time[opc]['gols']):
        print(f'No jogo {i+1} fez {g} gols.')
    print("-" * 30)

print("<< PROGRAMA ENCERRADO >>")