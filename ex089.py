'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final. mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
dados = list()
# estrutura para coletar dados
while True:
    aluno = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    dados.append([aluno, [nota1, nota2], media])
    flag = input("Quer continuar? [S/N]: ")
    while flag not in "NnSs":
        flag = input("Quer continuar? [S/N]: ")
    if flag in "Nn":
        break
print("-="*30)
# estrurura para exibir em tabela os dados solicitados
print(f'{"No.":<4} {"NOME":<15} {"MEDIA"}')
print("-"*30)
for indice, alunos in enumerate(dados):
    print(f'{indice:<4} {alunos[0]:<15} {alunos[2]:>.1f}')
print("-"*30)

# estrutura para exibir notas individuais
while True:
    numero_aluno = int(input("Mostrar notas de qual aluno? (999 para interromper): "))
    if numero_aluno == 999:
        break
    if numero_aluno <= len(dados) - 1:
        print(f'As notas do aluno(a) {dados[numero_aluno][0]} são {dados[numero_aluno][1]}.')