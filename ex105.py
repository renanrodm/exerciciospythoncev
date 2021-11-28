'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.'''

def notas(*nts, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nts: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
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
    dados['media'] = soma/dados['total']

    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif 5 <= dados['media'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'

    return dados


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)
