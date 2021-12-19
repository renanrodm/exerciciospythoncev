#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')



'''Minha solução:
cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.upper().split()
print('A sua cidade começa com SANTO?: {}'.format('SANTO' in cidade[0]))'''
