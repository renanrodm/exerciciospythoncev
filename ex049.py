'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Informe um número: '))
print("-"*11)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print("-"*11)