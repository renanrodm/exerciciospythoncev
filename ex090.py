'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno_dados = dict()
#estrutura de alimentação de dados
aluno_dados['nome'] = str(input('Nome: '))
aluno_dados['media'] = float(input('Media: '))
if aluno_dados['media'] >= 7:
    aluno_dados['situação'] = 'APROVADO'
elif 5 <= aluno_dados['media'] < 7:
    aluno_dados['situação'] = 'RECUPERAÇÃO'
elif aluno_dados['media'] < 5:
    aluno_dados['situação'] = 'REPROVADO!'
# estrutura de exibição dos dados do dicionário a partir do for
for k, v in aluno_dados.items():
    print(f'- {k} é igual a {v}')