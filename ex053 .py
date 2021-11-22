
'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços e acentos.

Exs.:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''


frase = str(input('Digite um frase qualquer: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS um palíndromo!')
else:
    print('NÃO é um palíndromo')


