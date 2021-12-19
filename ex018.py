#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangante.
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, coss))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, tang))

