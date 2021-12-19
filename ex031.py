#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

dist = int(input('Qual foi a distância percorrida em km?: '))

#if in line, condição simplificada
preço = dist*0.50 if dist <= 200 else preço = dist*0.45
print('A viagem custou {} R$'.format(preço))


'''Minha solução: 
if dist <= 200:
    preço = dist*0.50
    print('A viagem custou {} R$'.format(preço))
else:
    preço = dist*0.45'''