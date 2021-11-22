'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}. '.format(ano, idade, ano_atual))
    print('Você deve se alistar IMEDIATAMENTE!!')
elif idade < 18:
    print('Quem nasceu em {} tem {} anos em {}. '.format(ano, idade, ano_atual))
    print('Ainda faltam {} anos para seu alistamento.'.format(18-idade))
    print('Seu alistamento será em {}. '.format(ano_atual + (18-idade)))
else:
    print('Quem nasceu em {} tem {} anos em {}. '.format(ano, idade, ano_atual))
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))



