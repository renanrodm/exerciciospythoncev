# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Digite um ano qualquer. Digite 0 para analisar o ano atual: '))
#Se o resto da divisão do ano por 4 for zero, se o resto da divisão por 100 for diferente de zero e se o resto da divisão por 400 for zero
if ano == 0:
    ano = date.today().year #seleciona a data do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é um ano bissexto!'.format(ano))
