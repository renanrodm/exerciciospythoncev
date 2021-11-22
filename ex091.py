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
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.3)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')