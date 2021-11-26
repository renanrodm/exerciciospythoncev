'''Faça um programa que tenha uma funçao chama ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(j="<<desconhecido>>", g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


jogador = input('Nome do jogador: ')
gols = input('Numero de gols: ')

if len(jogador) != 0 and len(gols) != 0:
    ficha(jogador, gols)
elif len(jogador) == 0:
    ficha()
elif len(gols) == 0:
    ficha(jogador)
elif len(jogador) == 0 and len(gols) == 0:
    ficha()
