

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resp = 'S'
soma = quant = maior = menor = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    quant += 1
    soma = soma + num
    if quant == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = soma/quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor {}.'.format(maior, menor))