'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
import random
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6),
}
ranking = list()

for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*30)
for i, j in enumerate(ranking):
    print(f'{i+1}º: {j[0]} com {j[1]}')