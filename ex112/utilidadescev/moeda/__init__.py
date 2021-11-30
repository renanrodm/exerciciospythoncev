def resumo(preço=0, aumento=10, redução=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado:  \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-' * 30)


def metade(preço=0, formatado=False):
    res = preço / 2
    if formatado:
        return moeda(res)
    else:
        return res


def dobro(preço=0, formatado=False):
    res = preço * 2
    if formatado:
        return moeda(res)
    else:
        return res


def aumentar(preço=0, taxa=0, formatado=False):
    res = preço * (1 + (taxa / 100))
    if formatado:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, taxa=0, formatado=False):
    res = preço * (1 - (taxa / 100))
    if formatado:
        return moeda(res)
    else:
        return res


def moeda(preço=0.0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace(".", ",")
