'''Crie um programaque tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''



def voto(i):
    from datetime import date
    idade = date.today().year - i

    if idade <= 15:
        return f"Com {idade} anos de idade: NÃO VOTA."
    elif 16 <= idade <= 17:
        return f"Com {idade} anos de idade: VOTO OPCIONAL."
    elif idade >= 18:
        return f"Com {idade} anos de idade: VOTO OBRIGATÓRIO."

print('-'*30)
ano = int(input('Quem que ano você nasceu? '))
print(voto(ano))
