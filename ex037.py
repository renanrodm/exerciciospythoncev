'''#Escreva um programa que leia um número inteiro qualquer numero e peça para o usuário escolher qual será a base da conversão:

#1 para binário
#2 para octal
#3 para hexadecimal'''

n1 = int(input('Informe um número: '))
print('''Escolha uma das bases para conversão
[1] para binário
[2] para octal
[3] para hexadecimal''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para binário é igual a {}'.format(n1, bin(n1)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('{} convertido para hexdecimal é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('OPÇÃO INVÁLIDA! Escolha entre 1, 2 ou 3.')