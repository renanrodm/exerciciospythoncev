'''Crie um programa que gerencie o aproveitamente de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dados = {'nome': str(input('Nome do jogador: ')), 'gols': list()}
total = 0
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    gols_partida = int(input(f'     Quantos gols na partida {c}: '))
    dados['gols'].append(gols_partida)
    total += gols_partida
dados['total'] = total

print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')