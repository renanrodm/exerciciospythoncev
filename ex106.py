'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.'''
from time import sleep

c = [
    '\033[0:0m',  # 0 -> reset cores
    '\033[0:97:41m',  # 1 -> vermelho
    '\033[0:97:102m',  # 2 -> verde claro
    '\033[0:97:104m',  # 3 -> azul claro
    '\033[0:30:107m'   # 4 -> branco
]


def escreva(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def consulta_pyhelp(arg):
    escreva(f"Acessando o manual do comando '{arg}'", 3)
    print(c[4], end='')
    help(arg)
    print(c[0], end='')
    sleep(2)

while True:
    escreva(f'SISTEMA DE AJUDA PyHELP', 2)
    opc = input('Função ou biblioteca > ').strip()
    if opc in 'fim':
        break
    else:
        consulta_pyhelp(opc)

escreva('ATÉ LOGO!', 1)
