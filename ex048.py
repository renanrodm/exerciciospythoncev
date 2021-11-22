'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #contador: sempre acrescente mais 1 quando atendida condição.
        soma = soma + c #acumulador: acumula os valores resultantes de cada teste.
print('A soma todos os {} valores é {}'.format(cont, soma))
