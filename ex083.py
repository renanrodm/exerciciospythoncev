'''Crie um programa onde o usuário digite uma expressão qualquer que use parânteses. Seu aplicativo deverá analisar se a expressão passada está com os parânteses abertos e fechado na ordem correta'''

expr = str(input('Digite uma expressão:  '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão É válida!')
else:
    print('Sua expressão NÃO é válida!')
