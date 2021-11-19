'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

lin1 = [[], [], []]
lin2 = [[], [], []]
lin3 = [[], [], []]
for i in range(0, 3):
    valor = int(input(f"Digite um valor para [0, {i}]: "))
    lin1[i].append(valor)
for i in range(0, 3):
    valor = int(input(f"Digite um valor para [1, {i}]: "))
    lin2[i].append(valor)
for i in range(0, 3):
    valor = int(input(f"Digite um valor para [2, {i}]: "))
    lin3[i].append(valor)
print(f'{lin1}')
print(f'{lin2}')
print(f'{lin3}')


