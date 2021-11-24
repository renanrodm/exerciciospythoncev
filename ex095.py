'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamente de cada jogador.'''

jogadores = dict()
time = list()
# estrutura de armazenamento dos dados

while True:
    jogadores['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))

    jogadores['gols'] = list()
    for c in range(0, partidas):
        gols = int(input(f'     Quantos gols na partida {c+1}? '))
        jogadores['gols'].append(gols)
    jogadores['total'] = sum(jogadores['gols'])
    time.append(jogadores.copy())

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
    if resp in "N":
        break
print("-="*30)

# estrutura de exibição dos dados de todos os jogadores


print(f'{"cod"} ', end='') #estrutura para gerar cabeçalho a partir das chaves
for k in jogadores.keys():
    print(f'{k:<15}', end='')
print()

print("-"*40)

for i, v in enumerate(time): #estrutura de exibição dos dados de todos os jogadores
    print(f'{i:>3} ', end='')
    for d in time[i].values():
        print(f'{str(d):<15}', end='')
    print()
print("-"*40)

# estrutura de exibição dos dados individuais com validação dos dados

while True:

    opc = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if opc == 999:
        break

    if opc >= len(time):
        print(f'ERRO! Não existe jogador com o código {opc}. Por favor, digite um numero entre 0 e {len(time)-1}.')
    else:
        print("-" * 40)
        print(f'-- Levantamento de dados do jogador {time[opc]["nome"]}')
        for i, g in enumerate(time[opc]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print("-" * 40)

print("<< VOLTE SEMPRE >>")