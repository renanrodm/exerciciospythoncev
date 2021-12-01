'''Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.'''

import urllib.request

try:
    r = urllib.request.urlopen(url="https://www.pudim.com.br")
except:
    print("O site não está acessível no momento..")
else:
    print("Consegui acessar o site com sucesso! ")
