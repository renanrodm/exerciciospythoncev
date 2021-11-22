ficha = list()

# estrutura de armazenamento de dados
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)


# estrutura de exibição de dados em forma de tabela
for indice, alunos in enumerate(ficha):
    print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>8.1f}')

# estrutura de consulta de notas individuais
while True:
    print('-'*35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 9:
        print("Finalizando...")
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')