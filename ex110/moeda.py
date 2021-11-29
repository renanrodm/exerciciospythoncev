
def resumo(preço=0, aumento=0, redução=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado: ":<20}', f'{moeda(preço):<}')
    print(f'{"Dobro do preço:":<20}', f'{moeda(dobro(preço)):<}')
    print(f'{"Metade do preço:":<20}', f'{moeda(metade(preço)):<}')
    print(f'{f"{aumento}% de aumento:":<20}', f'{moeda(aumentar(preço, aumento)):<}')
    print(f'{f"{redução}% de redução:":<20}', f'{moeda(diminuir(preço, redução)):<}')
    print('-' * 30)


def metade(preço=0):
    return preço / 2


def dobro(preço=0):
    return preço * 2


def aumentar(preço=0, taxa=0):
    return preço * (1 + (taxa / 100))


def diminuir(preço=0, taxa=0):
    return preço * (1 - (taxa / 100))


def moeda(preço=0.0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace(".", ",")
