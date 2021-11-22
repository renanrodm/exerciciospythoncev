'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno_dados = dict()

aluno_dados['nome'] = str(input('Nome: '))
aluno_dados['media'] = float(input('Media: '))

print(f'- nome é igual a {aluno_dados["nome"]}')
print(f'- média é igual a {aluno_dados["media"]}')
if aluno_dados['media'] >= 7:
    print(f'- situação de APROVAÇÃO! Parabéns!')
elif 5 <= aluno_dados['media'] < 7:
    print(f'- situação de RECUPERAÇÃO!')
elif aluno_dados['media'] < 5:
    print(f'- situação de REPROVAÇÃO!')