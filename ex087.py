'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valroes da terceira coluna.
C) O maior valor  da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l},{c}] "))
print("-="*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-="*30)
#soma dos valores pares
soma_par = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
#soma dos valores da terceira coluna
soma_terc = 0
for l in range(0, 3):
    soma_terc += matriz[l][2]
#maior valor da segunda linha
maior_valor = matriz[1][0]
for c in range(0, 3):
    if matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terc}')
print(f'O maior valor da segunda linha é {maior_valor}')