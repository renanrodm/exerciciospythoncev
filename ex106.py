'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.'''
from time import sleep


def escreva(msg):
    print(f'~' * (len(msg)+ 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


def consulta_pyhelp(arg):

    print(f'{estilos["cabeçalho_consulta"]}', end='')
    escreva(f"Acessando o manual do comando '{arg}'")
    print(f'{estilos["reset"]}', end='')
    sleep(1)
    print(f'{estilos["conteudo_pyhelp"]}', end='')
    help(arg)
    print(f'{estilos["reset"]}', end='')

estilos = {
'reset': '\033[0:0m',
'cabeçalho_principal': '\033[0:97:102m',
'cabeçalho_consulta': '\033[0:97:44m',
'conteudo_pyhelp': '\033[0:30:107m',
'fim': '\033[0:97:41m'
}


while True:
    print(f'{estilos["cabeçalho_principal"]}', end='')
    escreva(f'SISTEMA DE AJUDA PyHELP')
    print(f'{estilos["reset"]}', end='')
    opc = input('Função ou biblioteca > ').strip()
    if opc in 'fim':
        break
    consulta_pyhelp(opc)

print(f'{estilos["fim"]}', end='')
escreva('ATÉ LOGO!')

