'''Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:

1. A média de idade do grupo
2. Qual é o nome do homem mais velho
3. Quantas mulheres tem menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-'*5, '{} PESSOA'.format(c), '-'*5)
    nome = str(input('informe seu nome: ')).strip().upper()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Sexo [M/F]: '))
    #media de idade
    somaidade += idade
    #identificando idade e nome do homem mais velho
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))












