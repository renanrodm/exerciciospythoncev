def LeiaInt(str):
    ok = False
    valor = 0
    while True:
        n = str(input(str))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0:31mERRO! Digite um número inteiro válido.\033[0:0m')
        if ok:
            break
    return valor


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')