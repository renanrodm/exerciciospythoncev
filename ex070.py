'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$ 1000
C - Qual é o nome do produto mais barato'''

print('=' * 30)
print('LOJAS SUPER BARATÃO'.center(30))
print('=' * 30)
totpreço = tot1000 = menorpreço = cont = 0
while True:
     #leitura de dados e inicializaçã de variáveis
     produto = str(input('Nome do produto: ')).strip()
     preço = float(input('Preço: R$ '))

     #tratamento de dados do programa
     cont += 1
     totpreço += preço
     if preço > 1000:
        tot1000 += 1
     if cont == 1 or preço < menorpreço:
          menorpreço = preço
          barato = produto

     #confirmação de continução ou finalização do programa
     resp = ' '
     while resp not in 'SN':
          resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
     if resp in 'Nn':
        break
print('-' * 15, 'FIM DO PROGRAMA', '-' * 15)
print(f'O total de compra foi de R${totpreço:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorpreço:.2f}')
