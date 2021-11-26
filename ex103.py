'''Faça um programa que tenha uma funçao chama ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(j="<<desconhecido>>", g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


jogador = input('Nome do jogador: ')
gols = input('Numero de gols: ')


if jogador != "" and gols != "":
    if jogador.isalpha() and gols.isnumeric():
        ficha(jogador, int(gols))
    else:
        ficha()

elif jogador != "" and gols == "":
    if jogador.isalpha():
        ficha(jogador)
    else:
        ficha()

elif jogador == "" and gols != "":
    if gols.isnumeric():
        ficha(g=int(gols))
    else:
        ficha()

else:
    ficha()

