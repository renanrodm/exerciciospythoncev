def metade(preço=0, formatação=False):
    res = preço / 2
    return res if not formatação else moeda(res)


def dobro(preço=0, formatação=False):
    res = preço * 2
    return res if not formatação else moeda(res)


def aumentar(preço=0, taxa=0, formatação=False):
    res = preço * (1 + (taxa / 100))
    if formatação:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, taxa=0, formatação=False):
    res = preço * (1 - (taxa / 100))
    if formatação:
        return moeda(res)
    else:
        return res


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace(".", ",")
