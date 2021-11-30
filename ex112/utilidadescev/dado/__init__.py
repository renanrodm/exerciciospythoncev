def leiaDinheiro(msg):
    while True:
        num = input(msg)

        if "," in num:
            num = num.split(",")
        elif "." in num:
            num = num.split(".")
        else:
            num = num.split()

        if len(num) <= 2:
            cont = 0
            for c in num:
                if c.isnumeric():
                    cont += 1
            if cont == len(num):
                num = ".".join(num)
                return float(num)

        print(f'\033[1;31mERRO! "{num}" é um preço inválido!\033[0:0m')
