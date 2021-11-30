def leiaDinheiro(msg):
    valido = False
    while not False:
        entrada = str(input(msg)).replace(",", ".")
        if entrada.isalpha() or entrada.strip() == "":
            print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[0:0m')
        else:
            valido = True
            return float(entrada)
