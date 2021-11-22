'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano da contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

Considerando aposentadoria dps de 35 anos de contribuição.'''
from datetime import datetime
dados = dict()
# estrutura de alimentação do dicionário

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratação'])) + dados['idade']
else:
    del dados['ctps']
print('-='*30)

# estrutura de exibição dos itens
for k, v in dados.items():
    print(f'- {k} tem o valor {v} ')