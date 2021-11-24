time = list()
jogador = dict()
partidas = list()

# estrutura de armazenamento de dados
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print(f'ERRO! Responda apenas S ou N.')
    if resp == "N":
        break

print("-"*40)

# estrutura de exibição do cabeçalho a partir das chaves dos diconários
print(f'cod ', end='')

for k in jogador.keys():
    print(f'{k:<15}', end='')
print()

print("-"*40)

# estrutura de exibição dos dados completos dos jogadores
for i, v in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-"*40)

while True:

    busca = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999:
        break

    if busca >= len(time):
        print(f'ERRO: Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DE DADOS DO JOGADOR [{time[busca]["nome"].upper()}]:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print(f'<< VOLTE SEMPRE >>')