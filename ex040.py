'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2

if media >= 7.0:
    print('Parabéns, sua média foi de {:.1f} e você foi APROVADO!'.format(media))
elif 5 <= media < 7:
    print('Sua média foi de {:.1f} e você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi de {:.1f} e você está REPROVADO: '.format(media))