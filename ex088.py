'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
qtde_jogos = int(input("Quantos jogos você quer que eu sorteie? -> "))
lista = []
for c in range(0, qtde_jogos):
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
