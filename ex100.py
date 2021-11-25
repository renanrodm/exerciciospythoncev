'''Faça um programa que tenha uma lista chamda números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''
from random import randint
from time import sleep

def sorteia(lst):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        num = randint(1, 10)
        print(f'{num}', end=' ')
        sleep(0.35)
        lst.append(num)
    sleep(0.2)
    print(f'PRONTO!')


def somaPar(lst):
    print(f'Somando os valores pares de {lst}, temos ', end='')
    soma_par = 0
    for c in lst:
        if c % 2 == 0:
            soma_par += c
    print(f'{soma_par}.')


numeros = list()

sorteia(numeros)
somaPar(numeros)


