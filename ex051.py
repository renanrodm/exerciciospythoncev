'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('='*40)
print('          10 TERMOS DE UMA PA          ')
print('='*40)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    print(a1, end=' -> ')
    a1 = a1 + r #acumulador
print('ACABOU')