'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''

valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
print('-='*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor informado foi {maior} nas posições ', end='')
cont = 0
for pos_item, item in enumerate(valores):
    if item == maior:
        print(f'{pos_item}... ', end='')
print(f'\nO menor valor informado foi {menor} nas posições ', end='')
for pos_item, item in enumerate(valores):
    if item == menor:
        print(f'{pos_item}... ', end='')