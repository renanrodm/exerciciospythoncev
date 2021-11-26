'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrando ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show=False):
    if show:
        print(f'{num}', end=' ')
        for f in range(num-1, 0, -1):
            print(f'x {f}', end=' ')
            num *= f
        print(f'= {num}')
    else:
        for f in range(num-1, 0, -1):
            num *= f
        return num


fatorial(5, show=True)