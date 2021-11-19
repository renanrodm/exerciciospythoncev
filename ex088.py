'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
import time
from time import sleep
qtde_jogos = int(input("Quantos jogos você quer que eu sorteie? -> "))
jogos = [0, 0, 0, 0, 0, 0]
for i in range(0, qtde_jogos):
    for c in range(0, 6):
        jogos[c] = random.randint(1, 60)
    time.sleep(0.5)
    print(f"Jogo {i}: {jogos}")