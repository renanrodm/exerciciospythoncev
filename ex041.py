'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: mirim
- Até 14 anos: infantil
- Até 19 anos: Junior
- Até 20 anos: sênior
- Acima: MASTER'''
from datetime import date
ano_nasc = int(input('Informe seu ano de nascimento: '))
ano_atual = 2017 #date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print('Quem nasceu em {} tem {} anos.'.format(ano_nasc, idade))
    print('Clássificação: MIRIM')
elif idade <= 14:
    print('Quem nasceu em {} tem {} anos.'.format(ano_nasc, idade))
    print('Classificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('Quem nasceu em {} tem {} anos.'.format(ano_nasc, idade))
    print('Classificação: JUNIOR'.format(idade))
elif idade <= 25:
    print('Quem nasceu em {} tem {} anos.'.format(ano_nasc, idade))
    print('Classificação: SÊNIOR'.format(idade))
else:
    print('Quem nasceu em {} tem {} anos.'.format(ano_nasc, idade))
    print('Classificação: MASTER'.format(idade))
