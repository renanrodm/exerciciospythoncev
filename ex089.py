'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final. mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
dados = [[], [], [], []]
#estrutura para coletar dados
while True:
    aluno = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    dados[0].append(aluno)
    dados[1].append(nota1)
    dados[2].append(nota2)
    dados[3].append(media)
    flag = input("Quer continuar? [S/N]: ")
    if flag in "Nn":
        break
print("-="*30)