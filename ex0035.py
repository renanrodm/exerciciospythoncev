
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

n1 = float(input('Informe o primeiro lado: '))
n2 = float(input('Informe o segundo lado: '))
n3 = float(input('Informe o terceiro lado: '))

if n3 < (n1+n2) and n2 < (n1+n3) and n1 < (n2+n3):
    print('Esses valores podem formar um triângulo!')
else:
    print('Esses valores NÃO podem formar um triângulo')