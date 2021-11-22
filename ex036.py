'''#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

preço = float(input('Valor da CASA R$ '))
salario = float(input('Qual é o salário? '))
anos = float(input('Em quantos anos irá pagar? '))
prestação = preço/(anos*12)

if prestação <= (salario*0.3):
    print('Para pagar uma casa no valor de {:.2f} em {} anos a prestação será de R${:.2f}'.format(preço, anos, prestação))
    print('Emprestimo CONCEDIDO!')
else:
    print('Para pagar uma casa no valor de {:.2f} em {} anos a prestação será de R${:.2f}'.format(preço, anos, prestação))
    print('Emprestimo NEGADO!')
