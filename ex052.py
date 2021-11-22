
'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
tot = 0
n = int(input('Informe um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1 #mesmo coisa que s = s + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[mO número {} foi divisível 2 vezes!'.format(n))
    print('E por isso ELE É PRIMO!')
else:
    print('\n\033[mO número {} foi divisível {} vezes!'.format(n, tot))
    print('E por isso {} NÃO É PRIMO'.format(n))
