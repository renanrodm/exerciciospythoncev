'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.'''

def notas(*nts, sit=False):
    soma = 0
    dados = dict()
    dados['total'] = len(nts)
    for i, c in enumerate(nts):
        soma += c
        if i == 0:
            dados['maior'] = c
            dados['menor'] = c
        if c > dados['maior']:
            dados['maior'] = c
        elif c < dados['menor']:
            dados['menor'] = c
    dados['média'] = soma/dados['total']
    return dados


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)