''' Reescreva a função leiaInt(), incluindo agora a possibilidade de digitação da um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''


def LeiaFloat(str):
    while True:
        try:
            entrada = float(input(str))
        except:
            print(f'\033[1;31mERRO! Digite um número real válido.\033[0;0m')
            continue # <- Joga o programa pro inicio do loop
        else:
            return entrada


def LeiaInt(str):
    while True:
        try:
            entrada = int(input(str))
        except:
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[0;0m')
            continue # <- Joga o programa pro inicio do loop
        else:
            return entrada


n = LeiaInt('Digite um Inteiro: ')
n2 = LeiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real {n2}.')