'''Desenvolva um programa que leia quatro valroes pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')))
print(f'Você digitou os valores {num} ')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º posição.')
else:
    print(f'O valor 3 não foi informado.')
print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'{c} ', end='')
