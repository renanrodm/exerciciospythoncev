'''Refaça o desafio51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('='*40)
print('          10 TERMOS DE UMA PA          ')
print('='*40)
primeiro = int(input('Primeiro termo: ')) #2
razao = int(input('Razão: ')) #2
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')
