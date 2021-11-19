'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
import time
qtde_jogos = int(input("Quantos jogos você quer que eu sorteie? -> "))
lista = []

for c in range(0, qtde_jogos):
    while len(lista) < 6:
        numero = random.randint(1, 60)
        if numero not in lista:
            lista.append(numero)
    print(f'Jogo {c+1}: {lista}')
    lista.clear()