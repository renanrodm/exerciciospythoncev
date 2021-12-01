def leiaInt(str):
    while True:
        try:
            entrada = int(input(str))
        except:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[0;0m')
            continue # <- Joga o programa pro inicio do loop
        else:
            return entrada


def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lst):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lst:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    opc = leiaInt("\033[32mSua opção:\033[m ")
    return opc