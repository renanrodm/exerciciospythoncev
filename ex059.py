'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior valor
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sairprograma = False
while not sairprograma:
    print('''Escolha sua opção:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior valor
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n2))
    elif opção == 4:
        print('Infore os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        sairprograma = True
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
        sairprograma = False
print('Você saiu do programa. Volte sempre! :D')