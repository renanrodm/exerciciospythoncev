#Escreva um programa que faça o computador "pensar" em um número inteiro antes de 0 e 5 e peça para o usuáiro tentar descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5)
num_user = int(input('Chute um número entre 0 e 5: '))
print('Processando....')
sleep(2) #Faz o computador dar uma "dormida" no tempo especificado em segundos
if num_user == computador:
    print('Parabéns, você acertou o número!!! :(')
else:
    print('Você errou o número, GANHEI.')
print('O número que pensei foi: ', computador)
