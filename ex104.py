'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n')'''


def LeiaInt(valor):
    cores = {'vermelho': '\033[0:31m', 'limpa': '\033[0:0m'}
    while True:
        num = input(valor)
        if num.isnumeric():
            break
        print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido.{cores["limpa"]}')
    return num


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')