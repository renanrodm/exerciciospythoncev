#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com {}R$ você pode comprar {:.2f}US$.'.format(dinheiro, dinheiro/3.27))
