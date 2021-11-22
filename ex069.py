'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A - quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
B - Quantas mulheres tem menos de 20 anos.'''
tot18 = tothomem = totmulheres = 0
while True:
    #inciando variáveis
    opção = ' '
    sexo = ' '

    #estrutura de leitura de dados
    print('--' * 15)
    print('CADASTRE UMA PESSOA'.center(30))
    print('--' * 15)
    idade = int(input('Idade: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    #Estrutura de recursos do programa
    if idade >= 18:
        tot18 += 1
    if sexo in 'Mm':
        tothomem += 1
    if sexo in 'Ff' and idade <= 20:
        totmulheres += 1

    #confirmação de uma nova execução do programa
    print('--' * 15)
    while opção not in 'SsNn':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break

print('='*5, 'FIM DO PROGRAMA', '='*5)
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {tothomem} homens cadastrados.')
print(f'E temos {totmulheres} mulheres com menos de 20 anos.')