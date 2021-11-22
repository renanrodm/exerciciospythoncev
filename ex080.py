'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort).
No final, mostre a lista ordenada na tela.'''

valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor:  '))
    if c == 0:
        valores.append(n)
        print('Valor adicionado ao final da lista...')
    elif n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos <= len(valores):

            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
    print(valores)
'''lista = []
lista2 = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    maior = max(lista)
    menor = min(lista)
    if lista[c] >= maior:
        lista2.append(lista[c])
        print(f'Adicionado ao final da lista...')
    elif lista[c] <= menor:
        lista2.insert(0, lista[c])
        print(f'Adicionado na posição 0 da lista...')
    elif lista[c] >= lista2[1]:
        lista2.insert(-1, lista[c])
        print(f'Adicionado na posição 1 da lista...')
    elif lista[c] <= lista2[1]:
        lista2.insert(1, lista[c])
        print(f'Adicionado na posição 1 da lista...')
    print(lista2)
print('-='*30)
print(f'A lista em ordem é {lista2}')'''