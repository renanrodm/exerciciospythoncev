'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
while True:
    opção = ' '
    lista.append(int(input('Digite um valor: ')))
    while opção not in 'sSnN':
        opção = input('Quer continuar? [S/N] ')
    if opção in 'Nn':
        break
for itens in lista:
    if itens % 2 == 0:
        pares.append(itens)
    else:
        impares.append(itens)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')