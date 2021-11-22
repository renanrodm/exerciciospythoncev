'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('='*40)
print('          10 TERMOS DE UMA PA          ')
print('='*40)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termos = 10
cont = 0
total = 0
while termos != 0:
    total += termos
    while cont < total:
        primeiro = primeiro + razão
        print('{} -> '.format(primeiro), end='')
        cont = cont + 1
        print('({})'.format(cont))
    print('PAUSA')
    termos = int(input('Quantos termos a mais você quer? '))
print('A progressão foi finalizada com {} termos'.format(cont))