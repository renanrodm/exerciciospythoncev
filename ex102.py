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
        f = 1
        for c in range(num - 1, 0, -1):
            print(f'x {c}', end=' ')
            f *= c
        print(f'= {num}')
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return print(f)


fatorial(5, show=True)
# help(fatorial)
