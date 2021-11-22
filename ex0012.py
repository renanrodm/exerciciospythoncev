#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preço = float(input('Informe o preço do produto: '))
desc = preço*0.95
print('O valor do produto com 5% de desconto é {:.2f} R$'.format(desc))
