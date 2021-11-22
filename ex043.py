'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida
imc = peso/altura²
'''

peso = float(input('Informe seu peso? (kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso/altura**2

if imc <= 18.5:
    print('''O seu IMC é de {:.1f} 
Você é considerado ABAIXO DO PESO.'''.format(imc))
elif imc < 25:
    print('''O seu IMC é de {:.1f}
Você está com o PESO IDEAL.'''.format(imc))
elif imc < 30:
    print('''O seu IMC é de {:.1f}
Você é considerado SOBREPESO.'''.format(imc))
elif imc < 40:
    print('''O seu IMC é de {:.1f}
Você se enquandra em OBESIDADE.'''.format(imc))
else:
    print('''O seu IMC é de {:.1f}
Você se enquandra em OBESIDADE MÓRBIDA.'''.format(imc))
