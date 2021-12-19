# Faça um programa que leia a largura e  altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
larg = float(input('Qual a largura da sua parede em metros? '))
alt = float(input('Qual a altura da sua parede em metros? '))
area = larg * alt
print('Sua parede tem dimensão de {} x {} e sua área é de {:.3f}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(area/2))
