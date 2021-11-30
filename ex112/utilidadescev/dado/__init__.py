def leiaDinheiro(msg):
    while True:
        num = input(msg)
        num2 = num

        if "," in num:
            num = num.split(",")
        elif "." in num:
            num = num.split(".")
        #verifica se é número
        if len(num) == 2:
            if num[0].isnumeric() and num[1].isnumeric():
                num = num[0] + "." + num[1]
                return float(num)
        print(f'\033[1;31mERRO! "{num2}" é um preço inválido!\033[0:0m')

