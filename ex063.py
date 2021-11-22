
'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
#0  1   1   2   3   5   8   13
#t1 t2  t3
print('-'*22)
print('Sequência de Fibonacci')
print('-'*22)
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('{} -> {} -> '.format(t1, t2), end='')
while c <= termos:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print('FIM', end='')
