'''Crie um programa que tenha uma tupla com várias palavras (nãp usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYHTON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:#p recebe o primeiro item da tupla;
    print(f'\nNa palavra {p} temos ', end='')
    for letras in p:#nesse momento letras recebe todas as letras da palavra da tupla.
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
