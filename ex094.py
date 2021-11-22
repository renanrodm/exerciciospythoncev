'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todas os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média'''
pessoas = list()
individuos = dict()
mulheres = list()
idade_maior_media = list()
tot_pessoas = 0
soma_idade = 0
while True:
    # estrutura para armazenamento dos dados
    individuos['nome'] = str(input('Nome: '))
    individuos['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while individuos['sexo'] not in 'MmFf': # tratamento de erro de string
        print('ERRO! Por favor, digite apenas M ou F.')
        individuos['sexo'] = str(input('Sexo [M/F]: ')).upper()
    individuos['idade'] = int(input('Idade: '))
    soma_idade += individuos['idade'] #acumula idade para cálculo da média
    pessoas.append(individuos.copy())
    tot_pessoas += 1 #conta quantas pessoas foram adicionadas
    print('-='*30)
    # estrutura de confirmação para continuação do programa
    opc = str(input('Quer continuar? [S/N]: '))
    while opc not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
        opc = str(input('Quer continuar? [S/N]: '))
    if opc in 'Nn':
        break
print('-='*30)

#estrutura de exibição básica dos itens A e B
print(f'A) Ao todo temos {tot_pessoas} pessoas cadastradas.')
media_idade = soma_idade/tot_pessoas
print(f'B) A média de idade é de {media_idade:.2f} anos.')

# estrutura de exibição do item C
for i, v in enumerate(pessoas):

    if pessoas[i]['sexo'] == 'F':# adicionando pessoas do sexo feminino para uma lista
        mulheres.append(v['nome'])

    if pessoas[i]['idade'] > media_idade: # adicionado pessoas acima da media de idade para uma lista
        idade_maior_media.append(v.copy())
print(f'C) As mulheres cadastradas foram {mulheres}')

# estrutura para exibir pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média: ')
for i, v in enumerate(idade_maior_media):
    print(f'    nome = {idade_maior_media[i]["nome"]}; sexo = {idade_maior_media[i]["sexo"]}; idade = {idade_maior_media[i]["idade"]}')
print('<< ENCERRADO >>')