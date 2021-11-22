'''Crie um programa que faça o computador Jokenpô com você.

Pedra, papel ou tesoura.'''
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua jogada: '))
computador = randint(0, 2)

if jogador <= 2:
    sleep(0.6)
    print('JO!')
    sleep(0.5)
    print('KEN!')
    sleep(0.4)
    print('PO!')

# Jogador escolhe PEDRA
if jogador == 0:
    if computador == 0:
        print('=-'*11)
        print('O JOGADOR jogou {}'.format(itens[0]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('EMPATE!')
    elif computador == 1:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[0]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('COMPUTADOR VENCE! PAPEL EMRBULHA PEDRA')
    elif computador == 2:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[0]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('JOGADOR VENCE! PEDRA ESMAGA PAPEL!')

# Jogador escolhe PAPEL
elif jogador == 1:
    if computador == 0:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[1]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('JOGADOR VENCE! PAPEL EMBRULHA PEDRA!')
    elif computador == 1:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[1]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('EMPATE!')
    elif computador == 2:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[1]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('COMPUTADOR VENCE! TESOURA CORTA PAPEL!')

# Jogador escolhe TESOURA
elif jogador == 2:
    if computador == 0:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[2]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('COMPUTADOR VENCE! PEDRA ESMAGA TESOURA!')
    elif computador == 1:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[2]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('JOGADOR VENCE! TESOURA CORTA PAPEL!')
    elif computador == 2:
        print('=-' * 11)
        print('O JOGADOR jogou {}'.format(itens[2]))
        print('o COMPUTADOR jogou {}'.format(itens[computador]))
        print('=-' * 11)
        print('EMPATE!')
else:
    print('OPÇÃO INVÁLIDA. ESCOLHA ENTRE 0, 1 OU 2.')