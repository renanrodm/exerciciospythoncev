#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Informe um número: '))
print('O dobro deste número é {}, o triplo é {} e a raiz quadrada {:.2f}'.format((n*2), (n*3), pow(n, (1/2))))
