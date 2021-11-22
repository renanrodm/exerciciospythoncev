'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todas os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média'''
pessoas = list()
individuos = dict()
while True:
    # estrutura para armazenamento dos dados
    individuos['nome'] = str(input('Nome: '))
    individuos['sexo'] = str(input('Sexo [M/F]: '))
    while individuos['sexo'] not in 'MmFf': # tratamento de erro de string
        print('ERRO! Por favor, digite apenas M ou F.')
        individuos['sexo'] = str(input('Sexo [M/F]: '))
    individuos['idade'] = int(input('Idade: '))
    pessoas.append(individuos.copy())
    print('-='*30)
    # estrutura de confirmação para continuação do programa
    opc = str(input('Quer continuar? [S/N]: '))
    while opc not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
        opc = str(input('Quer continuar? [S/N]: '))
    if opc in 'Nn':
        break