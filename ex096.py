'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(larg, comp):
    area = larg * comp
    print(f'A area de um terreno {larg:.1f}x{comp:.1f} é de {area}m².')


print('-' * 30)
print(f'{"Controle de Terreno":^30}')
print('-'*30)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
