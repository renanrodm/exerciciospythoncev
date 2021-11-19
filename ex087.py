'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valroes da terceira coluna.
C) O maior valor  da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_col = 0
maior_valor = matriz[1][0]
#loop de alimentação da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l},{c}]: "))

print("-="*30)
#loop de exibição e operações na matriz
for l in range(0, 3):
    # somando os valores da terceira coluna
    soma_col += matriz[l][2]
    for c in range(0, 3):
        #somando os valores pares
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        #maior valor da segunda coluna
        if matriz[1][c] > maior_valor:
            maior_valor = matriz[1][c]
        #exibindo matriz na tela de forma formata
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-="*30)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_col}')
print(f'O maior valor da segunda linha é {maior_valor}')