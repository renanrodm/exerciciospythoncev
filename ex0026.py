# Faça um programa que leia uma frase pelo teclado e mostre:
#1. Quantas vezes aparece a letra "A".
#2. Em que posição ela aparece a primeira vez.
#3. Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Analisando a frase...')
print('A letra A aparece {} vezes;'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {};'.format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {};'.format(frase.rfind('A')+1))