'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todas os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média'''

pessoas = list()
individuos = dict()
tot_pessoas = 0
tot_idade = 0

while True:
    individuos.clear()
    # estrutura para armazenamento dos dados
    individuos['nome'] = str(input('Nome: '))

    #estrutura de validação de dados para o cadastro
    while True:
        individuos['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if individuos['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    individuos['idade'] = int(input('Idade: '))
    tot_idade += individuos['idade']

    pessoas.append(individuos.copy())

    print('-=' * 30)

    # estrutura de validação de dados para sair do programa
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if opc in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if opc in 'N':
        break

print('-=' * 30)

# estrutura de exibição básica dos itens A e B
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

media_idade = tot_idade / len(pessoas)
print(f'B) A média de idade é de {media_idade:5.2f} anos.')

# estrutura de criação da lista de mulheres e idades acima da média
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end=' ')
print('')

# estrutura para mostrar lista de pessoas com idade acima da média
print(f'D) Lista de pessoas que estão acima da média de idade: ')
for p in pessoas:
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f'    {k} = {v}; ', end='')
        print('')

print('<< ENCERRADO >>')
