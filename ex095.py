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

print(f'{"Cód.":<5}{"Nome":<15}{"Gols":<25}{"Total":>}')

print("-"*60)
for i, j in enumerate(time):
    print(f'{i:^4} {j["nome"]:<15}{str(j["gols"]):<25}{j["total"]:<}')
print("-"*60)

# estrutura de exibição dos dados individuais

while True:

    while True:
        opc = int(input('Mostrar dados de qual jogador? (999 para parar): '))
        if 0 <= opc < len(time) or opc == 999:
            break
        print(f'ERRO! Não existe jogador com o código {opc}. Por favor, digite um numero entre 0 e {len(time)-1}.')
    if opc == 999:
        break

    print("-" * 60)
    print(f'-- Levantamento de dados do jogador {time[opc]["nome"]}')
    for i, g in enumerate(time[opc]['gols']):
        print(f'    No jogo {i+1} fez {g} gols.')
    print("-" * 60)

print("<< PROGRAMA ENCERRADO >>")