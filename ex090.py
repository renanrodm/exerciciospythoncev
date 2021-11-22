'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno_dados = dict()

aluno_dados['nome'] = str(input('Nome: '))
aluno_dados['media'] = float(input('Media: '))
if aluno_dados['media'] >= 7:
    aluno_dados['situação'] = 'APROVADO'
elif 5 <= aluno_dados['media'] < 7:
    aluno_dados['situação'] = 'RECUPERAÇÃO'
elif aluno_dados['media'] < 5:
    aluno_dados['situação'] = 'REPROVADO!'

print(f'- nome é igual a {aluno_dados["nome"]}')
print(f'- média é igual a {aluno_dados["media"]}')
print(f'- situação é igual {aluno_dados["situação"]}')