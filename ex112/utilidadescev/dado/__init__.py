def leiaDinheiro(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return float(num)
        print(f'\033[1;31mERRO! {num} é um preço inválido!\033[0:0m')

