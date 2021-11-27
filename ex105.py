'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.'''

def notas(*nts, sit=False):
    dados = dict()
    dados['total'] = len(nts)
    dados['maior'] = max(nts)
    dados['menor'] = min(nts)
    dados['média'] = sum(nts)/len(nts)
    return dados

resp = notas(5.5, 9.5, 10, 6.5)
print(resp)