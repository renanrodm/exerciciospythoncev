#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = int(input('Qual foi a velocidade do carro em km/h? '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Você ultrapassou {:.0f}km/h além do permitido e foi multado em {:.2f} R$'.format(multa/7, multa))
print('Você não foi multado por respeitar o limite de velocidade')