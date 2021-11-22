'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('='*10,'LOJAS MARTINS', '='*10)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
[ 2 ] À VISTA NO CARTÃO: 5% DE DECONTO
[ 3 ] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
[ 4 ] 3X OU MAIS NO CARTÃO: 20% DE JUROS''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço*0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))
elif opção == 2:
    total = preço*0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))
elif opção == 3:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 2:
        print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preço/2))
    elif parcelas == 1:
        print('Sua compra será parcelada em 1x de R${:.2f} SEM JUROS'.format(preço))
    else:
        print('OPÇÃO INVÁLIDA')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parcelas, preço*1.2/parcelas))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço*1.2))
    else:
        print('OPÇÃO INVÁLIDA')
else:
    print('OPÇÃO INVÁLIDA')