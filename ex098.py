'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetro: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contanges através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.'''
from time import sleep


def contador(inicio, fim, passo):

    if passo < 0:
        passo = passo * (-1)

    print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:

        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
        print(f'-> FIM')

    elif inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont = cont - passo
        print(f'-> FIM')
        print("-=" * 30)


print("-=" * 30)
contador(1, 10, 1)
contador(10, 0, 2)
print(f'Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
