'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetro: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contanges através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.'''
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * (-1)
    print("-=" * 30)
    print(f'Contando de {i} até {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont += p
        print(f'-> FIM')
    elif i > f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont -= p
        print(f'-> FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
