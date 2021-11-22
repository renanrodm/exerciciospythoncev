#Escreva um programa que pergunte o salário de um funcionário e calcule o valro do seu aumento.
#Para salários superiores R$ 1.250,00 calcule um aumento de 10%.
#Para salários inferiores ou iguais o aumento é de 15%.

salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    salario = salario*1.1
    print('O seu novo salário é de {:.2f}R$'.format(salario))
else:
    salario = salario*1.15
    print('O seu novo salário é de {:.2f}R$'.format(salario))
