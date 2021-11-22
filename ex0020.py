#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação do trabalho será: {}.'.format(alunos))

# random.suffle() mistura uma lista;
# random.sample(p, k) retorna num número específico de informações (k) dentro de uma população (p);
