from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        cabeçalho("OPÇÃO 1")
    elif resposta == 2:
        cabeçalho("OPÇÃO 2")
    elif resposta == 3:
        cabeçalho('Saindo do sistema, até logo. :)')
        break
    else:
        print("\033[1;31mERRO: Por favor, digite uma opção válida.\033[0;0m")
    sleep(2)
