'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrando ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    if show:
        print(f'{num}', end=' ')
        for f in range(num - 1, 0, -1):
            print(f'x {f}', end=' ')
            num *= f
        print(f'= {num}')
    else:
        for f in range(num - 1, 0, -1):
            num *= f
        return print(num)


fatorial(7, show=True)
# help(fatorial)
