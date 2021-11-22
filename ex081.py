'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor foi digitado ou não na lista. '''
lista = []
cont_num = 0
cont_cinco = 0
while True:
    opção = ' '
    lista.append(int(input('Digite um valor: ')))
    cont_num += 1
    while opção not in 'SsNn':
        opção = input('Deseja continuar? [S/N] ')
    if opção in 'Nn':
        break
lista.sort(reverse=True)
print('=-'*30)
print(f'Você digitou {cont_num} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
