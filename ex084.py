'''Faça um programa que leia o nome e peso de vários pessoas, guardando tudo em uma lista. No final. mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = []
dados = []
while True:
    dados.append(str(input('Seu nome: ')))
    dados.append(int(input('Seu peso (Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')