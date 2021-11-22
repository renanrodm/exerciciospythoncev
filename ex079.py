'''Crie um programa onde o usuário possa digitar vários valores números e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''

#solução professor
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não será adicionado.')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

'''minha solução:
lista1 = []
while True:
    opção = ' '
    lista1.append(int(input('Digite um valor: ')))
    #Índice do último elemento da lista
    ultimo_valor = len(lista1) - 1
    #verificação de valores repetidos na lista
    if ultimo_valor == 0:
        print('Valor adicionado com sucesso!')
    elif lista1[ultimo_valor] in lista1[0: ultimo_valor]:
        print('Valor duplicado! Não será adicionado.')
        lista1.pop()
    else:
        print('Valor adicionado com sucesso!')
    #Verificação de continuação do programa
    while opção not in 'SsNn':
        opção = input('Deseja continuar? [S/N] ')
    if opção in 'Nn':
        break
lista1.sort()
print('=-'*30)
print(f'Você digitou os valores {lista1}')'''