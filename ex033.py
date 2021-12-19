# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é ', menor)

# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é ', maior)


#REVISAR CODIGO AMANHÃ!!!!!
