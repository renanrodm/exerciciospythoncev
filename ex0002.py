#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite qualquer coisa: ')

print('A princípio, o tipo de primitivo dessa informação é: {}'.format(type(n)))
print('Essa string só tem espaço? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))

# Uma string é considerada um identificador válido se contiver apenas letras alfanuméricas (az) e (0-9) ou
# sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços. 


