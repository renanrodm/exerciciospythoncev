'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias conseccutivas que ele conquistou no final do jogo.'''
#front-end
from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
totvitorias = 0
while True:
    num_usuario = int(input('Digite um valor: '))
    num_computador = randint(0, 10)
    jogada_usuario = ' '
    while jogada_usuario not in 'PI':
        jogada_usuario = str(input('Par ou impar [I/P]? ')).strip().upper()[0]
    total = num_computador + num_usuario
    print(f'Você jogou {num_usuario} e o computador {num_computador}. Total de {total} ',end ='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    #tratamento dos dados: possibilidades de vitória e derrota
    if jogada_usuario == 'P':
        if total % 2 == 0:
            print('--' * 15)
            print('Você VENCEU!')
            totvitorias += 1
        else:
            print('--' * 15)
            print('Você PERDEU!')
            break
    elif jogada_usuario == 'I':
        if total % 2 != 0:
            print('--' * 15)
            print('Vcoê VENCEU!')
            totvitorias += 1
        else:
            print('--' * 15)
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-='*15)
print('-='*15)
print(f'GAME OVER! Você venceu {totvitorias} vezes.')
