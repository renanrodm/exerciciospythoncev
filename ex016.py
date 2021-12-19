#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex.: Digite um numero: 6.127. O numero 6.127 tem a parte inteira 6.
#Utilizar a classe math

num = float(input('Digite um numero real qualquer: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))

'''
from math import trunc
num = float(input('Digite um número real qualquer: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

# math.trunc retorna a porção inteira de um numero real/float'''