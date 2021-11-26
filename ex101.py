'''Crie um programaque tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''
from datetime import date


def voto(i):
    if i <= 15:
        return "NÃO VOTA"
    elif 16 <= i <= 17:
        return "VOTO OPCIONAL"
    elif i >= 18:
        return "VOTO OBRIGATÓRIO"

print('-'*30)
ano = int(input('Quem que ano você nasceu? '))
idade = date.today().year - ano
print(f'Com {idade} anos: {voto(idade)}.')
