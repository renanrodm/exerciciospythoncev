
'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

Maiorirdade = 21 anos'''
from datetime import date
atual = 2017 #date.today().year
tot_maior = 0
tot_menor = 0
for c in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - n
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('{} pessoas atingiram a maioridade.'.format(tot_maior))
print('{} pessoas NÃO ATINGIRAM a maiorirdade'.format(tot_menor))


