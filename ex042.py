'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: Todos os lados diferentes'''


n1 = float(input('Primeiro segmento:  '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n3 < (n1+n2) and n2 < (n1+n3) and n1 < (n2+n3):
    if n1 == n2 == n3:
        print('Os seguimentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif n1 != n2 != n3 != n1:
        print('Os seguimentos acima PODEM FORMAR um triângulo ESCALENO.')
    else:
        print('Os seguimentos acima PODEM FORMAR um triângulo ISÓSCELES.')
else:
    print('Esses valores NÃO podem formar um triângulo')


